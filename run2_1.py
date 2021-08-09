from flask import Flask,request

app=Flask(__name__)


#第一次改动

# http://127.0.0.1:5000/
# http://127.0.0.1:5000/index
@app.route('/index')
@app.route('/')#路由
def index_view():#视图函数
    return '这是主页'

# http://127.0.0.1:5000/select
@app.route('/select',methods=['POST','GET'])
def junshi_view():
    print(request.method)
    if request.method=='GET':
        return '<form method="POST" >'\
        '<input type="text" name="uname" value="请输入"/>'\
        '<br>'\
        '<input type="password" name="pwd" placeholder="123"/>'\
        '<br>'\
        '<input type="submit">'\
        '</form>'\
        '<p>'\
        """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Rerum qui perspiciatis quia est in illum aspernatur, itaque molestias quo unde nihil corrupti voluptatum perferendis officia quod tempore porro sit quidem?"""\
        '</p>'
    elif request.method=='POST':
        return '<h2 align="center">收到提交</h2>'\
        '''<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis fugiat nam unde illum temporibus, error quos ducimus eos voluptates, assumenda, architecto perspiciatis nobis dolores a mollitia. Officia eligendi nihil doloribus!</p>'''

app.run(debug=True)