''':var
该文件用于一些初始化文件设置，第一此运行时会保存到数据库种新建表格进行储存，或者文件形式进行保存
'''


import os
import configparser
conf = configparser.ConfigParser() # 类的实例化
def get_path():
    curpath = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(curpath, 'setting.ini')
    return path
def get_sections():
    #获取所有selections
    path=get_path()
    conf.read(path, encoding="utf-8")
    selections = conf.sections()
    return selections

def get_con(n):
    path = get_path()
    conf.read(path, encoding="utf-8")
    key_name = conf.get(n, "key_name")  # 读取一个section中的所有数据，返回一个列表
    name_a = conf.get(n, "name_a")  # 读取一个section中的所有数据，返回一个列表
    name_b = conf.get(n, "name_b")  # 读取一个section中的所有数据，返回一个列表
    return key_name,name_a,name_b

def read_setting_info():
    #查看键值对信息逻辑
    path = get_path()
    conf.read(path,encoding="utf-8")
    list_key_value = []
    section_list=conf.sections()
    section_list=section_list[1:]
    #section_list.remove("login")
    for i in section_list:
        n=i
        key_name = conf.get(n,"key_name") # 读取一个section中的所有数据，返回一个列表
        df_a = conf.get(n,"name_a")  # 读取一个section中的所有数据，返回一个列表
        df_b = conf.get(n,"name_b")  # 读取一个section中的所有数据，返回一个列表
        list_df=[df_a,df_b]
        list_key_value.append({key_name:list_df})
    print(list_key_value)
    return list_key_value

def read_setting_for_father_gui():
    #为merge提供键值对匹配逻辑
    path = get_path()
    conf.read(path, encoding="utf-8")
    section_list=conf.sections()
    section_list=section_list[1:]
    #section_list.remove("login")
    dict_key_value={}
    for i in section_list:
        n = i
        key_name = conf.get(n, "key_name")  # 读取一个section中的所有数据，返回一个列表
        df_a = conf.get(n, "name_a")  # 读取一个section中的所有数据，返回一个列表
        df_b = conf.get(n, "name_b")  # 读取一个section中的所有数据，返回一个列表
        list_df = [df_a, df_b]
        dict_key_value[key_name]=list_df
    return dict_key_value

def write_setting(key,table_a,table_b):
    #添加键值对的方法逻辑
    path = get_path()
    conf.read(path, encoding="utf-8")
    section_list=conf.sections()
    conf.set('login', 'number', str(len(section_list)))
    new_section=str(key)
    conf.add_section(new_section)
    conf.set(new_section, 'key_name', str(key))
    conf.set(new_section, 'name_a', str(table_a))
    conf.set(new_section, 'name_b', str(table_b))
    conf.write(open(path,'r+',encoding="utf-8"))  # 保存数据

def change_setting(section,key,table_a,table_b):
    #键值对修改方法逻辑
    path=get_path()
    conf.remove_section(section)
    new_section=str(key)
    conf.add_section(new_section)
    conf.set(new_section, 'key_name', str(key))
    conf.set(new_section, 'name_a', str(table_a))
    conf.set(new_section, 'name_b', str(table_b))
    conf.write(open(path, 'w', encoding="utf-8"))  # 保存数据

def remove_section(section):
    #删除selection
    path=get_path()
    conf.read(path, encoding="utf-8")
    value = conf.get('login', 'number')
    num = int(value)
    print(num)
    number = num - 1
    print(number)
    conf.set('login', 'number', str(number))
    conf.remove_section(section)
    print(conf.sections())
    conf.write(open(path, 'w', encoding="utf-8"))
