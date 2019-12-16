from app import app
#从app模块中导入创建的实例 （__init__.py中创建）
from flask import render_template
#导入渲染html模板
import mysql.connector

#数据库连接
config ={'host':'122.51.219.231',#默认127.0.0.1
        'user':'conuser',
        'password':'TXYMySQL@Connect2019',
        'port':3306 ,#默认即为3306
        'database':'g96-data',
        'charset':'utf8'#默认即为utf8
        }
try:
  cnn = mysql.connector.connect(**config)
  print('connet success')
except mysql.connector.Error as e:
  print('connect fails!{}'.format(e))#输出连接错误信息

@app.route('/')#建立路由
@app.route('/index') #通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法
def index():
    #将参数传递到index.html模板
    return render_template('index.html',title = '你好',user = {'username':'aa'})
@app.route('/test')
def test():
    
    return render_template('test.html')