i=1 
j=0
d = 0.0
e = -1
while i <= 30:
	den = (i+1.0)*(i+2.0)*(i+3.0)
	e = e * -1
	d = d + (e * 4.0) / den
	i= i+2
	kq = 3.0 + d
	j= j + 1
	print('Pi approximation', j,':', kq)