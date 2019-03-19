from urllib.parse import urlparse

class Page:
    def __init__(self, link, type, domain_url):
        self.link = link
        self.type = type
        self.sublinks = []
        self.absolute_url = Page.get_absolute(link, domain_url)

    def appendLink(self, subpage):
        self.sublinks.append(subpage)

    def toString(self):
        return "{ type: " + self.type + ", url: " + self.link + " absolute: " + self.absolute_url + ", sublinks: " + str(self.sublinks) + "}"

    def __eq__(self, other):
        if isinstance(other, Page):
            return self.link == other.link
        return False

    def __repr__(self):
        return self.toString();

    def __str__(self):
        return self.toString();

    @staticmethod
    def is_absolute(url):
        return bool(urlparse(url).netloc)

    @staticmethod
    def get_absolute(url, domain):
        if Page.is_absolute(url):
            return url
        else:
            return (str(domain) + "/" + url).replace("//", "/")
