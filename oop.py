# class car:
#     color="red"

#     def __init__(self,brand,color):
#         self.type=brand
#         self.color=color
        
#     def drive(self):
#         print(f" this {self.color} car can drive any one")
#     def setcolor(self,color):
#         self.color=color


# car1=car("toyota","pink")
# print(car1.type)
# # car1.drive()
# # car1.setcolor("green")
# # car1.drive()


#Encapsulation



#special method

class book:
    def __init__(self,title,auther):
        self.title=title
        self.auther=auther
    def __str__(self):
        return f"{self.title} by {self.auther}"

b=book("george","")
print(b)
        