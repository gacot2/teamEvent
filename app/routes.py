
from flask import Flask
from werkzeug.utils import redirect 
from app import app
from flask import render_template, flash, redirect

from app.models.forms import LoginForm, RegistrationForm




@app.route("/")
# define the view using a function, which returns a string
def hello_world(name =None):
    return render_template('index.html', name = name)


@app.route('/reg', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.dateOfBirth)
    if form.validate_on_submit():
        flash('User {} is registred'.format(
            form.firstName, form.lastName
        ))
        print(form.firstName, form.lastName)
        return redirect('/')
    return render_template('registration.html', title = 'Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #passing the login form model
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.email.data))
        #get the email of the user    
        print("HEYYY",form.email)
        return redirect('/')

    return render_template('login.html', title = 'Sign In', form = form)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)