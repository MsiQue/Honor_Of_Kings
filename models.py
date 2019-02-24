from app import db

class heroInfo(db.Model):
    __tablename__ = 'hero'
    id = db.Column(db.Integer, primary_key = True)  #英雄编号
    name = db.Column(db.String(100))                #英雄名称
    hp = db.Column(db.Integer)                      #生存能力
    atk = db.Column(db.Integer)                     #攻击伤害
    eff = db.Column(db.Integer)                     #技能效果
    dfc = db.Column(db.Integer)                     #上手难度
    skin = db.Column(db.String(100))                #皮肤名称

    def __init__(self, id, name, hp, atk, eff, dfc, skin):
        self.id = id
        self.name = name
        self.hp = hp
        self.atk = atk
        self.eff = eff
        self.dfc = dfc
        self.skin = skin

class summonerInfo(db.Model):
    __tablename__ = 'summoner'
    id = db.Column(db.Integer, primary_key=True)    #技能编号
    name = db.Column(db.String(100))                #技能名称
    rank = db.Column(db.String(100))                #解锁等级
    desc = db.Column(db.String(500))                #技能描述

    def __init__(self, id, name, rank, desc):
        self.id = id
        self.name = name
        self.rank = rank
        self.desc = desc


class toolInfo(db.Model):
    __tablename__ = 'tool'
    id = db.Column(db.Integer, primary_key=True)    #道具编号
    name = db.Column(db.String(100))                #道具名称
    price = db.Column(db.Integer)                   #道具售价
    total_price = db.Column(db.Integer)             #道具总价
    effection = db.Column(db.String(1000))          #道具效果

    def __init__(self, id, name, price, total_price, effection):
        self.id = id
        self.name = name
        self.price = price
        self.total_price = total_price
        self.effection = effection

