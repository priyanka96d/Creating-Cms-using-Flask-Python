
from flask import Flask,render_template,request,url_for,redirect,session
import mysql.connector
import random
from flaskext.mysql import MySQL


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'purva123'
app.config['MYSQL_DATABASE_DB'] = 'ecommerce'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

mydb = mysql.connect()
mycur =mydb.cursor()

app.secret_key = "project-502"


@app.route('/')
@app.route("/login", methods =['POST','GET'])
def login():
   msg = ''
   if request.method == "POST":
      username = request.form['username']
      password = request.form['pwd']
      
      mycur.execute("""SELECT * FROM ecommerce.login_data Where username=%s 
      AND password=%s""",(username,password))
      record = mycur.fetchone()
      id_number = random.randrange(1000,4000)
      if record:
         session['loggedin'] = True
         session['username'] = record[1]
         session['id_number'] = id_number
         
         #adding category to the cms.html page
         mycur.execute('SELECT category FROM ecommerce.products;')
         records = [row[0] for row in mycur.fetchall()]
         category=[]

         for i in records:
            if i not in category:
               category.append(i)
               
         print("Under login",category)
         return render_template('cms.html',username=session['username'],category=category,id_number=session['id_number'])
      else:
         msg="Incorrect username/password. Try agian!"

   return render_template('login.html',msg=msg)  


#CMS page
@app.route("/cms" , methods = ["POST","GET"])
def cms():
   if request.method == "POST":
      if request.form["button"] == "cmsData":
         username = session['username']
         tab1 = request.form['tab1']
         tab2 = request.form['tab2']
         tab3 = request.form['tab3']

         path_tab1 = request.form['path1']
         path_tab2 = request.form['path2']
         path_tab3 = request.form['path3']

         logo = request.form['logo']
         logo_img = request.form['logo_img']

         banner = request.form['banner']

         cms_category = request.form['category']
         print("under cms",cms_category)

         #inserting data into userCms_data db

         mycur.execute( """INSERT INTO ecommerce.userCms_data
                  (id,username,tab1,tab2,tab3,path1,path2,path3,logo,logo_img,
                  selected_category,banner)
                  Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                  (session['id_number'],username,tab1,tab2,tab3,path_tab1,path_tab2,path_tab3,logo,logo_img,
                  cms_category,banner))

         mydb.commit()

         
         print(mycur.rowcount, " Row was inserted.")  
         mycur.execute('SELECT category FROM ecommerce.products;')
         records = [row[0] for row in mycur.fetchall()]
         category=[]

         for i in records:
            if i not in category:
               category.append(i)       
      
         return render_template('cms.html',username=session['username'],category=category,id_number=session['id_number'])  
          

      elif request.form["button"] == "addRecord":
         return render_template('addRecord.html')  

   if request.method == 'GET':
      return render_template('cms.html')      
            


@app.route('/addRecord',methods=['POST','GET'])
def addRecord():
   msg=''
   if request.method == "POST":
      if request.form["button"] == "addRecord":
         title = request.form['title']
         price = int(request.form['price'])
         category = request.form['category']
         description = request.form['description']
         image = request.form['image']
         """
         data = []

         data = mycur.execute('select category from ecommerce.products')
         print("data",data)

         for i in data:
            if i == add_category:
               category = i
         else:
            category = add_category
         """
         mycur.execute("""INSERT INTO ecommerce.products 
         (title,price,category,description,image) 
         VALUES (%s,%s,%s,%s,%s)""",(title,price,category,description,image))

         mydb.commit()

         print(mycur.rowcount, " Row was inserted.") 
         print(title,price,category)
         
         mycur.execute('SELECT category FROM ecommerce.products;')
         records = [row[0] for row in mycur.fetchall()]
         category=[]

         for i in records:
            if i not in category:
               category.append(i)
         print(category)
         return render_template('cms.html',category=category) 
      

   if request.method == 'GET':
      return render_template('addRecord.html')          

@app.route('/logout')
def logout():
   session.pop('loggedin',None)
   session.pop('username',None)
   return redirect(url_for('login'))



@app.route('/index')
def index():
   sql = "select * from ecommerce.userCms_data where id = %s;"
   mycur.execute(sql,session['id_number'])
   
   records = mycur.fetchall()
   tabs = []
   paths = []
   navbar = {}
   logo =''
   logo_url = ''
   banner = ''
   

   for  i  in records:
      tabs.extend((i[1], i[2], i[3]))
      paths.extend((i[4], i[5], i[6]))
      logo = i[7]
      logo_url = i[8]
      selected_category = i[9]
      banner = i[11]

   for data in range(len(tabs)) and range(len(paths)):   
      navbar[tabs[data]] = paths[data]
   
   #calling data category wise
   sql = "select * from ecommerce.products where category = %s;"
   mycur.execute(sql,selected_category)
   print("Under index",selected_category)

   #storing db value for category
   title = []
   price = []
   desc = []
   image = []

   records_category = mycur.fetchall()
   for i in records_category:
      title.append(i[1])
      price.append(i[2])
      desc.append(i[4])
      image.append(i[5])
   
   data = zip(image,price,title,desc)

   return render_template('index.html',navbar=navbar,logo=logo,logo_url=logo_url,data=data,banner=banner)    

@app.route('/dummy')
def dummy():

   sql = "select * from ecommerce.userCms_data where id = %s;"
   mycur.execute(sql,session['id_number'])
   
   records = mycur.fetchall()
   tabs = []
   paths = []
   navbar = {}
   logo =''
   logo_url = ''
   banner = ''
   

   for  i  in records:
      tabs.extend((i[1], i[2], i[3]))
      paths.extend((i[4], i[5], i[6]))
      logo = i[7]
      logo_url = i[8]
      selected_category = i[9]
      banner = i[11]

   for data in range(len(tabs)) and range(len(paths)):   
      navbar[tabs[data]] = paths[data]


   return render_template('dummy.html',navbar=navbar,logo=logo,logo_url=logo_url,banner=banner)


if __name__ == "__main__":
    app.run(debug=True)