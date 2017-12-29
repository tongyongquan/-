#encoding: utf-8

from exts import db
from flask import Flask,request,redirect,url_for,session
import config
from flask import render_template
from models import  User,Question
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username,User.password == password).first()
        if user :
            session['user_id'] = user.id
            #如果要保存cookie 31天
            #session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'用户名或密码错误'


@app.route('/regist',methods=['POST','GET'])
def regist():
   if request.method=='GET':
       return render_template('regist.html')
   else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user= User.query.filter(User.username==username).first()
        if user:
            return u'该用户名已被注册'
        else:
            if password1!=password2:
                return u'两次密码输入不相同'
            else:
                user = User(username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/question',methods=(['POST','GET']))
@login_required
def question():
    if request.method=='GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id==user_id).first()
        question.author=user
        db.session.add(question)
        db.session.commit()
        return  redirect(url_for('index'))


@app.route('/test')
def test():
    return render_template('01.html')

if __name__ == '__main__':
    app.run()
