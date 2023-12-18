# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 23:51:14 2023

@author: admin
"""




#طباعة رسالة بسيطة:
'''
print("مرحبًا بك في عالم البرمجة!")
'''



num1 = 5
num2 = 3
result = num1 + num2
print("نتيجة الجمع هي:", result)


#استخدام الشرطيات:
'''
age = 18
if age >= 18:
    print("أنت بالغ .")
else:
    print("أنت  قاصر.")
'''
#استخدام الحلقات (for loop):
'''
for i in range(5):
    print("رقم:", i)
'''
#قائمة وتكرارها:
'''
fruits = ["تفاحة", "موز", "فراولة"]
for fruit in fruits:
    print("الفاكهة:", fruit)

'''

#الدالة البسيطة:
'''
def greet(name):
    print("مرحبًا", name)

greet("أحمد")
'''

#القائمة والاستخدام الشرطي:
'''
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        print(number, "هو عدد زوجي.")
    else:
        print(number, "هو عدد فردي.")
'''

#تكامل القوائم (List Comprehension):
'''
squares = [x**2 for x in range(5)]
print("التربيعات:", squares)
'''

#العمل مع النصوص:
'''
    sentence = "أنا أتعلم بايثون"
print("عدد الحروف في الجملة:", len(sentence))
'''
#استخدام مكتبة الوقت (Time Library):

import time

print("مرحبًا بك!")
time.sleep(10)
print("شكرًا لانتظارك.")





from math import *
print(sqrt(25))
