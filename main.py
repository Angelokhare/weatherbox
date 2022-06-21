from distutils.log import error
import requests
from requests.exceptions import ConnectionError
from multiprocessing import connection
from flask import *
import json
import datetime
import random
app = Flask(__name__)
df = datetime.date.today()
hj= datetime.timedelta(days=10)
gh=hj+ df
kl= gh.strftime("%d")
print(gh)

@app.route("/", methods=("POST", "GET"))
def welcome():
   hj=datetime.datetime.now().strftime("%Y")
   if request.method=="POST":
      return redirect(url_for("home"))
   return render_template("welcome.html", bot=hj)


@app.route("/welcome", methods=("POST", "GET"))
def home():
    if request.method=="POST":
      try:
         name = request.form['name'].lower()
         print(name)
    #    try:
         url = "https://yahoo-weather5.p.rapidapi.com/weather"

         querystring = {"location":{name},"format":"json","u":"c"}

         headers = {
	"X-RapidAPI-Key": "3c87ec6a25msh46b7d04fc169e7dp1cc42djsnd64003f09b54",
	"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
}

         response = requests.request("GET", url, headers=headers, params=querystring)
         fas=response.json()
      
         if {"message":"Internal Server Error"}==fas:
            print(response.text)
            dass= random.randint(0,4)
            print(dass)
            hj=datetime.datetime.now().strftime("%Y")
            return render_template("not.html", bot=hj, ran=dass)
         print(response.text)
         condition=fas["current_observation"]["condition"]
         locationstate=fas["location"]
    #    for fd in locationstate:
    #        print(locationstate[fd])   
         future=fas["forecasts"]
         print(len(future))
         kk= len(future)
         hg=datetime.datetime.now().strftime("%B %d")
         toon=datetime.datetime.now().strftime("%A")
         hj=datetime.datetime.now().strftime("%Y")
         hk=datetime.datetime.now().strftime("%B")
         astronomy=fas["current_observation"]["astronomy"]
         atmosphere=fas["current_observation"]["atmosphere"]
         wind=fas["current_observation"]["wind"]
    #    for gh in range(kk):   
    #     print(future[gh]["day"])  
    #    print(future[gh]["high"])  
         print(f"{toon}{hg}")
         df = datetime.date.today()
         ky= len(future)+1
         gf=[]
         gt=[]
         qk=[]
         for gh in range(1, ky): 
            hy= datetime.timedelta(days=gh)
            gh=hy+ df
            kl= gh.strftime("%d")
            an= gh.strftime("%B")
            ag= gh.strftime("%A")
            gf.append(str(kl))
            gt.append(an)
            qk.append(ag)
         print(gf)
         print(gt)
         print(qk)
         return render_template("search.html", jh=kk, future=future, condition=condition, location=locationstate, date=toon, bot=hj, astronomy=astronomy, loc=hg, atmosphere=atmosphere, wind=wind, gv=gf, mm=hk, er=gt, yu=qk)
      except ConnectionError:
         return redirect(url_for("home"))
    #         # return("error")
    hj=datetime.datetime.now().strftime("%Y")
    return render_template("index.html",bot=hj)

   #  http://l.yimg.com/a/i/us/we/52/9.gif
    # http://l.yimg.com/a/i/us/we/2/36.gif
    # https://l.yimg.com/a/i/us/we/52/9.gif
   

