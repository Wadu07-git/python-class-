#operator is a symbol which is udes to perform certain operation. 
# 1. Arithmetic operator, %
# symbol 
# +, -, *, /, %, //(floor division), 

# 2. Assignment operator 
# x+=y => x=x+y
# x+=y => x=x-y
# x-=y => x=x*y
# x/=y => x=x/y
# x*=y => x=x*y
# x%=y => x=x%y
# x*=y => x=x*y
# x//=y => x=x

# 3. Logical operator 
# True and True = True 
# False and False = False 
#false and true = True 

# *not operator 
# not operator makes ture statements to fasle and false statements 
# true = false 
# false = true 

# 4. Comparision operation
#==equal to 
#>greater than
#< lower than 
#>=greater than and equals to
#<=lower than and equals to
#!= not equals to 

# data = 5 
# print(data>4)
# data = 5
# print (not(data == 4 or data == 5))

#5. Membership 
# in, not in 
# num_list = [1,2,3,4,5,6,7,8,9]
# x = 10 
# print(x in num_list) 
# print (x not in num_list)

#Identity operator
# x = 10 
# print(id(x))
# y = 10 
# print(id(y))
# listx = [1,2,3]
# print(id(listx))
# listy = [1,2,3]
# print(id(listy))
# print("this is an identity operator output:", x is y)
# print("thsi is an identity operator output:", listx is not listy)
# x = int(input("Enter your nunber:"))
# #if else statement
# if x >=0:
#     print("Given number is positive number")
# else: 
#      print("Given number is negative number")



# 5. Bitwise operator 

# # addition operator i python 
# 6. membership operator 
# 7. Identity operator 
# x = 1 
# y = 1
# a = '1'
# b = '1'
# age = int(input("Enter your age:"))
# if age >= 18:
#     print("you are eligible to vote")
# else: 
#     print("you are not eligible to vote")

# elif statement
#     if x >0:
#         print("given number is reater than zero")
#     elif x==0:
#         print(" given number is equal to zero")
#     else:
#         print("given number is negative")
         
# loop is repetation or iteration 
# positive_num = [1,2,3,4,5,6]

# for x in positive_num: 
#     print (x) 

# x = int(input ("enter a number :"))
# for i in range (1,11):
#     print(x,"X",i,"=",i*x) 
#     print(f"{x} x {i}= {i*x}")
    
    # while loop 
# y = 1
# while y<=20: 
#         print(y)
#         y+=1 
# #nestd loop 
# #outer loop 
# for i in range (1,10):
#     #inner loop 
#     for x in range(1,10):
#         print(f"{i} x {x} = {i*x}")

# for i in range(1,11):
#     x = 1
#     while x<=10: 
#         print(f"{i} x {x} = {i*x}") 
#         x+=1

#while inside while
#while inside for 
# for a in range (1,11):
#     if a == 5:
#         break 
#     print (a)
#continue 
for a in range (1,11):
    if a%2 ==0:
        continue 
    print(a)
for a in range (1,11):
    pass 