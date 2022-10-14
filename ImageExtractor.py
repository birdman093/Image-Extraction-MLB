"""Image Extractor grabs MLB Showdown images for each player given the name

base: https://www.showdowncards.com/store/
input: card number, name, set name 
set names: 2000, ....

sample: https://www.showdowncards.com/store/4-darin-erstad-mlb-showdown-2000
"""

from bs4 import BeautifulSoup
import requests
import os

def urlImageExtractor(number, player, setName):
    urlSearch = urlPlayer(number,player,setName)
    htmlText = requests.get(urlSearch).text
    soup = BeautifulSoup(htmlText, 'lxml')
    images = soup.find_all('img')
    # need to go into src, grab url, then save image
    for image in images:
        if ".jpg" in image['src']:
            newURL = image['src']
            break    

    i = 0 
    while len(newURL) > i:
        if newURL[i] == ".":
            i += 1
        else:
            break
    baseImageURL = "https://www.showdowncards.com"
    return baseImageURL + newURL[i:]

def urlPlayer(number, player, setName):
    baseURL = "https://www.showdowncards.com/store/"
    splitName = player.split()
    URLbuild = [number, splitName[0], splitName[1], "mlb", "showdown", setName]
    baseURL += URLbuild[0]
    for i in range(1, len(URLbuild)):
        baseURL += "-" + URLbuild[i]
    return baseURL
    
def playerImageDL(number, player, setName, directory):
    imageURL = urlImageExtractor(number, player, setName)
    page = requests.get(imageURL)
    f_ext = os.path.splitext(imageURL)[-1]
    f_name = directory + number + '_' + player + '_' + setName + '{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)
    
if __name__ == "__main__":
    player = "darin erstad"
    number = "4"
    setName = "2000"
    directory = "ImageStorage/"
    playerImageDL(number, player, setName, directory)
