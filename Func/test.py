''''''''''
def lcs(a,b):
	num=0
	if len(b)>len(a):
		return num
	for i in range(0,len(a)-len(b)+1):
		if	a[i:i+len(b)]==b:
			num+=1
	return num
def son_string_dic(a,k):
	dic={}
	for i in range(0,len(a)-k+1):
		dic[a[i:i+k]]=1
	return dic
print(lcs("bababa","a"))



def deside(x,N):
	for i in range(N):
		if i == 0:
			if x <= N:
				return 1
		else:
			if x<=((2*N-i)*(i+1))/2:
				return i+1
	return -1
if __name__ == '__main__':
	c="test"
	while c!=None:
		c=input()
		a = c.split()
		x = int(a[0])
		y = int(a[1])
		N = int((-1 + int(1 + 8 * (x + y)) ** 0.5) / 2)
		print(deside(x, N))
	
	while(input())
		a = line.split()
		x=int(a[0])
		y=int(a[1])
		N = int((-1 + int(1 + 8 * (x+y)) ** 0.5) / 2)
		print(deside(x,N))


def func0(x,y,z):
	result=0
	for i in range(1, x + 1):
		for j in range(1, y + 1):
			for l in range(1, z + 1):
				if i + j > l and i + l > j and j + l > i:
					result += 1
	return result
#print(divmod(result,10000000007)[1])
if __name__ == '__main__':
	c="test"
	while c!=None:
		c = input()
		a = c.split()
		x = int(a[0])
		y = int(a[1])
		z=int(a[2])
		print(divmod(func0(x,y,z), 10000000007)[1])
'''''''''''











def func(head):
    if head==None:
        return None
    p=head
    temp=None
    pre=None
    while p!=None:
        temp=p.next
        p.next=pre
        p=temp
    return pre












import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))








