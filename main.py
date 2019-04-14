from flask import Flask, redirect, request
from flask import render_template
import requests
import json


foods = []
images = {
    'Apples' : 'https://media.self.com/photos/5b6b0b0cbb7f036f7f5cbcfa/4:3/w_728,c_limit/apples.jpg', #apples
    'Cattle' : 'https://d1lds9cvq82c7x.cloudfront.net/wp-content/uploads/2017/10/ln280510wink_6.jpg', #cattle
    'Chicken' : 'https://cms.splendidtable.org/sites/default/files/styles/w2000/public/chickens_buhanovskiy-iStock-GettyImagesPlus-LEDE.jpg?itok=kfjgEEAy%27', #chicken
    'Corn' : 'https://greenstar.coop/wp-content/uploads/2017/08/corn.jpg', #corn
    'Cotton' : 'https://nnimgt-a.akamaihd.net/transform/v1/crop/frm/yLeFMnh28MAxupuQMFvs9Q/7a7644c6-4532-4b18-9abc-90d0bf83f2aa.jpg/r0_81_1575_966_w1200_h678_fmax.jpg', #cotton
    'Eggs' : 'https://cdn1.medicalnewstoday.com/content/images/articles/323/323001/bowl-full-of-eggs.jpg', #eggs
    'Grapefruit' : 'https://cdn-img.health.com/sites/default/files/styles/medium_16_9/public/1472825151/9-GettyImages-184129838_high.jpg?itok=crCO6ve1', #grapefruit
    'Hay' : 'https://i.ebayimg.com/00/s/NjgxWDEwMjQ=/z/BKAAAOSw76BbfXmU/$_86.JPG', #hay
    'Hogs' : 'https://www.recordherald.com/wp-content/uploads/sites/27/2016/07/web1_Data-Hogs.jpg', #hogs
    'Ice cream' : 'https://img.taste.com.au/6CgraiFM/w720-h480-cfill-q80/taste/2017/12/roasted-peach-sour-cream-ice-cream-taste_1980x1320-133837-1.jpg', #ice cream
    'Milk' : 'https://vtnews.vt.edu/content/vtnews_vt_edu/en/articles/2018/09/cals-cancer/_jcr_content/article-image.transform/m-medium/image.jpg', #milk
    'Orange' : 'https://www.coindesk.com/wp-content/uploads/2017/07/orange.jpg', #orange
    'Peanuts' : 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/peanuts-royalty-free-image-616003590-1532549624.jpg?crop=1.00xw:0.824xh;0,0.0391xh&resize=480:*'
}
error = " "

app = Flask(__name__)
@app.route('/')
@app.route("/home")
def home():
    key = 'B8A86D31-1C0C-3E04-B6EA-0FDA97232001'
    state_alpha = "NC"
    agg_level_desc = 'STATE'
    year__GE = '2019'
    param = 'commodity_desc'
    begin_code = '02'
    URL = 'http://quickstats.nass.usda.gov/api/get_param_values/?key=' + key + '&state_alpha=' + state_alpha + '&agg_level_desc=' + agg_level_desc + '&year__GE=' + year__GE + '&param=' + param + '&begin_code=' + begin_code

    # Southern Region
    addFoods('WV', URL)
    addFoods('VA', URL)
    addFoods('NC', URL)
    addFoods('SC', URL)
    addFoods('TN', URL)
    addFoods('AR', URL)
    addFoods('LA', URL)
    addFoods('MS', URL)
    addFoods('AL', URL)
    addFoods('GA', URL)
    addFoods('FL', URL)
    foods = removeDupes()




    return render_template('produce.html', list = foods, err = error)


def addFoods(state, URL):
    state_alpha = state
    URL = URL + '&state_alpha=' + state_alpha
    r = requests.get(url = URL)
    data = r.json()

    for item in data["commodity_desc"]:
        foods.append(item.lower().capitalize())

def removeDupes():
    uniqueList = []
    for elem in foods:
        if elem not in uniqueList:
            uniqueList.append(elem)
    uniqueList.sort()
    return uniqueList

@app.route('/apple')
def apple():
    apple = 'Apple'
    return render_template('apple.html', product = apple)

@app.route('/cattle')
def cattle():
    cattle = 'Cattle'
    return render_template('cattle.html', product = cattle)

@app.route('/chicken')
def chicken():
    chicken = 'Chicken'
    return render_template('chicken.html', product = chicken)

@app.route('/corn')
def corn():
    corn = 'Corn'
    return render_template('corn.html', product = corn)

@app.route('/cotton')
def cotton():
    cotton = 'Cotton'
    return render_template('cotton.html', product = cotton)

@app.route('/egg')
def egg():
    egg = 'Eggs'
    return render_template('egg.html', product = egg)

@app.route('/grapefruit')
def grapefruit():
    grapefruit = 'Grapefruit'
    return render_template('grapefruit.html', product = grapefruit)

@app.route('/hay')
def hay():
    hay = 'Hay'
    return render_template('hay.html', product = hay)

@app.route('/hog')
def hog():
    hog = 'Hogs'
    return render_template('hog.html', product = hog)

@app.route('/icecream')
def icecream():
    icecream = 'Ice Cream'
    return render_template('icecream.html', product = icecream)

@app.route('/milk')
def milk():
    milk = 'Milk'
    return render_template('milk.html', product = milk)

@app.route('/orange')
def orange():
    orange = 'Oranges'
    return render_template('orange.html', product = orange)

@app.route('/peanut')
def peanut():
    peanut = 'Peanuts'
    return render_template('peanut.html', product = peanut)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      food = result.get('Produce')
      altFood = result.get('Produce')
      if checkFood(food) == True:
          return render_template('result.html',result = result, pictures = images, fType = altFood)
      else:
        error = 'Not Available'
        return home()

def checkFood(food):
    for x in foods:
        if x == food:
            return True
    return False



if __name__ == '__main__':
    app.run(debug = True)\
