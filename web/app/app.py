from flask import Flask,render_template
import pymysql
from flask_mysqldb import MySQL

app=Flask(__name__)

# app.config['MYSQL_HOST']='bgnobpenpyjuevrh0fpe-mysql.services.clever-cloud.com'
# app.config['MYSQL_USER']='u2enmuofuxxuyrkq'
# app.config['MYSQL_PASSWORD']='1rZVoL6BvM04OSZ7VfIH'
# app.config['MYSQL_DB']='bgnobpenpyjuevrh0fpe'

# mysql=MySQL(app)


@app.route("/funds")
def funds():
    # cur=mysql.connection.cursor()
        
    # q="select * from returns;"
    # cur=mysql.connection.cursor()
    # cur.execute(q)
    # rz=cur.fetchone()
    # cur.close()
    # s=[]
    # q=""
    # print(rz)
    # for i in rz:
    #     s.append(str(i))
    #     q+=str(i)
    # print(s)
    print("habhai isme")
    s=["1","2","3","4"]
    return {
        "Name":s[0], 
        "Age":s[1],
        "Date":s[2], 
        "programming":s[3]
        }
    
if __name__=="__main__":
    app.run(debug=True)