class Page:
    def __init__(self, link, type):
        self.link = link
        self.type = type
        self.sublinks = []

    def appendLink(self, subpage):
        self.sublinks.append(subpage)

    def toString(self):
        return "{ type: " + self.type + ", url: " + self.link + ", sublinks: " + str(self.sublinks) + "}"

    def __repr__(self):
        return self.toString();

    def __str__(self):
        return self.toString();
