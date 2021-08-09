from flask import Flask,render_template

app=Flask(__name__,template_folder='temp_templates')#template_floder指定由哪个文件夹找模板

# 效果相同,内容不同的页面,可以考虑使用模板

# http://127.0.0.1:5000/
@app.route('/')
def index_view():
    title='《老王的幸福生活》'# 相同的格式传入不同的值
    author='qtx,老王'
    content='老王6点半起床，坐公交去公司，上班，18点下班，坐公交，回家'
    # 占位变量=参数
    return render_template("index.html",title=title,author=author,content=content)

# http://127.0.0.1:5000/user
@app.route('/user')
def user_view():
    return render_template("yemian.html")

app.run(debug=True)