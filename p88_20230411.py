#p88 미분함수 
#파이썬으로 순간변화율 구하기

from sympy import symbols , Derivative

x=symbols ('x')
fx=x ** 2
fprime=Derivative(fx, x).doit()
y=fprime.subs({x:2})

print("x=2에서의 순간변화율 (미분계수, 미분값)은", y,"입니다")

