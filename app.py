from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def portfolio():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


#=== RUN APP ===#
HOSTNAME = 'localhost'
PORT = 5050
if __name__ == '__main__':
    app.run(debug=True, host=HOSTNAME,port=PORT)