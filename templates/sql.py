import pymysql
 
try: 
# 打开数据库连接
    db = pymysql.connect(host='localhost',
                    user='root',
                    password='751020',
                    database='DOGBK',)
 
# 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    
    print('数据库连接成功')
except pymysql.Error as e:
    print('数据库连接失败:', str(e))

if db:
    # 查询数据表
    try:
        
        sql = "SELECT * FROM DOGBK"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except pymysql.Error as e:
        print('数据查询失败:', str(e))
    finally:
        cursor.close()
        db.close()