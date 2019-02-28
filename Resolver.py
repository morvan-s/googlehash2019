from Photo import Photo
from Slide import Slide

MAX_LIMIT = 1000
class Resolver:

    def __init__(self, inputFile):
        self.inputFile = inputFile
        self.slidesByTags = {}
        self.verticalPhotos = []
        self.readInput(inputFile)
        print(self.find_moyenne())

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
        a = self.verticalPhotos.shift()
        b = self.verticalPhotos[0]
        dist = len(set(a.tags+b.tags))
        best_dist = dist
        index_b = 1
        while (dist < moyenne * 0.95 and dist > moyenne * 1.05) and (index_b < len(self.verticalPhotos)):
            dist = len(set(a.tags+self.verticalPhotos[index_b].tags))
            if abs(moyenne - dist) < abs(moyenne - best_dist):
                best_dist = dist
                b =  self.verticalPhotos[index_b]
            index_b += 1
        return a,b

    def vertical_merge(self):
        moy = find_moyenne(self)
        while(self.verticalPhotos > 0):
            a,b = find_vertical_merge(r,moy)
            s = Slide([a,b])
            for t in set(a.tags,b.tags):
                print(t)
