from app import app
#从app模块中导入创建的实例 （__init__.py中创建）
from flask import render_template
#导入渲染html模板

@app.route('/')#建立路由
@app.route('/index') #通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法
def index():
    #将参数传递到index.html模板
    return render_template('index.html',title = '你好',user = {'username':'aa'})
