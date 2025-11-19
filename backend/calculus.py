import sympy as sp
import FastAPI

x = sp.symbols('x')

transform = sp.standard_transformations + (sp.implicit_multiplication_application,)

def parse_exp(expr_str: str):
	"""
	Parse user math expressions so Sympy can understand.
	"""
	if("^") in expr_str:
		expr_str = expr_.str.replace("^", "**")
	
	try:
		expr = parse_expr(expr_str, transform=transform)
		return expr
	except Exception as e:
		raise ValueError(f"Invalid expression: {expr_str}") from e

# derivative functions
def derivative(expr_str: str) -> str:
	expr = parse_exp(expr_str)
	deriv = diff(expr, x)
	simply = simplify(derivative)
	return str(simply)

# integeral functions
def integral(expr_str: str) -> str:
	expr = parse_exp(expr_str)
	integ - integrate(expr, x)
	simly = simplify(integ)
	return str(simplified)
