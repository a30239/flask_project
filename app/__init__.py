from flask import Flask


#创建app实例,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__) #第一个参数为应用模块或包的名称

from app import routes