@app.route("/search", methods=("POST", "GET"))
def search():
    if request.method=="POST":
      try:
         name = request.form['name'].lower()
         print(name)
    #    try:
         url = "https://yahoo-weather5.p.rapidapi.com/weather"

         querystring = {"location":{name},"format":"json","u":"c"}

         headers = {
	"X-RapidAPI-Key": api,
	"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
}

         response = requests.request("GET", url, headers=headers, params=querystring)
         fas=response.json()
      
         if {"message":"Internal Server Error"}==fas:
            print(response.text)
            dass= random.randint(0,4)
            print(dass)
            hj=datetime.datetime.now().strftime("%Y")
            return render_template("not.html", bot=hj, ran=dass)
         print(response.text)
         condition=fas["current_observation"]["condition"]
         locationstate=fas["location"]
    #    for fd in locationstate:
    #        print(locationstate[fd])   
         future=fas["forecasts"]
         print(len(future))
         kk= len(future)
         hg=datetime.datetime.now().strftime("%B %d")
         toon=datetime.datetime.now().strftime("%A")
         hj=datetime.datetime.now().strftime("%Y")
         hk=datetime.datetime.now().strftime("%B")
         astronomy=fas["current_observation"]["astronomy"]
         atmosphere=fas["current_observation"]["atmosphere"]
         wind=fas["current_observation"]["wind"]
    #    for gh in range(kk):   
    #     print(future[gh]["day"])  
    #    print(future[gh]["high"])  
         print(f"{toon}{hg}")
         df = datetime.date.today()
         ky= len(future)+1
         gf=[]
         for gh in range(1, ky): 
            hy= datetime.timedelta(days=gh)
            gh=hy+ df
            kl= gh.strftime("%d")
            gf.append(str(kl))
         print(gf)
         return render_template("search.html", jh=kk, future=future, condition=condition, location=locationstate, date=toon, bot=hj, astronomy=astronomy, loc=hg, atmosphere=atmosphere, wind=wind, gv=gf, mm=hk)
      except ConnectionError:
         return redirect(url_for("home"))
    #         # return("error")
    hj=datetime.datetime.now().strftime("%Y")
    return render_template("search.html",bot=hj)


# @app.route("/result")
# def search():
#     return render_template("search.html")
    
   


if __name__ == "__main__":
    app.run(debug=True)












# from email import message
# from email.policy import default
# from platform import release
# from wsgiref.validate import validator
# from flask import Flask, render_template, redirect, url_for, request, flash
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_wtf import FlaskForm
# from wtforms import DateField, EmailField, IntegerField, PasswordField, SelectField, StringField, validators, SubmitField, BooleanField
# from wtforms.validators import DataRequired, Email, Length, InputRequired, EqualTo
# from datetime import datetime
# from flask_login import login_user, logout_user, LoginManager, UserMixin, login_required, current_user
# import time
# import requests
# from requests.adapters import HTTPAdapter
# import random



# app=Flask(__name__)
# app.config['SECRET_KEY'] = 'any secret string'
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///user.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db=SQLAlchemy(app)
# login_manager=LoginManager()
# login_manager.init_app(app)
# login_manager.login_view='Login'
# class User(UserMixin, db.Model):
#     username= db.Column(db.String(300), nullable=False, unique=True)
#     firstname= db.Column(db.String(300), nullable=False)
#     lastname= db.Column(db.String(300), nullable=False)
#     country= db.Column(db.String(300), nullable=False)
#     gender= db.Column(db.String(300), nullable=False)
#     id=db.Column(db.Integer, primary_key=True)
#     password=db.Column(db.String(200), nullable=False)
#     phone_number=db.Column(db.Integer, nullable=False)
#     # age=db.Column(db.Integer, nullable=False)
#     birthday= db.Column(db.String(200), nullable=False)
#     email=db.Column(db.String(200), nullable=False, unique=True)


# class Movie(UserMixin, db.Model):
#     title= db.Column(db.String(300), nullable=True)
#     overview= db.Column(db.String(300), nullable=True)
#     language= db.Column(db.String(300), nullable=True)
#     image= db.Column(db.String(300), nullable=True)
#     id=db.Column(db.Integer, primary_key=True)
#     rating=db.Column(db.Integer, nullable=True)
#     release= db.Column(db.String(200), nullable=True)   

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# class Signup(FlaskForm):
#     lastname = StringField(label="Lastname", validators=[DataRequired()])
#     firstname = StringField("Firstname", validators=[DataRequired()])
#     username = StringField(label="Username", validators=[DataRequired()])
#     gender= SelectField("Gender", validators=[DataRequired()], choices=["Male", "Female", "Prefer not to respond"])
#     country= SelectField("Country", validators=[DataRequired()], choices=['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia', 'the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'])
#     phone = IntegerField("Phone", validators=[DataRequired()])
#     email= EmailField('Email', validators=[Email(), DataRequired()])
#     birthdate = DateField("Date of Birth",validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired(), validators.Length(min=8)])
#     confpassword = PasswordField("Confirm password", validators=[DataRequired(), validators.Length(min=8)])
#     tick= BooleanField(validators=[DataRequired()])

