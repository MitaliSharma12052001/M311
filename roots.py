import re
from math import *
func=input("function: ")
print(func)
der=input("der: ")
def f(x):
	return eval(func)
def df(x):
	return eval(der)
#-------------------------------
#------------------------------
def incsearch(x0,step):
	fx0=f(x0)
	x=x0
	fx=fx0
	if fx0==0:
		return x0,x0
	sgn=fx0/abs(fx0)
	iters=0
	revolve=False
	while fx/abs(fx)==sgn:
		x+=step
		fx=f(x)
		if fx==0:
			return x,x
		iters+=1
		if iters>1000:
			if revolve==False:
				x=x0
				step=-step
				iters=0
				revolve=True
			else:
				return("change step")
	return x-step,x
#---------------------------------
#---------------------------------
def newton(x0,n): # quadratic convergence $$\frac{\alpha-x_{n+1}}{\alpha-x_n}=-\frac{1}{2}\frac{f''(\alpha)}{f'(\alpha)}$$
	xs=[x0]
	print("iterations: ")
	print("n\tx\tf\tdf")
	for i in range(1,n+2):
		xi=xs[-1]
		fx=f(xi)
		d=df(xi)
		print(i-1,"\t",xi,"\t",fx,"\t",d)
		xs.append(xi-fx/d)
	print("root: ")
	print(xs[-2])
	print("error: ")
	err=xs[-1]-xs[-2]
	print(err)
	print("rel error: ")
	print(err/xs[-1])
	return xs[-2]
#------------------------------------
def bisection(a,b,err):
	fa=f(a)
	fb=f(b)
	m=a+(b-a)/2
	fm=f(m)
	print(a,b,m,fa,fb,fm)
	if abs(a-b)<err:
		return a
	if fa==0:
		return a
	if fb==0:
		return b
	if fm==0:
		return m
	if fm*fa>0:
		return bisection(m,b,err)
	else:
		return bisection(a,m,err)
#-------------------------------------
def bisect(a,b,digits):# linear convergence
	err=10**(-1*digits)*5
	print("a","b","mid","f(a)","f(b)","f(mid)")
	root=bisection(a,b,err)
	true=bisection(a,b,err*0.0001)
	error=true-root
	print("root: ", root)
	print("error: ", error)
	print("rel error: " , error/true)
	return root
#------------------------------------
def regula_falsi(a,b,err):
	fa=f(a)
	fb=f(b)
	m=(a*fb-b*fa)/(fb-fa)
	fm=f(m)
	print(a,b,m,fa,fb,fm)
	if abs(a-b)<err:
		return a
	if fa==0:
		return a
	if fb==0:
		return b
	if fm==0:
		return m
	if fm*fa>0:
		return regula_falsi(m,b,err)
	else:
		return regula_falsi(a,m,err)
def regulafalsi(a,b,digits):# improve bisection method by choosing intermediate point using chords.
	err=10**(-1*digits)*5
	print("a","b","chord-intercept","f(a)","f(b)","f(intercept)")
	root=regula_falsi(a,b,err)
	true=regula_falsi(a,b,err*0.0001)
	error=true-root
	print("root: ", root)
	print("error: ", error)
	print("rel error: " , error/true)
	return root
#------------------------------------
def secant(a,b,n): # supra-linear convergence, golden ratio, approximate derivative by divided difference
	x=[a,b]
	for i in range(2,n+2):
		x1,x0=x[-1],x[-2]
		fx1,fx0=f(x1),f(x0)
		xnew=(fx1*x0-fx0*x1)/(fx1-fx0)
		x.append(xnew)
	print("n","x","f(x)","error")
	for i in range(n+1):
		print(i,x[i],f(x[i]),x[i+1]-x[i])
	print("relative error: ", (x[n+1]-x[n])/x[n+1] )
	return x[-2]
#------------------------------------
