from flask import Flask,render_template, request, url_for, redirect, session,jsonify
import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=./DigiCertGlobalRootCA.crt;UID=npc86194;PWD=AoGdx5iKBqIQ23Eu",'','')

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/home",methods=['GET','POST'])
def home():
    return render_template('home.html',username=session['username'])

@app.route("/dashboard",methods=['POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route("/register",methods=['POST'])
def register():
    return render_template('register.html')

@app.route("/login",methods=['POST'])
def login():
    return render_template('login.html')

@app.route("/about",methods=['POST'])
def about():
    return render_template('about.html')

@app.route('/validate_login', methods =['GET', 'POST'])
def validate_login():
    msg=''
    if request.method == 'POST':

        username = request.form['email']
        password = request.form['pwd']

        statement = ibm_db.prepare(conn,'SELECT * FROM Users WHERE email = %s AND password = %s', (username, password, ))
        ibm_db.execute(statement)
        account = ibm_db.fetch_assoc(statement)

        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return render_template('home.html')
        else:
            return render_template('index.html', msg = 'error')
    
@app.route("/validate_register",methods=['GET','POSt'])
def validate_register():
    msg = ''
    if request.method == 'POST':
        
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['pwd'] 
        phone = request.form['phone']
        cname = request.form['cname']
        address = request.form['address']
        print('Before storing')
        sql = "SELECT * FROM USERS WHERE email =?  AND cname=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,cname)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print('stored')
        if account:
            msg = 'exists'
        else:
            sql = 'INSERT INTO USERS VALUES (?,?,?,?,?,?,?)'
            insert_statement = ibm_db.prepare(conn,sql)
            ibm_db.bind_param(insert_statement,1,fname)
            ibm_db.bind_param(insert_statement,2,lname)
            ibm_db.bind_param(insert_statement,3,email)
            ibm_db.bind_param(insert_statement,4,password)
            ibm_db.bind_param(insert_statement,5,phone)
            ibm_db.bind_param(insert_statement,6,cname)
            ibm_db.bind_param(insert_statement,7,address)
            ibm_db.execute(insert_statement)
            msg = 'success'
    else:
        msg="error"
    
    return render_template('register.html',msg=msg)

@app.route("/profile",methods=['POST'])
def profile():
    if request.method == 'POST':
        
        statement = ibm_db.prepare(conn,'SELECT * FROM users WHERE username = %s', (session['username']))
        ibm_db.execute(statement)
        values = ibm_db.fetch_assoc(statement)
        data={
            'fname' : values['fname'],
            'lname' : values['lname'],
            'email' : values['email'],
            'phone' : values['phone'],
            'cname' : values['cname'],
            'address':values['address']
        }
    return render_template('profile.html',data=data)

@app.route('/users')
def users():
    if request.method == 'POST':
        
        statement = ibm_db.prepare(conn,'SELECT * FROM users')
        ibm_db.execute(statement)
        users = ibm_db.fetch_assoc(statement)

    return render_template('users.html',users=users)

@app.route('/items')
def items():  
    if request.method == 'POST':
        
        statement = ibm_db.prepare(conn,'SELECT * FROM items')
        ibm_db.execute(statement)
        items = ibm_db.fetch_assoc(statement)

    return render_template('items.html',items=items)

@app.route('/add_item')
def add_item():
    return render_template('add_items.html')

@app.route('/display_item',methods=['POST'])
def display_item():
    if request.method == 'POST':

        statement = ibm_db.prepare(conn,'SELECT * FROM items where product_id=%s',request.values)
        ibm_db.execute(statement)
        values = ibm_db.fetch_assoc(statement)
        data={
            'pid' : values['product_id'],
            'pname' : values['product_name'],
            'category' : values['category'],
            'mdate' : values['manf_date'],
            'edate' : values['exp_date'],
            'price':values['price'],
            'quantity':values['quantity'],
            'desc':values['description']
        }
        return render_template('/display_item.html',data=data)

@app.route('/validate_item',methods=['POST'])
def validate_item():
    if request.method == 'POST':

        pid = request.form['pid']
        pname = request.form['pname']
        category = request.form['category']
        mdate = request.form['mdate']
        edate = request.form['edate']
        price = request.form['price']
        quantity = request.form['qty']
        desc = request.form['desc']

        statement = ibm_db.prepare(conn,'INSERT into items VALUES(%s, %s, %s, %s, %s, %s, %s, %s)',(pid,pname,category,mdate,edate,price,quantity,desc))
        ibm_db.execute(statement)

    return redirect('/items')

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__=="_main_":
    app.run(debug=True)