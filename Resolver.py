from Photo import Photo
from Slide import Slide

MAX_LIMIT = 1000
class Resolver:

    def __init__(self, inputName):
        self.inputName = inputName
        self.slidesByTags = {}
        self.verticalPhotos = []
        self.slideshow = []
        self.readInput("inputs/" + inputName + '.txt')
        self.vertical_merge()
        self.complete_slideshow()
        self.writeOutput("outputs/" + inputName + '.txt')

    def readInput(self,inputFile):
        with open(inputFile) as fp:
            numberimages = int(fp.readline())
            for id in range(0,numberimages):
                temp = fp.readline()[:-1].split(' ')
                orientation = temp[0]
                tags = []
                for t in temp[2:]:
                    tags.append(t)
                photo = Photo(id, orientation, tags)
                if orientation == 'H':
                    slide = Slide([photo])
                    for tag in tags:
                        if tag not in self.slidesByTags.keys():
                            self.slidesByTags[tag] = []
                        self.slidesByTags[tag].append(slide)
                else:
                    self.verticalPhotos.append(photo)

    def find_moyenne(self):
        number_tags = 0
        limit = len(self.verticalPhotos) if len(self.verticalPhotos) < MAX_LIMIT else MAX_LIMIT
        for i in range(0,limit):
            for u in range(0,limit):
                number = len(set(self.verticalPhotos[i].tags + self.verticalPhotos[u].tags))
                number_tags += number
        return 0 if limit == 0 else number_tags / limit

    def find_vertical_merge(self, moyenne):
        assert len(self.verticalPhotos) > 1
        a = self.verticalPhotos.pop()
        b = self.verticalPhotos[0]
        dist = len(set(a.tags+b.tags))
        best_dist = dist
        index_b = 1
        best_index_b = 0
        while (dist < moyenne * 0.95 and dist > moyenne * 1.05) and (index_b < len(self.verticalPhotos)):
            dist = len(set(a.tags+self.verticalPhotos[index_b].tags))
            if abs(moyenne - dist) < abs(moyenne - best_dist):
                best_dist = dist
                best_index_b = index_b
                b =  self.verticalPhotos[index_b]
            index_b += 1
        del self.verticalPhotos[best_index_b]
        return a,b

    def vertical_merge(self):
        moy = self.find_moyenne()
        while(len(self.verticalPhotos) > 0):
            a,b = self.find_vertical_merge(moy)
            s = Slide([a,b])
            for t in set(a.tags+b.tags):
                if t not in self.slidesByTags.keys():
                    self.slidesByTags[t] = []
                self.slidesByTags[t].append(s)

    def score_beetween_slide(self,a,b):
        in_a={}
        in_both={}
        in_b={}
        for t in a.tags():
            if t in b.tags():
                in_both[t] = True
            else:
                in_a[t] = True
        for t in b.tags():
            if t not in a.tags():
                in_b[t] = True
        return min(len(in_a.keys()),len(in_both.keys()),len(in_b.keys()))

    def complete_slideshow(self):
        current_slide = list(self.slidesByTags.values())[0][0]
        best_voisin = current_slide

        while(best_voisin != None):
            best_voisin = None
            voisins = {}

            self.slideshow.append(current_slide)
            #remove les tags associé à l'objet current
            for tag in current_slide.tags():
                self.slidesByTags[tag].remove(current_slide)

            best_voisin_score = 1000000000000000
            for current_tags in current_slide.tags():
                for v in self.slidesByTags[current_tags]:
                    if v not in voisins:
                        voisins[v]=True
                        score = self.score_beetween_slide(current_slide,v)
                        if score < best_voisin_score:
                            best_voisin_score = score
                            best_voisin = v
            if best_voisin == None: best_voisin = self.find_another_voisin()
            current_slide = best_voisin

    def find_another_voisin(self):
        res = None
        for l in list(self.slidesByTags.values()):
            if len(l) >= 1:
                return l[0]
        return res

    def writeOutput(self, outputFile):
        file = open(outputFile, "w")
        file.write(str(len(self.slideshow)) + "\n")
        for slide in self.slideshow:
            for i in range(0,len(slide.photos)):
                photo = slide.photos[i]
                file.write((" " if i != 0 else "") + str(photo.id))
            file.write("\n")
        file.close()
