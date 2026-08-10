# # student={
# #     "name":"Abdul hadi ",
# #     "Roll_no":3341,
# #     "program":"bscs",
# #     "cgpa":3.1

# # }

# # list=[1,2,3,4,5]
# # for index, item in enumerate(list):
# #     print(index ,item)

# # for key, value in student:
# #     print(f"{key} = {value}")

# # def add(a,b):
# #     return(a+b)


# # print(add(2,3))

# squr=lambda x:x*x
# print(squr(5))

# add=lambda a,b:a+b
# print(add(4,5))

# num=[1,2,3,4,5,6,7,8,9]
# squares=list(map(lambda x:x*x,num))
# final="-".join(map(str,squares))
# print(final)
# print(squares)

# odd=list(filter(lambda x:x%2!=0,num))
# print(odd)


import pyttsx3
import random
import mymodule
mymodule.greed()

num=random.randint(0,10)
print(num)

engine=pyttsx3.init()
engine.say("hello hadi i love you last night i saw you in my night mare and we are getting marriage will you marry me oh offcource i will never marry you bhootni curaaaaaaaaaaaaaaaaaaaaaaaaaail kehi ki na ho to")
engine.runAndWait()

