import json
import re
from bs4 import BeautifulSoup
from functions import GetHtmlText
from models import *

def toolInfoGet():
    f = open('item.json', 'r', encoding = 'utf-8')
    item = json.load(f)
    for a in item:
        Str1 = re.sub('<br>', '\n', a['des1'][3:-4])
        Str2 = re.sub('[<>/]', '', Str1)
        Item = toolInfo(a['item_id'], a['item_name'], a['price'], a['total_price'], Str2)
        db.session.add(Item)
        db.session.commit()

def summonerInfoGet():
    f = open('summoner.json', 'r', encoding = 'utf-8')
    item = json.load(f)
    for a in item:
        Item = summonerInfo(a['summoner_id'], a['summoner_name'], a['summoner_rank'], a['summoner_description'])
        db.session.add(Item)
        db.session.commit()



def Analyze(RE, Text):
    match = re.search(RE, Text)
    if match:
        A = match.group(0)
        B = A.split('%')[0]
        return eval(B[-2]) * 10
    else:
        return 100

def Solve(num):
    url_1 = 'http://pvp.qq.com/web201605/herodetail/'
    url_2 = '.shtml'
    Text = GetHtmlText(url_1 + str(num) + url_2)
    if (Text != None):
        soup = BeautifulSoup(Text, 'html.parser')
        id = num
        name = soup.h2.string
        hp  = Analyze(r'<span class="cover-list-bar data-bar1 fl"><b class="icon"></b><i class="ibar" style="width:[1-9]0%"></i></span>', Text)
        atk = Analyze(r'<span class="cover-list-bar data-bar2 fl"><b class="icon"></b><i class="ibar" style="width:[1-9]0%"></i></span>', Text)
        eff = Analyze(r'<span class="cover-list-bar data-bar3 fl"><b class="icon"></b><i class="ibar" style="width:[1-9]0%"></i></span>', Text)
        dfc = Analyze(r'<span class="cover-list-bar data-bar4 fl"><b class="icon"></b><i class="ibar" style="width:[1-9]0%"></i></span>', Text)
        match = re.search(r'data-imgname="[^"]*', Text)
        skin = re.sub(r'\|', ',', match.group(0).split('"')[1])
        Item = heroInfo(id, name, hp, atk, eff, dfc, skin)
        db.session.add(Item)
        db.session.commit()

def heroInfoGet():
    for i in range(100, 530):
        print(i)
        Solve(i)

def getInfo():
    toolInfoGet()
    summonerInfoGet()
    heroInfoGet()


