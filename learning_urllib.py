import urllib.request, urllib.parse, urllib.error
if __name__ == '__main__':
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand:
        print(line.decode().strip())