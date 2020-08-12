import pickle


class StudentSystem():
    """ 学生管理系统控制类
    """

    def __init__(self):
        # 系统内的学生列表
        self.students = []

    def save_students(self):
        """ 将当前的学生列表信息保存到文件 students.pkl 中 """
        f = open('students.pkl', 'wb')
        pickle.dump(self.students, f)
        f.close()
        print('>>>学生档案已经保存到students.pkl 文件中')

    def load_students(self):
        try:
            f = open('students.pkl', 'rb')
            self.students = pickle.load(f)
            f.close()
        except:
            self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f'>>>成功加入一个学生:{student.name}')
        self.save_students()

    def delete_student(self, stu):
        """ 在当前的学生列表中删除一个学生
        :param stu: 传入需要删除的学生对象，或者这个学生的学号
        """
        pos = -1
        for i, student in enumerate(self.students):
            if student.number == stu or student == stu:
                pos = i
                break
        if pos == -1:
            print(f'>>>没有找到可供刪除的学生 {stu}')
        else:
            del self.students[pos]
            print(f'>>>成功删除学生 {stu}')
        self.save_students()

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
        self. name = '无名氏'
        self.age = 0
        self. number = '_'
        self. gender = '未知'
        self. grade = '未知'
        self. address = '未知'

    def __str__(self):
        return f'''+{self.name}-{self.number}
性别： {self.gender}
年龄： {self.age} 
班级： {self.grade} 
地址： {self.address} '''


if __name__ == '__main__':
    student_system = StudentSystem()
    student_system.main()
