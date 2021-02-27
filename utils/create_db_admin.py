#!/usr/bin/env python3
import mariadb
import sys


try:
    username = sys.argv[1]
    password = sys.argv[2]
except:
    username = 'jeff'
    password = 'Diana1'


cnx = mariadb.connect(
        user='root', 
        password='Minnesota+1991',
        host='localhost',
      )
cursor = cnx.cursor()

query = ("CREATE USER IF NOT EXISTS '{}'@localhost IDENTIFIED BY '{}';".format(username, password))
cursor.execute(query)

query = ("GRANT ALL PRIVILEGES ON *.* TO '{}'@localhost;".format(username))
cursor.execute(query)

query = ("SELECT User FROM mysql.user;")
cursor.execute(query)

for (User) in cursor:
    print("User: {}".format(User[0]))


query = ("FLUSH PRIVILEGES;")
cursor.execute(query)

cnx.close()
