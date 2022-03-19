# import requests
# import json
import mysql.connector
import os,sys
 
dir = 'checkPlagiarism'
# delete old file
def deletefile():
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

# getnew file
def getfile(problem_id):
    mydb = mysql.connector.connect(
    host="http://sql.cisgraderoom.xyz",
    user="user",
    password="cis@sql",
    database="cisgraderoom"
    )
    mycursor = mydb.cursor()
    # sql_select_query = """SELECT username,code FROM submit WHERE problem_id = %s"""
    sql_select_query = """SELECT a.username, a.code FROM submitTable a INNER JOIN ( SELECT username, MAX(Date) Date FROM submitTable GROUP BY username ) b ON a.username = b.username AND a.Date = b.Date WHERE problem_id = %s"""
    data_tuple = (problem_id)
    mycursor.execute(sql_select_query, data_tuple)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    mydb.close()
    print('get file :',problem_id)

if __name__ == '__main__':
    globals()[sys.argv[1]]()