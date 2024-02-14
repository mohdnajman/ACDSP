"""

Name of developer: Mr.Dhason Padmakumar
Name of program:python_and_postgres.py
Description:	
    
3.	Install the DBMS – Postgres. - Done
4.	Write a program in Python to create a database table. - Done
5.	Write a program in Python to insert tuple(s) into the database table. - Done
6.	Write a program in Python to retrieve/fetch/select data from the database table. - Done
7.	Write a program in Python to edit/update data in the database table.
8.	Write a program in Python to delete tuple from the database table.
9.	Write a program in Python to drop (permanently delete) the database table. - Done

                
Date first written:Thu,13-Jul-2023
Date last updated: Fri,15-Jun-2023  

"""

"""

DBMS - Database Management System - A complex system s/w to manage data stored in databases
DBASE 3+
FOXPRO
CLIPPER
-----
MYSQL - 45.68%
MS SQL SERVER - 26.7%
ORACLE - The most robust and expensive - 11.75%
SQLite - Smallest - 30.83%
MS ACCESS - Less number of users are using it
DB2
INGRESS
SYBASE
POSTGRES -  46.48%

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

try:
    conn = psycopg2.connect(host=hostname,
                          dbname=databasename,
                          user=username,
                          password=mypassword,
                          port=portnumber)
    cur = conn.cursor()
    
    #cur = conn.cursor(cursor_factory=psycopg2.extras.Dictionary)
    
    # Drop/Permanently delete the table if the STUDENT_T exists
    cur.execute('DROP TABLE IF EXISTS STUDENT_T')
    
    # Create the table STUDENT_T    
    create_table_script = """CREATE TABLE IF NOT EXISTS STUDENT_T 
    (stud_id CHAR(5),
     stud_name VARCHAR(40),
     stud_age CHAR(2),
     stud_gender CHAR(1));"""
    cur.execute(create_table_script)
    conn.commit() # Each transaction (Writing, Deletion) must be commiitted 
    
    # Insert tuples/rows to the table  STUDENT_T
    # insert_script = """INSERT INTO STUDENT_T(stud_id,
    # stud_name,
    # stud_age,
    # stud_gender) VALUES (%s,%s,%s,%s)"""
    # value_script = [('S0002','ZAILAN','21','M'),
    #                 ('S0002','DHASON','53','M'),
    #                 ('S0003','SHAKAR','20','M'),
    #                 ('S0004','CHOW YEE MEI','20','F')]
    # cur.execute(insert_script,value_script)
    # conn.commit()
    
    insert_script = """INSERT INTO STUDENT_T(stud_id,
    stud_name,
    stud_age,
    stud_gender) VALUES 
                    ('S0002','ZAILAN','21','M'),
                    ('S0002','DHASON','53','M'),
                    ('S0003','SHAKAR','20','M'),
                    ('S0004','CHOW YEE MEI','20','F');"""
    cur.execute(insert_script)
    conn.commit()
    
    # Retrieve/Select/fetch data from the table - STUDENT_T - This is to read multiple tuples
    cur.execute('SELECT * FROM STUDENT_T;')
    for record in cur.fetchall():
        print(record)
        
     # Retrieve/Select/fetch data from the table - STUDENT_T - This is to read only one tuple
    cur.execute("""SELECT * FROM STUDENT_T WHERE stud_name = 'ZAILAN';""")
    print(cur.fetchone())   
    
except Exception as error:
    print(error)
finally:
  if cur is not None:
      cur.close()
  if conn is not None:
      conn.close()
       