#     submit= SubmitField("Sign up")

#     # lastname = StringField(label="Lastname", validators=[DataRequired("Please enter your lastname.")])
#     # firstname = StringField("Firstname", [validators.DataRequired("Please enter your firstname.")])
#     # username = StringField(label="Username", validators=[validators.DataRequired("Please enter your username.")])
#     # # age = IntegerField("Age", [validators.DataRequired("Please enter your Age.")])
#     # # gender=SelectField("Gender",choices=[Male", "Female", "Prefer not to respond"])
#     # gender= SelectField("Gender",[validators.DataRequired("Please enter your gender.")], choices=["Male", "Female", "Prefer not to respond"])
#     # country= SelectField("Country",[validators.DataRequired("Please enter your country.")], choices=['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia', 'the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'])
#     # phone = IntegerField("Phone", [validators.DataRequired("Please enter your phone number.")])
#     # # email = EmailField("Email", [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
#     # # email =email = StringField("Email", [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
#     # # email = EmailField("Email", [InputRequired("Please enter your email address."), Email("Please enter your email address.")])
#     # email= EmailField('Email', validators=[Email(), DataRequired()])
#     # birthdate = DateField("Date of Birth",[validators.DataRequired("Please Enter your date of birth")], format='%m/%d/%Y')
#     # confpassword = PasswordField("Confirm password", [validators.DataRequired("Please enter your password."), validators.Length(min=8)])
#     # password = PasswordField("Password", [validators.DataRequired("Please enter your password."), validators.Length(min=8), EqualTo('confpassword', message='Passwords must match'), validators.EqualTo('confirm', message='Passwords must match')])
#     # # confpassword = PasswordField("Confirm password", [validators.DataRequired("Please enter your password."), validators.Length(min=8)])
#     # tick= BooleanField(validators=[DataRequired()])
#     # # show = BooleanField('Show password', id='check')
#     # submit= SubmitField("Sign up")


# @app.route('/')
# def front():
#     toon=datetime.now().strftime("%d-%m")
#     big=datetime.now().strftime("%Y")
#     return render_template("index.html", today=toon, year=big)

# @app.route('/home')
# def home():
#     toon=datetime.now().strftime("%d-%m")
#     big=datetime.now().strftime("%Y")
#     return render_template("index.html", today=toon, year=big)

# # @app.route('/blog')
# # def blog():
# #     fem=t
# #     return render_template("blog.html",fem=fem)

# @app.route('/signup', methods=('GET', 'POST'))
# def signup():
#     big=datetime.now().strftime("%Y")
#     toon=datetime.now().strftime("%d-%m")
#     form = Signup()
#     if form.validate_on_submit():
#         print(form.username.data.lower())
#         print(form.birthdate.data)
#         if form.password.data== form.confpassword.data:
#             if User.query.filter_by(email=form.email.data).first():
#               flash("This Email has exited before!")
#               return redirect(url_for("invalide"))

#             elif User.query.filter_by(username=form.username.data).first():  
#                 flash("This username has exited before!")
#                 return redirect(url_for("invalidu"))
#             else:
#                 new_password = generate_password_hash(password=form.password.data, salt_length=8, method='pbkdf2:sha256')
#                 person= User(username=form.username.data.lower(), email=form.email.data.lower(), country=form.country.data.lower(), password=new_password, phone_number=form.phone.data, firstname=form.firstname.data.lower(), lastname=form.lastname.data.lower(), gender=form.gender.data.lower(), birthday=form.birthdate.data)
#                 print(form.username.data)
#                 db.session.add(person)
#                 db.session.commit()
#             return ("New user has been created!")
#         else:
#             flash(message="incorrect password")
#             return redirect(url_for("invalidp"))
#     return render_template("signup.html", form=form, year=big, today=toon)


