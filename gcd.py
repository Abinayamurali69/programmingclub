def find_gcd(x,y):
    smallest=min(x,y)
    for i in range(1,smallest+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd
def get_euclid_gcd(a,b):
    while b:
        a,b=b,a%b
    return a
if __name__=="__main__":
    gcd1=find_gcd(48,60)
    gcd2=get_euclid_gcd(48,60)
    print(gcd1)
    print(gcd2)
