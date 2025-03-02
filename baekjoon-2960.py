def prime(a):
    for i in a:
        if i == 2:
            return i
        else: 
            for j in range(2,i):
                if i%j == 0:
                    break
                elif j == i-1:
                    return i
                            

# n = int(input())
# k = int(input())
n, k = map(int, input().split())
s = 0
e = 0
x = 0
y = 2
list_1 = []
a = [i for i in range(2,n+1)]
while len(a) != 0:
    x = prime(a)
    y = x
    while True:
        if x in a:
            a.remove(x)
            list_1.append(x)
        x = x + y
        if a == []:
            break
        if x > a[-1]:
            break
        
print(list_1[k-1])        
        
        