from flask import Flask, render_template, request
import bitutil.stu
app = Flask(__name__)

@app.route("/insertForm")
def insertForm():
    return  render_template("insert.html")

@app.route("/insert", methods=['post'])
def insertStuPost():
    name = request.form['name']
    kor = request.form['kor']
    eng = request.form['eng']
    math = request.form['math']
    print(name+kor+eng+math)

    s = bitutil.stu.insertStu(name,kor,eng,math)
    print(s)
    return render_template("insert.html")


@app.route("/info", methods=['post'])
def infoStuPost():
    name = request.form['name']
    print(name)
    s = bitutil.stu.searchStu(name)
    print(s)
    return render_template("search.html", s=s)

@app.route("/info/<name>")
def infoStu(name):
    s = bitutil.stu.searchStu(name)
    print(s)
    return render_template("search.html", s=s)

# @app.route("/search")
# def searchStu(name):
#     return bitutil.stu.searchStu(name)

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/listStudent")
def listStudent():
    return bitutil.stu.listStudent()

@app.route("/")
def index():
    return "hello"
if __name__ == "__main__":
    app.run()