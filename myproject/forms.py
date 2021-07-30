from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, email_validator
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('电子邮件', validators=[DataRequired(), Email()])
    password = PasswordField('密码',validators=[DataRequired()])
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('电子邮件', validators=[DataRequired(), Email()])
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired(), EqualTo('pass_confirm', message='密码不一致')])
    pass_confirm = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('注册')
    
    def check_email(self, field):
        """檢查Email"""
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')
    def check_username(self, field):
        """檢查username"""
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')