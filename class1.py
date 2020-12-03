###  class1-1: #####
for i in range(1,10):
   for j in range(1,i+1):
       print(str(i)+"*"+str(j)+"="+str(i*j),end="")
   print("")
###  class1-2:  ###
Number=input("Number:")
product=1
for i in range([1,int(Number+1)]):
   product=product*i
print(product)
###  class1-3   ###  
a=input("Word:")
b=input("word:")
if a.lower() in b.lower():
   print("TRUE")
else:
   print("FALSE")
###  class1-4   ###  
a=input("Number:")
b=input("Number:")
if a>b:
   print("a>b")
else:
   print("a<b")
###  class1-4   ###  
Number=input("Number:")
while(int(Number)<9):
   print("The Number is :"+Number)
   break
###  class2-1   ###  
a=[1,2,3,4,5,6]
for i,j in enumerate(a):
   print("数组的索引是:"+str(i)+"数组的值是"+str(j))
###  class2-2   ###  
ixExist=False  ##boolean类型判断对错   字符都是重复的，是FALSE，否则是TRUE
word=input("Word:")
for i,j in enumerate(word):
    k=(word[i+1:])
    l=(word[0:i])
    if str(j).lower() in str(k).lower():
        print("a")
    elif i>0 and str(j).lower() in str(k).lower():
        print("a")
    else:
        print(i)
        isExist=True
        break
    if i>=len(word)-1 and isExist == False:
        print("没有不重复的字符")#length长度  Word的长度-1
 ###  class3-1  ###
nums=input("Number:")#0-10
while nums !=10:
             print(nums)
             nums=int(nums)+1
             print(nums)
             break#如果要到十停止就去掉break
