from flask import Flask,render_template,url_for,flash,request

import sqlite3


app = Flask(__name__)


@app.route('/' , )
def hello_world():
    indexCss=url_for("static",filename="css/indexCss.css")
    mainJs=url_for("static",filename="js/main_part.js")
    loginButton=url_for("static",filename="images/loginButton.png")
    login=url_for("static",filename="images/login.jpg")
    titlePic=url_for("static",filename="images/title.png")
    ex1=url_for("static",filename="images/ex1.jpg")
    ex2=url_for("static",filename="images/ex2.jpg")
    ex3=url_for("static",filename="images/ex3.png")
    titleBg=url_for("static",filename="images/titleBg.png")
    modelBg=url_for("static",filename="images/modelBg.jpg")
    bg=url_for("static",filename="images/bg.jpg")
    return render_template("index.html",mainJs=mainJs,indexCss=indexCss,loginButton=loginButton,login=login,titlePic=titlePic,ex1=ex1,ex2=ex2,ex3=ex3,titleBg=titleBg,modelBg=modelBg,bg=bg)




    
@app.route('/moreInfo')
def init():
    registerBkg=url_for("static",filename="images/registerBg.jpg")
    moreInfoCss=url_for("static",filename="css/moreInfoCss.css")
    return render_template("moreInfo.html",moreInfoCss=moreInfoCss,registerBkg=registerBkg);

if __name__ == '__main__':
    app.run()