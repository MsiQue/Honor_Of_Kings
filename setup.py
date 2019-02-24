from app import db
from models import *
from spider import getInfo

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    getInfo()