# @app.route('/invalid-password', methods=('GET', 'POST'))
# def invalidp():
#     big=datetime.now().strftime("%Y")
#     toon=datetime.now().strftime("%d-%m")
#     form = Signup()
#     if form.validate_on_submit():
#         print(form.username.data)
#         print(form.birthdate.data)
#         if form.password.data== form.confpassword.data:
#             if User.query.filter_by(email=form.email.data).first():
#               flash("This Email has exited before!")
#               return redirect(url_for("invalide"))

#             elif User.query.filter_by(username=form.username.data).first():  
#                 flash("This username has exited before!")
#                 return redirect(url_for("invalidu"))
#             else:
#                 new_password = generate_password_hash(password=form.password.data, salt_length=8, method='pbkdf2:sha256')
#                 person= User(username=form.username.data, email=form.email.data, country=form.country.data, password=new_password, phone_number=form.phone.data, firstname=form.firstname.data, lastname=form.lastname.data, gender=form.gender.data, birthday=form.birthdate.data)
#                 print(form.username.data)
#                 db.session.add(person)
#                 db.session.commit()
#             return ("New user has been created!")
#         else:
#             flash(message="incorrect password")
#             return redirect(url_for("invalidp"))
#     fan="Password entered does not Match!"
#     dot="*"
#     return render_template("signup.html", form=form, year=big, today=toon, mess=fan, x=dot)


# @app.route('/invalid-email', methods=('GET', 'POST'))
# def invalide():
#     big=datetime.now().strftime("%Y")
#     toon=datetime.now().strftime("%d-%m")
#     form = Signup()
#     if form.validate_on_submit():
#         print(form.username.data)
#         print(form.birthdate.data)
#         if form.password.data== form.confpassword.data:
#             if User.query.filter_by(email=form.email.data).first():
#               flash("This account has exited before!")
#               return redirect(url_for("invalide"))

            
#             elif User.query.filter_by(username=form.username.data).first():  
#                 flash("This username has exited before!")
#                 return redirect(url_for("invalidu"))

#             else:
#                 new_password = generate_password_hash(password=form.password.data, salt_length=8, method='pbkdf2:sha256')
#                 person= User(username=form.username.data, email=form.email.data, country=form.country.data, password=new_password, phone_number=form.phone.data, firstname=form.firstname.data, lastname=form.lastname.data, gender=form.gender.data, birthday=form.birthdate.data)
#                 print(form.username.data)
#                 db.session.add(person)
#                 db.session.commit()
#             return ("New user has been created!")
#         else:
#             flash(message="incorrect password")
#             return redirect(url_for("invalidp"))
#     fan="EMAIL already exist!"
#     dot="*"
#     return render_template("signup.html", form=form, year=big, today=toon, mess=fan, y=dot)



# @app.route('/invalid-username', methods=('GET', 'POST'))
# def invalidu():
#     big=datetime.now().strftime("%Y")
#     toon=datetime.now().strftime("%d-%m")
#     form = Signup()
#     if form.validate_on_submit():
#         print(form.username.data)
#         print(form.birthdate.data)
#         if form.password.data== form.confpassword.data:
#             if User.query.filter_by(email=form.email.data).first():
#               flash("This Email has exited before!")
#               return redirect(url_for("invalide"))

#             elif User.query.filter_by(username=form.username.data).first():  
#                 flash("This username has exited before!")
#                 return redirect(url_for("invalidu"))
#             else:
#                 new_password = generate_password_hash(password=form.password.data, salt_length=8, method='pbkdf2:sha256')
#                 person= User(username=form.username.data, email=form.email.data, country=form.country.data, password=new_password, phone_number=form.phone.data, firstname=form.firstname.data, lastname=form.lastname.data, gender=form.gender.data, birthday=form.birthdate.data)
#                 print(form.username.data)
#                 db.session.add(person)
#                 db.session.commit()
#             return ("New user has been created!")
#         else:
#             flash(message="incorrect password")
#             return redirect(url_for("invalidp"))
#     fan="Username already exist!"
#     dot="*"
#     return render_template("signup.html", form=form, year=big, today=toon, mess=fan, z=dot)    



