from flask import Flask,render_template

app=Flask(__name__,template_folder='project_templates')

# http://127.0.0.1:5000/
@app.route('/')
def index_view():
    return render_template('index.html',cid=1)

# http://127.0.0.1:5000/list/参数
@app.route('/list/<int:cid>')#路由传参
def result_view(cid):
    print(cid)
    if cid<=2:
        return '你传入的cid小于等于2'
    else:
        return '你传入的cid大于2'
app.run(debug=True)