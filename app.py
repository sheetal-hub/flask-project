from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/admission')
def admission():
    return render_template('admission.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)

