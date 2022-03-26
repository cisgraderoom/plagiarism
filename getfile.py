import mysql.connector
import sys
import numpy as np
from decouple import config

def getfile(problem_id):
    if(problem_id != ''):
        mydb = mysql.connector.connect(
        host= config('MYSQL_CONTAINER'),
        user=config('MYSQL_ROOT_USERNAME'),
        password=config('MYSQL_ROOT_PASSWORD'),
        database=config('MYSQL_DATABASE')
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
            host= config('MYSQL_CONTAINER'),
            user=config('MYSQL_ROOT_USERNAME'),
            password=config('MYSQL_ROOT_PASSWORD'),
            database=config('MYSQL_DATABASE')
            )
            mycursor = mydb.cursor()
            values = ', '.join(map(str, myresult))
            sql_select_query = "INSERT INTO plagiarism (owner, compare, result, problem_id) VALUES {} ON DUPLICATE KEY UPDATE owner = VALUES(owner), compare = VALUES(compare), result = VALUES(result)".format(values)

            print(sql_select_query) #ไว้ดู
            mycursor.execute(sql_select_query)
            mydb.commit()
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
            return False
        else:
            sql = "UPDATE jobs SET status = %s WHERE id = %s;"
            value = (1,jobs_id)
            mycursor.execute(sql,value)
            mydb.commit()
    return True

if __name__ == '__main__':
    globals()[sys.argv[1]]()