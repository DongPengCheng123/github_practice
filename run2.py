from flask import Flask,request,url_for

app=Flask(__name__)

# http://127.0.0.1:5000/ 相同地址的不同请求，处理方法不一样
@app.route('/',methods=['POST','GET'])#通过methods参数来指定当前地址允许接收的数据类型
def index_view():
    print(request.method)#所有和请求有关的内容，都会保存在request的对象中（是flask提供的）
    if request.method=='GET':
        return '<form method="POST" action="/">'\
            '<input type="submit">'\
            '</form>'
    elif request.method=='POST':
        return '<h1>POST请求的数据提交成功</h1>'
    
@app.route('/user/<uname>')
def uname_view(uname):
    return '%s有关的信息' % uname

# 想获取某个数据对应的地址，可以用反向解析方式
@app.route('/urlFor')
def url_view():
    return '反向解析qtx有关信息的地址是 %s' % url_for('uname_view',uname='qtx')

app.run(debug=True)