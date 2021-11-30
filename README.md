# Creating Cms with Flask Python

Objective:- Creating a CMS using Python Flask so that user can change the website content without bothering the developer. 

Technologies used:
  Python 3.9,
  Flask,
  Mysql DB,
  HTML CSS
  
Folder description:
1) Templates: - In Flask all the html file should be stored in templates folder
2) Style:- Contain all CSS files
3) apicalling.py :  Calling online API and storing its data in different variables
4) mysql-db.py : Create a connection with Database and storing data from called api (from apiCalling.py)
5) app.py : This is a Main File use for routing and handling html-python communication 
  
Steps to start the project:
1) Run app.py file.
2) copy the url address and paste it to the browser.
3) First page is the "Login.html Page".
4) Because it is plateform for comapany employees they already have username and password. They could not create new login details. Login details are stored in mysql database. 
5) After succesful Login CMS page will display. In this page user can give following details:-
      i) Navigational tab name and its html url
      ii) Logo Title
      iii) Logo Image
      iv) Banner URL
      v) Choose a Category from dropdown (which category's data you want to display on main page [index.html])
      vi) AddRecord
6) There are two options present in Header of cms page.
      i) Main Page: To see what changes you made and what to display on Final User Inteface.
      ii) Logout
7) After Clicking AddRecord button new page will display. In this you can add new product details.     
