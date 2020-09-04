import MySQLdb
import MySQLdb.cursors
import pickle
from datetime import datetime


class StudentSystem():
    """ 学生管理系统控制类
    """

    def __init__(self):
        # 连接数据库服务器
        self.db = MySQLdb.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='root',
            db='student_system',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor, # 指定 cursor 返回的结果格式是字典而不是元组
        )
        # 系统内的学生列表
        self.students = []

    # def save_students(self):
    #     """ 将当前的学生列表信息保存到文件 students.pkl 中 """
    #     f = open('students.pkl', 'wb')
    #     pickle.dump(self.students, f)
    #     f.close()
    #     print('>>>学生档案已经保存到students.pkl 文件中')

    def load_students(self):
        self.students = []
        # 创建一个指针（用于执行查询和返回结果）
        with self.db.cursor() as c:
            # 执行一个查询
            c.execute('''
                SELECT *
                FROM students
                ORDER BY id;
            ''')
            # print(c.fetchall())  # 返回所有结果行

            for row in c.fetchall():
                student = Student()
                student.id = row['id']
                student.name = row['name']
                student.number = row['number']
                student.gender = row['gender']
                student.age = row['age']
                student.grade = row['grade']
                student.address = row['address']
                student.reg_time = row['reg_time']
                # print(row)
                self.students.append(student)

    def add_student(self, student):
        
        with self.db.cursor() as c:
            c.execute('''
                INSERT INTO students
                (name, number, gender,age, grade, address)
                VALUES
                (%s, %s, %s, %s, %s, %s);
            ''', [
                student.name,
                student.number,
                student.gender,
                student.age,
                student.grade,
                student.address,
            ])
        self.load_students()


    def delete_student(self, stu):
        """ 在当前的学生列表中删除一个学生
        :param stu: 传入需要删除的学生对象，或者这个学生的学号
        """
        
        pos = -1
        for i, student in enumerate(self.students):
            if str(student.number) == stu or student == stu:
                pos = i
                break
        if pos == -1:
            print(f'>>>没有找到可供刪除的学生 {stu}')
            return
        
        student = self.students[pos]
        with self.db.cursor() as c:
            c.execute('''
                DELETE FROM students
                WHERE id = %s
            ''', [
                student.id,
            ])
        print(f'>>>成功删除学生 {stu}')
        self.load_students()

    def main(self):
        """ 将 StudentSystem 以控制台交互的方式启动 """
        self.load_students()

        while True:
            print('''
    1. 添加学生
    2. 查看学生列表
    3. 删除学生
    4. 设置学生属性
    5. 退出系统
    ''')
            command = input('请输入您的操作:').strip()
            if command == '1':
                print('>>>添加学生')
                student = Student()
                student.name = input('请输入姓名:')
                student.number = input('请输入学号:')
                student.gender = input('请输入性别:')
                student.age = input('请输入年龄:')
                student.grade = input('请输入班级:')
                student.address = input('请输入地址:')
                self.add_student(student)

            elif command == '2':
                print(f'>>>共有{len(self.students)}个学生')
                for student in self.students:
                    print(student)
            elif command == '3':
                number = input('请输入需要删除学生学号').strip()
                self.delete_student(number)

            # elif command == '4':
            #    pass
            elif command == '5':
                break
            else:
                print('非法代码，请重新输入')


class Student():

    def __init__(self):
        self.id = None
        self.name = '无名氏'
        self.age = 0
        self.number = '_'
        self.gender = '未知'
        self.grade = '未知'
        self.address = '未知'
        self.reg_time = datetime.now()

    def __str__(self):
        return f'''+{self.name}-{self.number}
性别： {self.gender}
年龄： {self.age} 
班级： {self.grade} 
地址： {self.address} '''


if __name__ == '__main__':
    student_system = StudentSystem()
    student_system.main()
