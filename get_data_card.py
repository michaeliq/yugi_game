import requests
from bs4 import BeautifulSoup as bs

class Card():

    def __init__(self,url_card):
        self.url_card = url_card

        self.type = ""
        self.name_card = ""
        self.description = ""
        self.attack = 0
        self.defens = 0
        self.efects = []
        self.image = ""

    def __call__(self):
        self.get_type()
        self.get_name_card()
        self.get_description()
        self.get_attack()
        self.get_defens()
        self.set_efects()
        self.get_image()

    def get_image(self):
        re = requests.get(self.url_card)
        soup = bs(re.content,"html.parser")
        a = soup.find('a',class_="image image-thumbnail")
        self.image = a.img["src"]
        print("url's image was set up")
