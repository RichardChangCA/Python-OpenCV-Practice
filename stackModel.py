"""
��ջ��ʹ��list��ʵ�ֶ��У�֧��push(element)��pop()��top()������
pop��top������Ӧ�÷��ص�һ��Ԫ�ص�ֵ������ִ�����²������У�
push(1),pop(),push(2),push(3),top(),pop()����Ӧ�÷���1��2��2
"""

class Stack:

    def __init__(self):
        self.lis = []
        
    def my_push(self, element):
        self.lis.append(element)

    def my_top(self):
        print(self.lis[0])
        return self.lis[0]

    def my_pop(self):
        return_value = self.lis[0]
        self.lis.remove(self.lis[0])
        print(return_value)

s = Stack()
s.my_push(1)
s.my_pop()
s.my_push(2)
s.my_push(3)
s.my_top()
s.my_pop()
