import unittest
import math
from src.main.assignment_1 import (
    approximation_algorithm,
    bisection_method,
    fixed_point_iteration,
    newton_raphson
)

class TestAssignment1(unittest.TestCase):
    def test_approximation_algorithm(self):
        self.assertAlmostEqual(approximation_algorithm(2, 15), math.exp(2), places=5)

    def test_bisection_method(self):
        def f(x): return x**3 - x - 2
        self.assertAlmostEqual(bisection_method(f, 1, 2), 1.521, places=3)

    def test_fixed_point_iteration(self):
        def g(x): return (x**3 - 2) / x
        self.assertAlmostEqual(fixed_point_iteration(g, 1.5), 1.521, places=3)

    def test_newton_raphson(self):
        def f(x): return x**3 - x - 2
        def df(x): return 3*x**2 - 1
        self.assertAlmostEqual(newton_raphson(f, df, 1.5), 1.521, places=3)

if __name__ == "__main__":
    unittest.main()
