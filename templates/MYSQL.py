#1.配置数据库连接信息并且连接数据库
#2.判断是否成功连接数据库
#3.根据关键字进行查询出信息
#4.输出查询结果
#5.退出程序



import pymysql
# 配置数据库连接信息
try:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='751020',
                                 database='DOGBK',
                                 port=3306,
                                 cursorclass=pymysql.cursors.DictCursor)
    print('连接成功')
except Exception as e:
    print('无法连接数据库，请检查连接配置。')
    exit()

# 根据关键字查询出信息


while True:
    keywords = input("请输入要查询信息的名称：")
#判断是否有输入没有就继续
    if not keywords:
        continue
#有输入时根据数据表中的name和alias字段进行查询
    
    with connection.cursor() as cursor:  #返回一个游标对象
        sql = "SELECT * FROM DOGBK WHERE name LIKE %s OR alias LIKE %s" #一个sql语句
        cursor.execute(sql, ("%" + keywords + "%", "%" + keywords + "%")) #将keywords传递给sql语句替换%s
        results = cursor.fetchall() 
          
    if len(results) == 0:
        print('没有查询到匹配的结果。')
    else:
        print(results)

    user_input = input("是否继续查询？（输入 q 或 quit 退出查询）")
    if user_input.lower() in ('q', 'quit'):
        break
    
# 关闭数据库连接
connection.close()


        
