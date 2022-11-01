# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:00:13 2022

@author: 劉佳怡
"""

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

dbconfig = { 
    "host":"localhost",
    "port":3307,
    "database":"website",
    "user":"root",
    "password":""}

connection_pool = pooling.MySQLConnectionPool(pool_name = "test_pool",
    pool_size = 3,
    pool_reset_session = True,
    **dbconfig
    )



def filt (input_username):
    try:
        connection_object = connection_pool.get_connection()
        cursor = connection_object.cursor()
        sql = "SELECT * FROM member WHERE username= %s "
        sql_value = (input_username,)
        cursor.execute(sql,sql_value) 
        myresult = cursor.fetchone()
    except:
        print("Unexpected Error")
    finally:
        cursor.close()
        connection_object.close()    
    return myresult


def add(input_name,input_username,input_password):
    try:
        connection_object = connection_pool.get_connection()
        cursor = connection_object.cursor()
        sql = "INSERT INTO member (name,username,password) VALUES(%s,%s,%s)"
        sql_value = (input_name,input_username,input_password)
        cursor.execute(sql,sql_value)
        connection_object.commit()
    except:
        print("Unexpected Error")
    finally:
        cursor.close()
        connection_object.close()


def confirm(input_username,input_password):
    try:
        connection_object = connection_pool.get_connection()
        cursor = connection_object.cursor()
        sql = "SELECT * FROM member WHERE username=%s "
        sql_value = (input_username,)
        cursor.execute(sql,sql_value)
        myresult = cursor.fetchone()
    except:
        print("Unexpected Error")
    finally:
        cursor.close()
        connection_object.close()
    
    if myresult != None:
        if myresult[2] == input_username and myresult[3] == input_password:
            return "correct"
        else:
            return "wrong"
    else: 
        return "wrong"
    
def message_content():
    try:
        connection_object = connection_pool.get_connection()
        cursor = connection_object.cursor()
        sql = "SELECT member.name,message.content,message.time FROM member INNER JOIN message ON member.id = message.member_id  ORDER BY message.time DESC " 
        cursor.execute(sql)
        myresult = cursor.fetchall()
    except:
        print("Unexpected Error")
    finally:
        cursor.close()
        connection_object.close()
    return myresult

def message_send(id,content):
    try:
        connection_object = connection_pool.get_connection()
        cursor = connection_object.cursor()
        sql = "INSERT INTO message(member_id,content) VALUES(%s,%s)"
        sql_value = (id,content)
        cursor.execute(sql,sql_value)
        connection_object.commit()
    except:
        print("Unexpected Error")
    finally: 
        cursor.close()
        connection_object.close()

    
def api_member(username):
    try:
        connection_object=connection_pool.get_connection()
        cursor = connection_object.cursor()
        sql = "SELECT id,name,username FROM member WHERE username = %s"
        sql_value = (username,)
        cursor.execute(sql,sql_value)
        myresult = cursor.fetchone()
    except:
        print("Unexpected Error")
    finally:
        cursor.close()
        connection_object.close()
    return myresult


def api_update(newname,id):
    try:
        connection_object=connection_pool.get_connection()
        cursor = connection_object.cursor()
        sql = "UPDATE member SET name = %s WHERE id = %s"
        sql_value = (newname,id)
        cursor.execute(sql,sql_value) 
        connection_object.commit()
    except:
        print("Unexpected Error")
    finally:
        cursor.close()
        connection_object.close()
    return "ok"
        
    
 


        

        

    





    
    

   


