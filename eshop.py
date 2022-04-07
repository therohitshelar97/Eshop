from flask import *
import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'eshop'
    )

cursor = db.cursor()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/mens")
def mens():
    return render_template('mens.html')

@app.route("/office_wear")
def office_wear():
    return render_template('office_wear.html')

@app.route("/order1")
def order1():
    return render_template('order1.html')

@app.route("/order12")
def order12():
    cursor.execute("select * from bhai")
    data = cursor.fetchall()
    return render_template('order12.html',userdata=data)

@app.route("/make",methods=["POST"])
def make():
    uname=request.form.get('uname')
    addr=request.form.get('addr')
    contact=request.form.get('contact')
    contact1=request.form.get('contact1')
    q = "insert into bhai(Name,Address,Contact,Contact1) values('{}','{}','{}','{}')".format(uname,addr,contact,contact1)
    try:
        cursor.execute(q)
        db.commit()
        return redirect(url_for('order12'))
    except:
        db.rollback()
        return "Error"
    
@app.route("/cotton_white")
def cotton_white():
    return render_template('cotton_white.html')

@app.route("/gadget")
def gadget():
    return render_template('gadget.html')

@app.route("/womens")
def womens():
    return render_template('womens.html')

@app.route("/skyblue_saree")
def skyblue_saree():
    return render_template('skyblue_saree.html')

@app.route("/kids")
def kids():
    return render_template('kids.html')

@app.route("/fashion")
def fashion():
    return render_template('fashion.html')

if __name__=='__main__':
    app.run(debug=True)