# @app.route('/login', methods=("POST", "GET"))
# def login():
#     toon=datetime.now().strftime("%d-%m")
#     big=datetime.now().strftime("%Y")
#     if request.method=="POST":
#         name = request.form['username'].lower()
#         password = request.form['password']
#         print(name)
#         print(password)
#         us= User.query.filter_by(email=name).first() 
#         using= User.query.filter_by(username=name).first()
#         if us :
#             flash("This account has exited before!")
#             if check_password_hash(us.password, request.form['password']):
#                 login_user(us)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida")) 
#         elif using:
#             flash("This account has exited before!")
#             if check_password_hash(using.password, request.form['password']):
#                 login_user(using)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida"))        

#         else:
#             return redirect(url_for("invalidl"))   
#     return render_template("login.html", year=big, today=toon)

# @app.route('/invalid-login-user', methods=("POST", "GET"))
# def invalidl():
#     toon=datetime.now().strftime("%d-%m")
#     big=datetime.now().strftime("%Y")
#     if request.method=="POST":
#         name = request.form['username'].lower()
#         password = request.form['password']
#         print(name)
#         print(password)
#         us= User.query.filter_by(email=name).first() 
#         using= User.query.filter_by(username=name).first()
#         if us:
#             flash("This account has exited before!")
#             if check_password_hash(us.password, request.form['password']):
#                 login_user(us)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida"))  
#         elif using:
#             flash("This account has exited before!")
#             if check_password_hash(using.password, request.form['password']):
#                 login_user(using)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida"))         

#         else:
#             return redirect(url_for("invalidl"))  
#     use="This account does not exit!"         
#     return render_template("login.html", year=big, today=toon, note=use)   


# @app.route('/invalid-login-password', methods=("POST", "GET"))
# def invalida():
#     toon=datetime.now().strftime("%d-%m")
#     big=datetime.now().strftime("%Y")
#     if request.method=="POST":
#         name = request.form['username'].lower()
#         password = request.form['password']
#         print(name)
#         print(password)
#         us= User.query.filter_by(email=name).first() 
#         using= User.query.filter_by(username=name).first()
#         if us:
#             flash("This account has exited before!")
#             if check_password_hash(us.password, request.form['password']):
#                 login_user(us)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida"))  

#         elif using:
#             flash("This account has exited before!")
#             if check_password_hash(using.password, request.form['password']):
#                 login_user(using)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida"))         

#         else:
#             return redirect(url_for("invalidl"))  
#     use="This password entered is incorrect!"         
#     return render_template("login.html", year=big, today=toon, note=use) 


# @app.route("/welcome")
# @login_required
# def user():
#     return render_template("user.html", name=current_user.username)


# # @app.route("/welcome")
# # def viv():
# #     return redirect("login") 

# @app.route("/logout-user")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("login"))   


# @app.route('/users-movie', methods=("POST", "GET"))  
# @login_required
# def movie():
#     if request.method=="POST":
#         toon=datetime.now().strftime("%d-%m")
#         viv=datetime.today().strftime('%A').lower()
#         name = request.form['name'].lower()   
#         if name==[]:
#             return render_template("movie.html", dis=viv, today=toon)
#         else:    
#              md="1affd879f3e8aac72ebe06eb3db99dc1"
#              ma="a7f423ca02d4c7d3280f566396d8e180"
#              mc="6a4570c97e3acf8ac318f2bca3ed09cd"
#              mf="8e49fca814ae244c2b6949e2ede67661"
#              letters=[md, ma, mc, mf]
#              hh=random.randint(0,len(letters)-1)
#              vv=letters[hh]
#              print(letters[hh]) 
#              print(name)
#              response = requests.get("https://api.themoviedb.org/3/search/movie", params={"api_key": letters[hh], "query": name})
#              data = response.json()["results"]
#              print(vv)
#              if data==[]:
#                 fame = request.form['name']
#                 dam= f"{fame} not found!"
#                 return render_template("movie.html", dam=dam, dis=viv, today=toon)
#              else:
#                 #  print(data)
#                 print(vv)
#                 return render_template("movieshow.html", feg=data)
#     toon=datetime.now().strftime("%d-%m")
#     viv=datetime.today().strftime('%A').lower()
#     return render_template("movie.html", dis=viv, today=toon)   
# viv=datetime.today().strftime('%A').lower()
# print(viv)


