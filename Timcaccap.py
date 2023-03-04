
import random
def euclid(a, b):
    r1 = a 
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while(r2>0):
        q = r1//r2
        r = r1 - (q*r2)
        r1 = r2
        r2 = r 

        s = s1 - (q*s2)
        s1 = s2
        s2 = s 

        t = t1 - (q*t2)
        t1 = t2
        t2 = t 
    return r1, s1, t1

def listed(p,q):
    n = q* p
    phi =(p-1)*(q-1)
    while(1):
        num = random.randrange(2,n)
        a,b,c=euclid(phi,num)
        if a != 1:
            continue
        else:
            if c<0:
                c+=phi
            break

    with open ("Caccapkey.txt", "w") as f:
        f.write(str(hex(num)))
        f.write("\n")
        f.write(str(hex(c)))
def rdnumfile(a):
    ret =""
    for i in a:
        if (i.isalnum()):
            ret+=i
        else:
            break
    return int(ret,16)
# Bat dau chuong trinh
x, y = 0, 0
with open ("PaQ2.txt", "r") as f:
    x = rdnumfile(f.readline())
    y = rdnumfile(f.readline())

listed(x,y)
