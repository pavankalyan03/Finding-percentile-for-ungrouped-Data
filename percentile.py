print("Finding the perecintile")
l=list(map(int,input("give the input with seperated spaces: ").split()))
l.sort()
a=int(input("required percentile: "))


def percentile(a):

    z=len(l)
    x=(z+1)*(a/100)
    intpart,decpart=int(x),x-int(x)
    m=l[intpart-1]
    n=l[intpart]-l[intpart-1]
    percentile=m+(decpart*n)
    return percentile


def qrt_dev():
    q=percentile(75)
    r=percentile(25)
    y=(q-r)/2
    return y


print("required percentile is: ",percentile(a))
print("quartile deviation is: ",qrt_dev())
