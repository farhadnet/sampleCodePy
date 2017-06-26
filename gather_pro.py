from HTMLParser import HTMLParser
import urllib

class GatherLinks(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self,tag,attrs):
        if tag == 'a':
           for name,value in attrs:
               if name == 'href':
                   self.links.append(value)


parser = GatherLinks()
data = urllib.urlopen("http://www.python.org").read()
parser.feed(data)
count = 0
for x in parser.links:
    print x
    count+=1

print count
