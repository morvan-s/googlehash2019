class Slide:
    def __init__(self, photos):
        self.photos = photos

    def tags(self):
        sum_tags = []
        for p in self.photos:
            sum_tags += p.tags
        return list(set(sum_tags))
