from flask import *
from app import app
from models import *


@app.route('/')
def index():
    return render_template('entrance.html')


@app.route('/Hero')
def Hero():
    return render_template('hero.html')


@app.route('/Hero/Query', methods=['GET', 'POST'])
def queryHero():
    name = request.form.get("name")
    a = heroInfo.query.filter(heroInfo.name == name).first()
    if (a):
        return render_template('response_hero.html', A=a)
    else:
        return '未找到'


@app.route('/Summoner')
def Summoner():
    return render_template('summoner.html')


@app.route('/Summoner/Query', methods=['GET', 'POST'])
def querySummoner():
    name = request.form.get("name")
    a = summonerInfo.query.filter(summonerInfo.name == name).first()
    if (a):
        return render_template('response_summoner.html', A=a)
    else:
        return '未找到'


@app.route('/Tool')
def Tool():
    return render_template('tool.html')


@app.route('/Tool/Query', methods=['GET', 'POST'])
def queryTool():
    name = request.form.get("name")
    a = toolInfo.query.filter(toolInfo.name == name).first()
    if (a):
        return render_template('response_tool.html', A=a)
    else:
        return '未找到'
