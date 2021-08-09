from flask import Flask,render_template,request

app=Flask(__name__,template_folder='project_templates')

# http://localhost:5000/login
@app.route('/login',methods=['POST','GET'])
def login_view():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        print(request.form)
        return '<h4>用户登录成功!</h4>'\
            '欢迎%s登录，您的登录密码是%s'%(request.form['uname'],request.form['upwd'])

# http://localhost:5000/show
@app.route('/show',methods=['POST','GET'])
def show_view():
    return '<h4>用户登录成功!!</h4>'

app.run(debug=True)