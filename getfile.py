# import requests
# import json
import mysql.connector
import os,sys
import numpy as np
# from deletecomment import deleteComment

# dir = 'checkPlagiarism'
# # delete old file
# def deletefile():
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))

# # getnew file
def getfile(problem_id):
    # problem_id = 2
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
        # myresult = mycursor.fetchall()
        myresult = np.array(mycursor.fetchall())
        # print(myresult[0][1])
        # for x in myresult:
        #     x = list(x)
        # deleteComment(myresult)
    return myresult

if __name__ == '__main__':
    globals()[sys.argv[1]]()

# import mysql.connector
# problem_id = 2
# if(problem_id != ''):
#     mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="cisgraderoom",
#     database="cisgraderoom"
#     )
#     mycursor = mydb.cursor()
#     sql_select_query = "SELECT a.username,a.problem_id,a.code,a.lang FROM submission a INNER JOIN ( SELECT username, MAX(created_at) created_at FROM submission WHERE problem_id = "
#     sql_select_query += str(problem_id) + " GROUP BY username) b ON a.username = b.username AND a.created_at = b.created_at"
#     data_tuple = 2
#     mycursor.execute(sql_select_query)

#     myresult = mycursor.fetchall()
#     for x in myresult:
#         print(x)