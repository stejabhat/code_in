n=4
arr=[5,6,8,9]
k=3
ar=[]
# o=len(arr)//2
# arr.sort(reverse=True)
# print(arr)
# for i in range(o-1,n):
#     ar.append(arr[i])
# print(ar)
# for j in range(0,n-k):
#     ar.append(arr[j])
# print(ar)
    

f_p=sorted(arr[:k],reverse=True)
s_p=sorted(arr[k:],reverse=True)
print(f_p)
print(s_p)
k_p=f_p+s_p
print(k_p)