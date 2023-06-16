from flask import Flask, render_template
import pymysql

# 创建Flask应用
app = Flask(__name__)

# 添加路由，用于返回HTML页面
@app.route('/index')
def index():
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
        print('无法连接数据库:', e)
        return '无法连接数据库，请检查配置'

    # 查询数据
    data = []
    if connection:
        try:
            cursor = connection.cursor()
            sql = "SELECT * FROM DOGBK"
            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
        except pymysql.Error as e:
            print('数据查询失败:', str(e))
        finally:
            cursor.close()
            connection.close()

    # 将查询结果传递给HTML页面进行展示
    return render_template('index.html', data=data)

# 运行Flask应用
if __name__ == '__main__':
    app.run()