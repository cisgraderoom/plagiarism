import mysql.connector
import sys
import numpy as np
def getfile(problem_id):
    if(problem_id != ''):
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="cisgraderoom",
        database="cisgraderoom"
        )
        mycursor = mydb.cursor()
        sql_select_query = "SELECT a.username,a.code,a.lang FROM submission a INNER JOIN ( SELECT username, MAX(created_at) created_at FROM submission WHERE problem_id = "
        sql_select_query += str(problem_id) + " GROUP BY username) b ON a.username = b.username AND a.created_at = b.created_at"
        mycursor.execute(sql_select_query)
        myresult = np.array(mycursor.fetchall())
    return myresult

def sendresult(myresult,jobs_id):
    if(myresult != ''):
        try:
            mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="cisgraderoom",
            database="cisgraderoom"
            )
            mycursor = mydb.cursor()
            sql_select_query = "INSERT INTO plagiarism (owner, compare, result, problem_id) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE owner = VALUES(owner), compare = VALUES(compare) , result = VALUES(result)"
            mycursor.executemany(sql_select_query,myresult)
            mydb.commit()
        except Exception as e:
            print(e)
        else:
            sql = "UPDATE jobs SET status = %s WHERE id = %s;"
            value = (1,jobs_id)
            mycursor.execute(sql,value)
            mydb.commit()
    return myresult

if __name__ == '__main__':
    globals()[sys.argv[1]]()