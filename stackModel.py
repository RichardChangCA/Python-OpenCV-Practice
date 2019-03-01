"""
用栈（使用list）实现队列：支持push(element)，pop()和top()方法。
pop和top方法都应该返回第一个元素的值。比如执行以下操作序列：
push(1),pop(),push(2),push(3),top(),pop()，你应该返回1，2和2
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
