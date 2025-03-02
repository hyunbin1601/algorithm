def prime_arr(n):
    prime = []

    def isPrime(a):
        if a < 2:
            return False
        for i in range(2,a):
            if(a%i==0):
                return False
        return True

    for i in range(n+1):
        if isPrime(i):
            prime.append(i)
    return prime

def solution(arr):
    arr.sort()
    a = 1
    prime_list = []
    list1 = []
    for i in arr:
        prime_list = []
        a = i
        while a!=1:
            
            for j in prime_arr(i):
                
                if a%j == 0 :
                    a = a//j
                    prime_list.append(j)
                    if a == 1:
                        list1.append(prime_list)
                    break
    return list1
    
arr1 = [2, 4, 6, 8, 14]
s = 1
for i in solution(arr1)[0]:
    s *= i
s1 = s
for i in solution(arr1):
    s1=s
    print(s1)
    for j in i:
        if s1 % j == 0:
            s1 = s1 // j
        else:
            s *= j
            
        
print(s)
print(solution(arr1))
                    
                    
for i in list1[0]:
    s *= i
s1= s
for i in list1:
    s1=s
    for j in i:
	    if s1%j == 0:
		    s1 = s1//j						
        else:
		    s *= j
    
return s