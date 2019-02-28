from Photo import Photo
from Slide import Slide

class Resolver:
    def __init__(self, inputFile):
        self.inputFile = inputFile
        self.slidesByTags = {}
        self.verticalPhotos = []
        self.readInput(inputFile)

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

    def mergeVerticalPhotosAsSlides():
        return

    def solveSlideShow():
        return
