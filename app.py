from flask import Flask, render_template, request, url_for

app = Flask(__name__)
# Basic setup ^^^^

# class

class USER:
    def __init__ (self, fname = None, lname = "Re", email = None):
        self.fname = fname
        self.lname = lname
        self.email = email
user = USER()

@app.route('/')
def HomePage():
    return render_template('NOT_SIGNED_IN/index.html')

@app.route('/complain')
def Complain():
    return render_template('NOT_SIGNED_IN/complain.html')

@app.route('/ordering1')
def Ordering():
    return render_template('NOT_SIGNED_IN/ordering1.html')

@app.route('/sign_up')
def SignUp():
    return render_template('NOT_SIGNED_IN/sign_up.html',url=url_for('SignInForm'))
# FORM FILLOUT vvvv

# Completed.html(Cass)
@app.route('/SIGNED_IN/index2', methods=['GET', 'POST'])
def SignInForm():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        user = USER(fname, lname, email)
    return render_template('SIGNED_IN/index2.html', fname=user.fname, lname = user.lname, 
                           email = user.email)
    

@app.route('/2')
def SIHomePage():
    return render_template('SIGNED_IN/index2.html', fname = user.fname, lname = user.lname, email = user.email)

@app.route('/contact')
def SIContact():
    return render_template('SIGNED_IN/contact.html')

@app.route('/ordering2')
def SIOrdering():
    return render_template('SIGNED_IN/ordering2.html')


# Basic setup vvvvv
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80 ,debug = True)