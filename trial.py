import mysql.connector as t
mydb = t.connect(host = "localhost",user = "root",passwd = "Bhupendra.2004")
mycur = mydb.cursor()
mycur.execute('show databases')
for i in mycur:
    print(i)