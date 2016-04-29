def count_specMult(a , max_val):
    count=0
    num_list=list(range(1,max_val+1))
    p_list = prime_list(a)
    i=0
    while i<len(num_list):
        n=0
        c=1
        while n<a:
            if(num_list[i]%p_list[n]!=0):
                c=0
                break
            n+=1
        if(c==1):
            num_list[i]=0
        i+=1
    count = num_list.count(0)
    
    return count

def prime_list(a):
    p_list = []
    i=2
    n=0
    while n<a:
        if(isPrime(i)):
            p_list.append(i)
            n+=1
        i+=1
    return p_list

def isPrime(i):
    if(i==2):
        return True
    if(i%2==0):
        return False
    j=2
    while(j<=i/2):
        if(i%j==0):
            return False
        j+=1
    return True

print(count_specMult(4, 100000000))

