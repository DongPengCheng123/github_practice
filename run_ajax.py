from flask import Flask,request,render_template

app=Flask(__name__,template_folder='project_templates')

# http://127.0.0.1:5000/get
@app.route('/get')
def get_result():
    print(request.args)
    uname=request.args.get('uname')
    upwd=request.args.get('upwd')
    return '接收GET数据成功，账号%s，密码%s'%(uname,upwd)

# http://127.0.0.1:5000/post
@app.route('/post',methods=['POST'])
def post_result():
    print(request.form)
    uname=request.form.get('uname')
    upwd=request.form.get('upwd')
    return '接收POST数据成功，账号%s，密码%s'%(uname,upwd)

#通过服务器访问demo2.html
@app.route('/')
def demo2_view():
    return render_template('demo2.html')

if __name__ == "__main__":
    app.run(debug=True)