'''
Author: your name
Date: 2021-07-27 20:28:31
LastEditTime: 2021-07-29 12:49:47
LastEditors: your name
Description: In User Settings Edit
FilePath: \flask\app.py
'''
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, logout_user, login_required
from myproject import app, db
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user.check_password(form.password.data) and user is not None:
                login_user(user)
                flash("登录成功")
                next = request.args.get('next')
                if next == None or not next[0]=='/':
                    next = url_for('welcome_user')
                return redirect(next)
    return render_template('login.html',form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("已退出系统")
    return redirect(url_for('home'))

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
        username=form.username.data, password=form.password.data)
        
        # add to db table
        db.session.add(user)
        db.session.commit()
        flash("感谢注册")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

if __name__ == '__main__':
    app.run(debug=True)