from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# globally stored user input(From sign_in page)
class USER:
    def __init__ (self, fname = None, lname = "Re", email = None, address = None):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.address = address
user = USER()

# >>>NOT_SIGNED_IN pages:
@app.route('/complain')
def Complain():
    return render_template('NOT_SIGNED_IN/complain.html')
@app.route('/shop')
def Shop():
    return render_template('NOT_SIGNED_IN/index.html')
@app.route('/')
def HomePage():
    return render_template('NOT_SIGNED_IN/info.html')
@app.route('/ordering1')
def Ordering():
    return render_template('NOT_SIGNED_IN/ordering1.html')
@app.route('/sign_up')
def SignUp():
    return render_template('NOT_SIGNED_IN/sign_up.html',url=url_for('SignInForm'))

    # FORM FILLOUT vvvv
@app.route('/SIGNED_IN/index2', methods=['GET', 'POST'])
def SignInForm():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        address = request.form['address']
        global user
        user = USER(fname, lname, email, address)
    return render_template('SIGNED_IN/index2.html', fname=user.fname, lname = user.lname, 
                           email = user.email, address=user.address)

# >>>SIGNED_IN pages(Same order in templates folder):
@app.route('/contact')
def SIContact():
    return render_template('SIGNED_IN/contact.html', fname=user.fname, lname = user.lname, 
                           email = user.email, address=user.address)
@app.route('/shop2')
def SIShop():
    return render_template('SIGNED_IN/index2.html', fname = user.fname, lname = user.lname, 
                           email = user.email, address=user.address)
@app.route('/2')
def SIHomePage():
    return render_template('SIGNED_IN/info2.html', fname=user.fname, lname = user.lname, 
                           email = user.email, address=user.address)
@app.route('/ordering2')
def SIOrdering():
    return render_template('SIGNED_IN/ordering2.html', fname=user.fname, lname = user.lname, 
                           email = user.email, address=user.address)
@app.route('/profile')
def SIProfile():
    return render_template('SIGNED_IN/profile.html', fname=user.fname, lname = user.lname, 
                           email = user.email, address=user.address)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80 ,debug = True)