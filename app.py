from flask import Flask, render_template, request, url_for

app = Flask(__name__)
# Basic setup ^^^^

@app.route('/')
def HomePage():
    return render_template('NOT_SIGNED_IN/index.html')

# Basic setup vvvvv
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80 ,debug = True)