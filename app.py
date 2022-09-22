from flask import Flask,render_template, request,url_for
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
 
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Joseph'
# app.config['MYSQL_DB'] = 'flask'
db = SQLAlchemy(app)

    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Cart')
def Cart():
    return render_template('Cart.html')

if __name__ == "__main__":
    app.run(debug=False)
    app.run(host='localhost', port=5000)