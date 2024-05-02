from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def portfolio():
    return render_template('home.html')



#=== RUN APP ===#
HOSTNAME = 'localhost'
PORT = 5050
if __name__ == '__main__':
    app.run(debug=True, host=HOSTNAME,port=PORT)