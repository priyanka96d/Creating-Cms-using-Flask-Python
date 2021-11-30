list1=['men','women','men','women']
new_list=[]

for i in list1:
   if i not in new_list:
      new_list.append(i)

print(new_list)      



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

         cms_category = request.form['category']

         #inserting data into userCms_data db

         mycur.execute( """INSERT INTO ecommerce.userCms_data
                  (username,tab1,tab2,tab3,path1,path2,path3,logo,logo_img,
                  selected_category)
                  Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                  (username,tab1,tab2,tab3,path_tab1,path_tab2,path_tab3,logo,logo_img,
                  cms_category))

         mydb.commit()

         print(mycur.rowcount, " Row was inserted.")  
         mycur.execute('SELECT category FROM ecommerce.products;')
         records = [row[0] for row in mycur.fetchall()]
         category=[]

         for i in records:
            if i not in category:
               category.append(i)       
      
         return render_template('cms.html',username=session['username'],category=category)  
          

      elif request.form["button"] == "addRecord":
         return render_template('addRecord.html')  

   if request.method == 'GET':
      return render_template('cms.html') 