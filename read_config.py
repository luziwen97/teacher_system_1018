

import os
import configparser
import pymysql
import sqlalchemy
import pandas as pd



def get_config_info():
    #读取congfig文件关于数据库的连接设置
    conf = configparser.ConfigParser()  # 类的实例化
    curpath = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(curpath, 'config.ini')
    conf.read(path, encoding="utf-8")
    selection = conf.sections()
    print(selection)
    host = str(conf.get(selection[0], "host"))
    port = int(conf.get(selection[0], "port"))
    user = str(conf.get(selection[0], "user"))
    password = str(conf.get(selection[0], "password"))
    database = str(conf.get(selection[0], "database"))
    charset = str(conf.get(selection[0], "charset"))
    return host,port,user,password,database,charset
host, port, user, password, database, charset= get_config_info()
def con():
    #连接数据库
    host, port, user, password, database, charset=get_config_info()
    connect = pymysql.connect(
        host=host,  # 默认用主机名
        port=port,
        user=user,  # 默认用户名
        password=password,  # mysql密码
        database=database,  # 库名
        charset=charset  # 编码方式
    )
    print("数据库连接成功！")
    return connect

def get_table_names():
    #获取数据库中所有表格名称
    #返回参数为列表，元素为字符串
    print('获取所有表名字')
    consor=con().cursor()
    print("表格名获取中")
    table_names=[]
    sql_1 = "select table_name from information_schema.tables where table_schema="+"'"+str(database)+"'"+" and table_type = 'BASE TABLE' AND table_schema = DATABASE ()";
    print(sql_1)
    consor.execute(sql_1)
    result = consor.fetchall()
    for i in result:
        table_names.append(str(i[0]))
    return table_names

def get_columns_names(text):
    #获取对应表中的所有列名
    consor = con().cursor()
    columns_names = []
    sql_2 ="select COLUMN_NAME from INFORMATION_SCHEMA.Columns where table_name=" + "'" + text + "'" + ";"
    consor.execute(sql_2)
    result = consor.fetchall()
    for i in result:
        columns_names.append(str(i[0]))
    return columns_names
def create_table(df,df_name):
    #传入df表然后设定表名在数据库中创建数据表
    try:
        sql_11="mysql+pymysql://"+str(user)+":"+str(password)+"@"+str(host)+"/"+str(database)+"?charset="+str(charset)
        print(sql_11)
        yconnect = sqlalchemy.create_engine(sql_11)
        #yconnect  = sqlalchemy.create_engine('mysql+pymysql://root:12345678@localhost/teacher_db?charset=utf8')
        df.to_sql(str(df_name),yconnect,index=False,if_exists='replace')
    except Exception as reason:
        print(reason)

def get_table(table_name):
    #根据数据表名获取df表
    sql_4 = "SELECT * FROM " + str(table_name) + ";"
    sql_11 = "mysql+pymysql://" + str(user) + ":" + str(password) + "@" + str(host) + "/" + str(
        database) + "?charset=" + str(charset)
    print(sql_11)
    yconnect = sqlalchemy.create_engine(sql_11)
    #yconnect = sqlalchemy.create_engine('mysql+pymysql://root:12345678@localhost/teacher_db?charset=utf8')
    df = pd.read_sql(str(sql_4), con=yconnect)
    return df

def add_value(table_name,column_name,value):
    #根据表名，列名，以及值，添加元素
    consor=con().cursor()
    sql_8= "INSERT INTO "+table_name+" ("+column_name+") "+"VALUES"+"("+"'"+value+"'"+")"+";"
    print(sql_8)
    try:
        consor.execute(sql_8)
        consor.connection.commit()
        print("end")
    except Exception as reason:
        print(reason)
def add_values(table_name,column1_name,value1,column2_name,value2):
    #根据表名，列名，以及值，添加元素
    consor=con().cursor()
    sql_8= "INSERT INTO "+table_name+" ("+column1_name+','+column2_name+") "+"VALUES"+"("+"'"+str(value1)+"'"+','+"'"+str(value2)+"'"+")"+";"
    print(sql_8)
    try:
        consor.execute(sql_8)
        consor.connection.commit()
        print("end")
    except Exception as reason:
        print(reason)

def update(table_name,column_name,key_name,key,value):
    #根据表名，列名，键值，键名，值，更新键列对应的值
    consor = con().cursor()
    sql_9="UPDATE "+str(table_name)+ " SET "+str(column_name)+" = "+"'"+str(value)+"'"+ " WHERE "+str(key_name)+" = "+"'"+str(key)+"'"+";"
    print(sql_9)
    consor.execute(sql_9)
    consor.connection.commit()
def update2(table_name,column_name,key1_name,key1,key2_name,key2,value):
    #根据表名，列名，键值，键名，值，更新键列对应的值
    consor = con().cursor()
    sql_9="UPDATE "+str(table_name)+ " SET "+str(column_name)+" = "+"'"+str(value)+"'"+ " WHERE "+str(key1_name)+" = "+"'"+str(key1)+"'"+' and '+str(key2_name)+" = "+"'"+str(key2)+"'"+";"
    print(sql_9)
    consor.execute(sql_9)
    consor.connection.commit()
def check(table_name,column_name,key_name,key):
    #根据表名，键名，列名，及键值查询对应的值
    consor = con().cursor()
    sql_10="SELECT "+str(column_name)+" FROM "+str(table_name) +" WHERE "+str(key_name)+" = "+str(key)+";"
    print(sql_10)
    consor.execute(sql_10)
    consor.fetchall()
    return consor.fetchall()

def add_column(table_name,column_name,type_):
    #根据表名，列名，格式，添加对应列
    consor = con().cursor()
    sql_7="ALTER TABLE "+ table_name+" ADD " +column_name+" "+type_+";"
    print(sql_7)
    consor.execute(sql_7)

def get_cow(table_name,column_name):
    #根据表名，列名，获取列中所有值
    #根据列名和表名获取列的所有记录值
    sql_6="select "+str(column_name)+" FROM "+str(table_name)+";"
    sql_11 = "mysql+pymysql://" + str(user) + ":" + str(password) + "@" + str(host) + "/" + str(
        database) + "?charset=" + str(charset)
    print(sql_11)
    yconnect = sqlalchemy.create_engine(sql_11)
    #yconnect = sqlalchemy.create_engine('mysql+pymysql://root:12345678@localhost/teacher_db?charset=utf8')
    df = pd.read_sql(str(sql_6), con=yconnect)
    cow_values=df[column_name].to_list()
    return cow_values
def get_id(table_name,value):
    consor = con().cursor()
    sql_10="SELECT `教师ID` FROM " +str(table_name)+" WHERE 姓名="+"'"+str(value)+"'"+";"
    print(sql_10)
    consor.execute(sql_10)
    result = consor.fetchall()
    print(result[0][0])
    return result[0][0]
"===========================================下面是功能======================"






if __name__ == '__main__':
    #print(get_table_names())
    #print(get_cow("教师","教师ID"))
    print(get_id("教师","张三"))