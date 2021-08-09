from flask import Flask#导入Flask类,用于构建flask应用

app=Flask(__name__)#通过Flask类构建实例对象(flask应用),需要指定当前模块的模块名(__name__),可以把当前模块变成flask应用


# http://127.0.0.1:5000/
@app.route('/')#装饰器，用于定位视图函数的技术,也称路由(url到python函数的映射)
@app.route('/index')
def hello_world():#视图的内容以函数方式显示，也称视图函数
    str='hello world,你好涩会人～这是一个首页'
    return str

# http://127.0.0.1:5000/mil
@app.route('/mil')
def mil_view():
    return '这是军事相关的页面'

# http://127.0.0.1:5000/internet
@app.route('/internet')
def internet_view():
    return '这是互联网相关的页面'

# http://127.0.0.1:5000/show/参数
@app.route('/show/<name>')
def show_name_view(name):
    return 'hello %s'% name

# http://127.0.0.1:5000/show/参数/参数
@app.route('/show/<name>/<int:age>')
def show_view(name,age):
    return "%s is %s year's old" % (name,age)


app.run(debug=True)#通过flask应用的run方法,来启动flask服务程序