import os
from flask import Flask, request, render_template
# from s_system import StudentSystem, Student
from s_system_db import StudentSystem, Student
app = Flask(__name__)


os.environ.setdefault('FLASK_ENV', 'development')

system = StudentSystem()
system.load_students()


@app.route('/add_student.html', methods=['POST', 'GET'])
def add_student():
    context = dict(
        title='学生管理系统',
        message=None,
    )
    if request.method == 'POST':
        print(request.form)
        student = Student()
        student.name = request.form['name']
        student.number = request.form['number']
        student.age = request.form['age']
        student.gender = request.form['gender']
        student.grade = request.form['grade']
        student.address = request.form['address']
        system.add_student(student)
        context['message'] = f'操作成功，已经成功添加学生{student}<br><a href="/">返回</a>'
    
    return render_template(
        'add_student.html',
        **context
    )


@app.route('/del_student.html', methods=['POST'])
def del_student():
    num = request.form['student']
    system.delete_student(num)
    return f'操作成功，已经成功删除学生<br><a href="/">返回</a>'


@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        title='学生管理系统',
        students=system.students,
    )


if __name__ == '__main__':
    app.run()
