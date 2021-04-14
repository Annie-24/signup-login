from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from passlib.hash import sha256_crypt
engine = create_engine("mysql+pymysql://Annie24:@localhost/register")
                       #(mysql+pymysql://username:@localhost/databasename)
db=scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


#register form

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        secure_password = sha256_crypt.encrypt(str(password))


        if password == confirm:
            db.execute("INSERT INTO users(name, email, password) VALUES(:name,:email,:password)",
                                  {"name":name,"email":email,"password":secure_password})
            db.commit()
            flash("you are registered and can login", "success")
            return redirect(url_for('login'))
        else:
            flash("password does not match", "danger")
            return render_template("register.html")                                  

    return render_template("register.html") 

#Login form
@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        emaildata = db.execute("SELECT email FROM users WHERE email=:email",{"email":email}).fetchone()
        passwordata = db.execute("SELECT password FROM users WHERE email=:email",{"email":email}).fetchone()


        if email != email:
            flash("No email","danger")
            return render_template("login.html")
        else:
            for passwor_data in passwordata:
                if sha256_crypt.verify(password,passwor_data):
                    flash("You are now login","success")
                    return redirect(url_for('home'))
                else:
                    flash("incorrect password","danger")
                    return render_template("login.html")        
    return render_template("login.html")     




if __name__ == ("__main__"):
    app.secret_key="supersecret80"
    app.run(debug=True)