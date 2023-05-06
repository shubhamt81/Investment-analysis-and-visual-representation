from flask import Flask,render_template
from flask_mysqldb import MySQL
from flask_cors import CORS

app=Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
app.config['MYSQL_HOST']='bgnobpenpyjuevrh0fpe-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']='u2enmuofuxxuyrkq'
app.config['MYSQL_PASSWORD']='1rZVoL6BvM04OSZ7VfIH'
app.config['MYSQL_DB']='bgnobpenpyjuevrh0fpe'

mysql=MySQL(app)

@app.route("/funds")
def funds():
    cur=mysql.connection.cursor()
        
    q="select * from returns;"
    cur=mysql.connection.cursor()
    cur.execute(q)
    rz=cur.fetchone()
    cur.close()
    s=[]
    q=""
    print(rz)
    for i in rz:
        s.append(str(i))
        q+=str(i)
    print(s)
    return {"Company_name":s[0],"name_of_plan":s[1],"cap_size":s[2],"type_of_investment":s[3],"ROI":s[4],"risk":s[5],"min_investment":s[6],"ROI_1M":s[7],"ROI_3M":s[8],"ROI_6M":s[9],"ROI_1Y":s[10],"ROI_3Y":s[11],"ROI_5Y":s[12],"ROI_10Y":s[13],"cat":s[14],"sub_cat":s[15],"vro_rating":s[16],"lumpsum_min":s[17],"sip_min":s[18],"aum":s[19],"nav":s[20],"CAT_AVG_10Y":s[21],"CAT_AVG_5Y":s[22],"CAT_AVG_3Y":s[23],"CAT_AVG_1Y":s[24],"CAT_AVG_6M":s[25],"CAT_AVG_3M":s[26],"CAT_AVG_1M":s[27]}
    
    
if __name__=="__main__":
    app.run(debug=True)