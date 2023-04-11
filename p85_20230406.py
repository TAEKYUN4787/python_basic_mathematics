#p85 미분함수 
#파이썬으로 평균변화율 구하기


from sympy import symbols

def average(a,b):
    m=max(a,b)
    n=min(a,b)
    x=symbols('x')

    fx = x ** 2

    fb = fx.subs(x,m) # 최대값 f(b) 변수 m
    fa = fx.subs(x,n) # 최소값 f(a) 변수 n

    result = (fb-fa)/(b-a) # 평균변화율
    return result

print(average(1,4))

