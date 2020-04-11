from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') #indexroute - so that when we browse to URL no immediate 404
#next we need to define function for this route
def index():
    return render_template('index.html') #hier könnte auch einfach n string returned werden, aber wir beziehen uns auf unser index.html
#template inheritance - on master html (base.html) "skeleton of all others" and inherit it to others so they use it again and again

if __name__ == '__main__':
    app.run(debug=True) #debugTrue normalerweise nicht nur jetzt das wenn es errors gibt die gleich zu sehn sind
