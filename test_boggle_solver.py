import unittest

# --- The module/class being tested ---
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    def add(self, a, b):      return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b


# --- The test class ---
class TestCalculator(unittest.TestCase):

    # Runs BEFORE each test method
    def setUp(self):
        self.calc = Calculator()

    # Runs AFTER each test method
    def tearDown(self):
        self.calc = None

    # --- 10 test frames ---

    def test_add_positive(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 4), 2.5)

    def test_divide_by_zero_raises(self):
        self.assertRaises(ValueError, divide, 10, 0)

    def test_result_is_float(self):
        self.assertIsInstance(divide(1, 2), float)

    def test_result_not_none(self):
        self.assertIsNotNone(self.calc.add(0, 0))

    def test_add_is_commutative(self):
        self.assertEqual(self.calc.add(3, 7), self.calc.add(7, 3))

    def test_multiply_by_zero(self):
        self.assertTrue(self.calc.multiply(99, 0) == 0)


if __name__ == "__main__":
    unittest.main()