# # @app.route('/showcase-movie', methods=("POST", "GET"))
# # @login_required
# # def showcase():
# #     viv=datetime.today().strftime('%A').lower()
# #     if request.method=="POST":
# #         name = request.form['name'].lower()
# #         print(name)
# #         response = requests.get("https://api.themoviedb.org/4/search/movie", params={"api_key": "a7f423ca02d4c7d3280f566396d8e180", "query": name})
# #         data = response.json()["results"]
# #         print(data)
# #         return render_template(("movieshow.html"), feg=data)
# #     return render_template("movieshow.html", dis=viv)
# # 

# if __name__=='__main__':
#     app.run(debug=True)






















































































# # from flask import Flask, flash, render_template, request, url_for, redirect
# # from datetime import datetime
# # from flask_wtf import FlaskForm
# # from werkzeug.security import check_password_hash, generate_password_hash
# # from wtforms import StringField, PasswordField, SelectField, SubmitField, IntegerField
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_login import login_user, logout_user, LoginManager, UserMixin, login_required, current_user
# # from wtforms.validators import DataRequired, Email, Length, number_range

# # app=Flask(__name__)
# # app.config["SQLALCHEMY_DATABASE_URL"]="sqlite///game.db"
# # app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
# # db=SQLAlchemy(app)

# # login_manage=LoginManager
# # login_manage.init_app(app)

# # class Signup(FlaskForm):
# #     email=StringField(label="Username", validators=[DataRequired(), Email()])
#     # password=PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
# #     username=StringField(label="Name", validators=DataRequired("Pls enter your name!"))
# #     phone_number=IntegerField(label="Phone number", validators=[DataRequired(), number_range()])
# #     submit=SubmitField(label="Submit")

# # class Storage(db.Model, UserMixin):
# #     username= db.Column(db.String(300), nullable=False, unique=True)
# #     id=db.Column(db.Integer, primary_key=True)
# #     password=db.Column(db.String(200), nullable=False)
# #     phone_number=db.Column(db.Integer, nullable=False)
# #     email=db.Column(db.String(200), nullable=False, unique=True)
# # db.create_all()

# # date=datetime.now().strftime("%Y")
# # @app.route('/')
# # def home():
# #     return render_template("index.html")

# # @app.route('/register')
# # def register():
# #     form= Signup()
# #     if form.validate_on_submit():
# #         if Storage.query.filter_by(email=form.email.data).first() or Storage.query.filter_by(username=form.username.data).first():
# #             flash("This account has exited before!")
# #             redirect(url_for("register"))
# #         else:
# #             new_password = generate_password_hash(password=form.password.data, salt_length=8, method='pbkdf2:sha256')
# #             new_person=Storage(password=new_password, username=form.username.data, email=form.email.data)
# #             db.session.add(new_person)
# #             db.session.commit()
# #             redirect(url_for("welcome"))

# #     return render_template("register.html")

# # @app.route('/login')
# # def login():
# #     form=Signup()
# #     email=form.email.data
# #     password=form.password.data
# #     user = Storage.query.filter_by(email=email).first()
# #     if form.validate_on_submit():
# #         if not user:
# #           flash("Email not recognised!")
# #           redirect(url_for("login"))
# #         elif check_password_hash(user.password, password):
# #             flash("Incorrect Password!")
# #             redirect(url_for("login"))
# #         else:
# #             user= Storage.query.filter_by(email=email).first()
# #             check_password_hash(user.password, password)
# #             login_user(user)
# #             redirect("welcome.html")
# #     return render_template("login.html")


# # @app.route('/welcome')
# # @login_required
# # def welcome():
# #     current_user.username
# #     return render_template("welcome.html")




# # if __name__=='__main__':
# #     app.run(debug=True)



























