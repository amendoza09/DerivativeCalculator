# stuff for calculus problem solving
import sympy as sp
# import FastAPI

x = sp.symbols('x')
f = input("input function f(x)=")

deriv = sp.diff(f,x)

print("f'(x)=", deriv)
