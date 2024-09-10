a=[2,3,27,20,11,27,10,19,10,13,10,2,15,23,19,3]
b=[1,24,2,10,9,7,3,12,24,10,9,22,9,5,10,5]
c=[2,2,10,15,6,9,16,17]
d=[5,7,8,24,8,3,6,15,22,6,1,1,11,27,14,5]
e=[2,17,15,14,5,10,2,22]
f=[6,10,4,1,5,5,4,8,6,3,1,6,10,6,10,2]
g=[6,13,3,3,6,10,10,10]

print(len(a),len(b),len(c),len(d), len(e), len(f), len(g))

def sumeucl(i):
    s=a[i]
    print(f"{a[i]}", end='+')
    if((i+d1)%2==1):
        s+=b[i]
        print(f"{b[i]}", end='+')
    else:
        s+=c[((i+d1)//2)%8]
        print(f"{c[((i+d1)//2)%8]}", end='+')
    if((i+d2)%2==1):
        s+=d[(i+d1)%16]
        print(f"{d[(i+d1)%16]}", end='+')
    else:
        s+=e[((i+d2)//2)%8]
        print(f"{e[((i+d2)//2)%8]}", end='+')
    if((i+d3)%2==1):
        s+=f[(i+d2)%16]
        print(f"{f[(i+d2)%16]}", end='+')
    else:
        s+=g[((i+d3)//2)%8]
        print(f"{g[((i+d3)//2)%8]}", end='+')
    print(f"={s}")
    return s

for d1 in range(16):
    for d2 in range(16):
        for d3 in range(16):
            match=True
            s=0
            for ip in range(16):
                sn=sumeucl(ip)
                print(f"d1={d1} d2={d2} d3={d3} s({ip})={sn}")
                if(s>0 and s!=sn):
                    print(f"seg {ip} different to previous try next")
                    match=False
                    break
                s=sn
            if(match):
                print(f"found d1={d1} d2={d2} d3={d3}")
                exit(0)
