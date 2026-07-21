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
class ATM:
    def __init__(self,number,bank,subbranch):
        self.number = number    
        self.bank = bank
        self.subbranch = subbranch

#创建两个ATM对象
atm1 = ATM('001','招商银行','南园支行')
atm2 = ATM('002','中国银行','北园支行')

print(atm1.number)



#三、属性对应对象所具有的性质，方法对应对象能做些什么 
#    ——> 属性是放在类里面的变量，方法是放在类里面的函数
#面向对象编程三个特性：封装，继承，多态







