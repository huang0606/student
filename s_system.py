
students = []

import pickle

def save_students(students):
    f = open('students.pkl', 'wb')
    pickle.dump(students, f)
    f.close()
    print('>>>学生档案已经保存到students.pkl 文件中')


class Student():

    def __init__(self):
        self. name = '无名氏'
        self. number = '_'
        self. gender = '未知'
        self. address = '未知'

    def __str__(self):
        return f'''+{self.name}-{self.number}
性别： {self.gender}
年龄： {self.address} '''


def main():
    try:
        f = open('students.pkl', 'rb')
        students = pickle.load(f)
        f.close()
    except:
        students = []

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
            student.address = input('请输入地址:')

            students.append(student)
            print(f'>>>成功加入一个学生:{student.name}')
        elif command == '2':
            print(f'>>>共有{len(students)}个学生')
            for student in students:
                print(student)
        elif command == '3':
            number = input('请输入需要删除学生学号').strip()
            pos = -1
            for i, student in enumerate(students):
                if student. number == number:
                    pos = i
                    break
                if pos == -1:
                    print(f'>>>没有找到学生号为{number}的学生')
                else:
                    del students[pos]
                    print(f'>>>成功删除学号为{number}的学生')
        # elif command == '4':
        #    pass
        elif command == '5':
            break
        else:
            print('非法代码，请重新输入')

        save_students(students)


if __name__ == '__main__':
    main()
