# test_assignment_1.py
import unittest
from src.main.assignment_1 import bisection_method, fixed_point_iteration, newton_raphson_method

class TestAssignment1(unittest.TestCase):
    def test_bisection_method(self):
        # Test Bisection Method with known parameters
        result = bisection_method(lambda x: x**2 - 2, 0, 2, 1e-6, 100)
        self.assertAlmostEqual(result, 1.414213, places=6)

    def test_fixed_point_iteration(self):
        # Test Fixed-Point Iteration with known parameters
        result = fixed_point_iteration(lambda x: (x / 2) + (1 / x), 1.5, 1e-6, 100)
        self.assertAlmostEqual(result, 1.414213, places=6)

    def test_newton_raphson_method(self):
        # Test Newton-Raphson Method with known parameters
        result = newton_raphson_method(lambda x: x**2 - 2, lambda x: 2 * x, 1.5, 1e-6, 100)
        self.assertAlmostEqual(result, 1.414213, places=6)

    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()