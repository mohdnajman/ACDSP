# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 18:06:31 2023

@author: evoma
"""

# Import the backage/module/library to handle postgress operations
import psycopg2
import psycopg2.extras

# Define and initialize all the important variables
conn = None # This variable for database connection
cur = None # Cursor -> It is a temporay data structure to handle rows/tuples fetched from a database table
hostname = 'localhost'
databasename = 'postgres'
username = 'postgres'
mypassword = 'postgres'
portnumber = 5432

drop_table_script = """ DROP TABLE IF EXISTS STUDENT_DS """

try:
    conn = psycopg2.connect(host=hostname,
                          dbname=databasename,
                          user=username,
                          password=mypassword,
                          port=portnumber)
    # cur = conn.cursor()
    # create_table_script = """CREATE TABLE IF NOT EXISTS STUDENT_DS
    # (stud_id CHAR(5),
    #  stud_name VARCHAR(40),
    #  stud_age INT,
    #  stud_gender CHAR(1));"""
    # cur.execute(create_table_script)
    # conn.commit()
    
    # insert_script = """INSERT INTO STUDENT_DS(stud_id,
    #                                           stud_name,
    #                                           stud_age,
    #                                           stud_gender) VALUES (%s, %s, %s, %s)"""
    
    # value_script = [('S0002','ZAILAN',21,'M'),
    #                 ('S0002','DHASON',53,'M'),
    #                 ('S0003','SHAKAR',20,'M'),
    #                 ('S0004','CHOW YEE MEI',20,'F')]
    # cur.executemany(insert_script, value_script)
    # conn.commit()
    
    cur.execute('SELECT * FROM STUDENT_DS;')
    for record in cur.fetchall():
        print(record)
        
except Exception as error:
    print('Connection to Postgres unsuccesfull')
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
