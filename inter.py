#1 count the number of each elements inside the array
# n=int(input())
# arr=[]
# x=int(input())
# print("Enter the numbers")
# for i in range(n):
#     k = int(input())
#     k=int(k)
#     arr.append(k)
# print(arr)
# count=0
# for i in range(n):
#     if arr[i]==x:
#        count+=1
# print(count)

# #2 addition of two numbers without using +
# q=int(input())
# v=int(input())
# # r=q-(-v)
# print(r)

#3 modulus of two numbewrs without using mod

# r=(q*v)//(q-v)-v

#4 get the answer without using // and % hw


# print(r)






#5 highest prime factor
# arr=[]
# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         arr.append(i)
# print(arr)


# def is_prime(n):
#     if n<2:
#         return False
#     if n>2:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True


# def highest_prime(arr):
#     hp=0
#     for num in arr:
#         if is_prime(num) and num>hp:
#             hp=num
#     return hp
# print(highest_prime(arr))

#6 find out missing numbers
#wrong till line no.80
# n=int(input())
# arr=[]
# for i in range(n-1):
#     k=int(input())
#     arr.append(k)
# print(arr)
# def missing(n):
#     i=0
#     for arr in range(n-1):
#         i+=1

#         if i!=arr:
#             print(i)
#     return n
# print(missing(n))


# loops,arrays,matrix,binary tree for tomorrow


#7 need to find all the elements occuring more than once in the given numbers set, wronggggggggggggggggg
# n=int(input())
# arr=[]
# x=int(input())
# print("Enter the numbers")
# for i in range(n):
#     k = int(input())
#     k=int(k)
#     arr.append(k)
# print(arr)
# count=0
# for i in range(n):
#     if arr[i]==x:
#        count+=1
#     print(count)
# if count>1:
#         print(arr[i])


#8 find the second highest value in the array
n=int(input())
arr=[]
for i in range(n):
    k = int(input())
    k=int(k)
    arr.append(k)
print(arr)
arr.sort()
u_a=list(set(arr))
print(u_a)
m=len(arr)
k=m-1
if n<=1:
    print(-1)
else:
    print(u_a[n-k])

