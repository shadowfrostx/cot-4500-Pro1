import math

def approximation_algorithm(x, n):
    result = 0
    for i in range(n + 1):
        result += (x ** i) / math.factorial(i)
    return result

def bisection_method(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at the interval endpoints must have opposite signs.")
    
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("Fixed-point iteration did not converge.")

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            raise ValueError("Derivative is zero. Method fails.")
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("Newton-Raphson method did not converge.")

if __name__ == "__main__":
    # Example function for root-finding
    def f(x):
        return x**3 - x - 2
    
    def df(x):
        return 3*x**2 - 1
    
    def g(x):
        return math.sqrt(x + 2)  # Example function for fixed-point iteration
    
    print("Approximation Algorithm:", approximation_algorithm(2, 10))
    print("Bisection Method:", bisection_method(f, 1, 2))
    print("Fixed-Point Iteration:", fixed_point_iteration(g, 1.5))
    print("Newton-Raphson Method:", newton_raphson(f, df, 1.5))
