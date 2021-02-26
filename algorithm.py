import math
from functools import cmp_to_key
# sum ,n =0 ,0
# for i in range(5):
#     if i==3:
#         continue
#     for j in range (10):
#         if j==3:
#             continue
#         for a in range(10):
#             if a==3:
#                 continue
#             for b in range (10):
#                 if b==3:
#                     continue
#                 sum=i+j+a+b
#                 if sum!=0 and sum %3 ==0:
#                     n+=1


# print(res)

# #3的倍数
# k ,n =1 ,0
# def isT(nu) : 

#     if nu%3 == 0:         
#         return True
#     while nu>0:
#         if nu%10 == 3:
#             return True
#         nu//=10
#     return False

# while k<=33333:
#     if isT(k) :
#         n+=k
#     k+=1

# print(n,k)




#邮票
# m=[]
# v=0
# n=0
# for i in range(31):
#     for j in range(41):
#         for k in range(41):
#             v=(i)*205+(j)*82+30*(k)
#             if v in m:
#                 continue
#             m.append(v)
#             n+=1

# print(n-1)

# sum, k =0, 1
# while k<=99:
#     sum, k =sum+k**4, k+1

# print (sum)


# i , j ,k =1, 0 ,5
# n=3
# while n<31:
#     i, j, k=j,k, i+j+k
#     n+=1

# print(k)

#逆数和
# n,sum =1 , 0
# while sum<=15:
#     sum,n=sum+1.0/n,n+1
# print(n-1)


#三角形
# def is_sqr(num):
#     a = int(math.sqrt(num))
#     return a * a == num

# n=0
# are=8192*2
# for i in range(1,are+1):
#     j=i
#     while i*j<=are:
        
#         if is_sqr(i**2+j**2):
#             n+=1
#         j+=1

# print(n)


#耐数
# def isT(num):
#     id,next=0,1
#     while num>10:
#         next=1
#         while num>0:    
#             next*=num%10
#             num//=10
#         num=next
#         id+=1
#     # print(id)
#     return id==7
# n=0
# for i in range(1000000):
#     if isT(i):
#         n+=1

# print(n)


#圆周
# s='1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989'
# m={}
# maxl=0
# ss=''
# for i in range(1,1000):
#     tem=s[i-1:i+1]
#     if m.get(tem):
#         m[tem]+=1
#     else :
#         m[tem]=1
#     if m[tem]>maxl:
#         maxl=m[tem]
#         ss=tem

# print (ss)

# n=1234567890
# sum=0
# for k in range(1,2000001):
#     if n%k==0:
#         sum+=k
# print(sum)





# #约数
# from functools import cmp_to_key
# def smma(num):
#     for i in range(2,num+1):
#         if num%i==0:
#             return i
# def cmpp(i,j):
#     return i-j
# def cmpa(i,j):
#     if smma(i)>smma(j):
#         return -1
#     elif smma(i)==smma(j):
#         return j-i
#     else :
#         return 1
# l=[]
# for i in range(2,1000001):
#     if i%2==0:continue
#     l.append(i)

# sorted(l,key=cmp_to_key(cmpa))
# print(l[240000])


# ll=240001
# l=[]
# for i in range(1000000,1,-1):
   
#     if i%2==0 or i%3==0 or i%5 ==0:
#         continue
#     if i % 7 == 0:
#         l.append(i)
#     else: 
#         l.insert(0,i)
      
# print (l[ll-1])
# res=699937

        
        

#罗马
# digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), 
#           (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

# def intToRoman(num: int) -> str:
#     roman_digits = []
#     # Loop through each symbol.
#     for value, symbol in digits:
#         # We don't want to continue looping if we're done.
#         if num == 0: break
#         count, num = divmod(num, value)
#         # Append "count" copies of "symbol" to roman_digits.
#         roman_digits.append(symbol * count)
#     return "".join(roman_digits)

# n=1
# sum=0

# for i in range(1,1001):
#     if len(intToRoman(i))==9:
#         sum+=i
# print (sum)


#螺旋矩阵
# m=n=48
# test = [[0 for i in range(m)] for j in range(n)]

# def spiralOrder(matrix) :
#     if not matrix or not matrix[0]:
#         return list()
        
#     rows, columns = len(matrix), len(matrix[0])
#     visited = [[False] * columns for _ in range(rows)]
#     total = rows * columns
#     order = ['0']*rows

#     directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     row, column = 0, 0
#     directionIndex = 0
#     for i in range(total):
#         matrix[row][column]= chr(ord('A')+i%26)
#         if row==column:
#             order[row]=matrix[row][column]
#         visited[row][column] = True
#         nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
#         if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
#             directionIndex = (directionIndex + 1) % 4
#         row += directions[directionIndex][0]
#         column += directions[directionIndex][1]
#     return order

# orderb=spiralOrder(test)

# print (''.join(orderb))



#日历
# week=0
# co=12
# y=2001
# day,mon=13, 1
# n=0
# moo={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# while True :
#     week=(co+week)%7
    
#     if week==5:
#         n+=1

#     if n==666:
#         break
#     co=moo[mon]
#     if mon==2 and y%4==0:
#         co+=1
#     mon+=1
#     if mon>12:
#         y+=1
#         mon=1

# print (y,mon,day,week,n)



#7位长度 剩下位的数量

# def isT(s):
#     stack=[]
#     for c in s:
#         if not stack or c>=stack[-1]:
#             stack.append(c)

#     return len(stack)==5

# #print(isT("3141592658979"))
 

# n=0
# for i in range(10000000):
#     tem='0'*(7-len(str(i)))
#     tem=tem+str(i)  
    
#     if isT(tem):
#         n+=1
# print (n)
#135135


#国际象棋
# m=n=50
# def spiralOrder(num,i,j) :
#     q=[[i,j]]
#     l=v=[]
#     directions = [[-2 ,1], [-2, -1], [-1, 2], [-1, -2],[1,2],[1,-2],[2,-1],[2,1]]
#     while num>0:
#         l=[]
#         v=[]
#         for c in q:
#             for i in range(8):
#                 nr=c[0]+directions[i][0]
#                 nc=c[1]+directions[i][1]
#                 if 0<=nr<m and 0<=nc<n and nr*m+nc not in v:
#                     v.append(nr*m+nc)
#                     l.append([nr,nc])
#         q=l
#         num-=1
#     return q
# q=spiralOrder(25,0,0)
# print(len(q))

# 装货
# n=5000
# num=1
# for i in range(800,0,-1):
#     if i>n:
#         num+=1
#         n=5000
#     n-=i
# print(num)

#范数
# num=0
# for i in range(1000,10000):
#     num=i*728
#     if len(str(num))==6:
#         s=str(i)+str(num)
#         if len(set(s))==10:
#             break
        
# print(num)







