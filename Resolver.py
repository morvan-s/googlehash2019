class Resolver:
    def __init__(self, inputFile):
        self.inputFile = inputFile
        self.slidesByTags = {}
        self.verticalPhotos = []
        self.readInput(inputFile)

    def readInput(self,file):
        with open('input/'+file) as fp:
            numberimages = int(fp.readline())
            for numero in range(0,numberimages):
                temp = fp.readline()[:-1].split(' ')
                orientation = temp[0]
                tags = []
                for t in temp[2:]:
                    tags.append(t)


    def mergeVerticalPhotosAsSlides():
        return

    def solveSlideShow():
        return
