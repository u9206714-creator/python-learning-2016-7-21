#一、面向过程编程指将要实现的事情拆分成一个个步骤
'''
def save_money(face_value,ATM_number,bank,banknote_number):
    ...
def withdraw_money(face_value,ATM_number,bank,banknote_number):
    ...
save_money(50,'001','招商银行','AA00000000')
withdraw_money(50,'001','中国银行','AA00000000')
'''


#二、面向对象编程即先考虑各个对象有什么性质、能做什么事情
#定义ATM类  ->类是创建对象的模板
'''
class ATM:
    def __init__(self,number,bank,subbranch):
        self.number = number    
        self.bank = bank
        self.subbranch = subbranch
'''
#创建两个ATM对象
'''
atm1 = ATM('001','招商银行','南园支行')
atm2 = ATM('002','中国银行','北园支行')

print(atm1.number)
'''



#三、属性对应对象所具有的性质，方法对应对象能做些什么 
#    ——> 属性是放在类里面的变量，方法是放在类里面的函数
#面向对象编程三个特性：封装，继承，多态



#四、学习class语法
#1、类定义属性
'''
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

cat1 = CuteCat('jojo',2,'orange')
'''

#2、类定义方法 -> 调用类方法：对象.方法名() ; 在class中定义函数

#practice

class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.number = student_id
        self.grades = {'chinese':0,'maths':0,'english':0}

    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade
    def print_grades(self):
        print(f'{self.name}(number:{self.number}) test scores:')
        for course in self.grades:
            print(f'{course}:{self.grades[course]}')
    def get_grade(self,course):
        if course in self.grades:
            return self.grades[course]
        else:
            return 'None such course!'
    def average_grade(self):
        total = 0
        for course in self.grades:
            total += self.grades[course]
        return total / len(self.grades)
stu1 = Student('Jack','01') 
stu1.set_grade('chinese',95)
stu1.set_grade('maths',97)
stu1.set_grade('english',98)
print(stu1.average_grade())



#1、
#stu1 = Student('Jack','01')
#stu1.set_grade('english',88)
#print(stu1.get_grade('english'))
 
#stu1 = Student('Jack','01',)
#stu1.set_grade('chinese',95)
#stu1.set_grade('maths',94)
#stu1.print_grades()
#stu2 = Student('Alice','02')
#print(stu1.name)
#stu2.set_grade('maths',95)
#print(stu2.grades)

 


































