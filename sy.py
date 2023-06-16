#1.配置数据库连接信息并且连接数据库
#2.判断是否成功连接数据库
#3.实现查询信息的接口
#4.获取查询关键字
#5.判断是否有输入
#6.根据关键字进行查询出信息
#7.判断查询结果是否存在
#8.输出查询结果
#9.让结果变成超链接，点击打开新的网页


from flask import Flask, jsonify, request,render_template
import pymysql
import json

app = Flask(__name__)

# 配置数据库连接信息
try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='751020',
        database='DOGBK',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('连接成功')
except Exception as e:
    print('无法连接数据库，请检查连接配置。')
    exit()

@app.route('/')
def index():
    # return url_for('static', filename='base.html')
 return render_template('base.html')

# @app.route('/dog1.html')
# def dog1():
#     # return url_for('static', filename='base.html')
#  return render_template('dog1.html')
# 实现查询信息的接口
@app.route('/search', methods=['GET'])
def search():
    # 获取查询关键字
    keywords = request.args.get('keywords')

    # 判断是否有输入
    if not keywords:
         return render_template('base.html', keywords=keywords, results=[])

    # 根据关键字查询数据库
    with connection.cursor() as cursor:
        sql = "SELECT * FROM DOGBK WHERE name LIKE %s OR alias LIKE %s"
        cursor.execute(sql, ("%" + keywords + "%", "%" + keywords + "%"))
        results = cursor.fetchall()

    # 判断查询结果是否存在
    if not results:
        return jsonify("Sorry, this keyword is not available in the database")

    # 构造响应数据
    response_data = json.dumps(results, ensure_ascii=False)
    response = app.response_class(response=response_data, mimetype='application/json;charset=utf-8')

    # 返回查询结果
    return render_template('index.html', keywords=keywords, results=results)

@app.route('/detail')
def detail():
    id = request.args.get('id')

    with connection.cursor() as cursor:
        sql = "SELECT * FROM DOGBK WHERE id = %s"
        cursor.execute(sql, id)
        result = cursor.fetchone()

    if not result:
        return "Sorry, this data is not available in the database"
    return render_template('detail.html', result=result)
if __name__ == '__main__':
    app.run()