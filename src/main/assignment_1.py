x0 = 1.5
tol = 0.000001

def sqrt_two_approximation():
    iter_count = 0
    diff = x0
    x = x0

    print(f"{iter_count} : {x}")

    while diff >= tol:
        iter_count += 1
        y = x
        x = (x / 2) + (1 / x)
        print(f"{iter_count} : {x}")

        diff = abs(x - y)

    print(f"\nConvergence after {iter_count} iterations")

if __name__ == "__main__":
    sqrt_two_approximation()


def bisection_method(f, a, b, tol, max_iter):
  """
  Bisection Method to find a solution to f(x) = 0.

  :param f: The continuous function.
  :param a: The left endpoint of the interval.
  :param b: The right endpoint of the interval.
  :param tol: Tolerance for stopping criterion.
  :param max_iter: Maximum number of iterations.
  :return: Approximate solution p, number of iterations used, or message of failure.
  """

  # Initialize variables
  i = 1
  fa = f(a)

  # Bisection iteration
  while i <= max_iter:
      # Compute p
      p = a + (b - a) / 2
      fp = f(p)

      # Check for convergence
      if fp == 0 or (b - a) / 2 < tol:
          return p, i  # Procedure completed successfully

      # Update interval [a, b]
      i += 1
      if fa * fp > 0:
          a = p
          fa = fp
      else:
          b = p

  # Method failed after N0 iterations
  print('Method failed after {} iterations, N0 = {}'.format(max_iter, max_iter))
  return None, i

# Get user inputs
expression = input("Enter the function f(x): ")
a = float(input("Enter the left endpoint a: "))
b = float(input("Enter the right endpoint b: "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Define the function based on user input
def func(x):
  return eval(expression)

# Call the bisection method
result, iterations = bisection_method(func, a, b, tolerance, max_iterations)

# Print the result and number of iterations
if result is not None:
  print('Approximate solution:', result)
  print('Number of iterations used:', iterations)
else:
  print('Method failed to converge after', iterations, 'iterations.')

def fixed_point_iteration(g, p0, tol, max_iter):
  """
  Fixed-Point Iteration to find a solution to p = g(p).

  :param g: The function representing the fixed-point iteration.
  :param p0: Initial approximation.
  :param tol: Tolerance for stopping criterion.
  :param max_iter: Maximum number of iterations.
  :return: Approximate solution p, number of iterations used, or message of failure.
  """

  # Initialize variables
  i = 1
  p = g(p0)

  # Fixed-Point Iteration
  while i <= max_iter:
      # Check for convergence
      if abs(p - p0) < tol:
          return p, i  # Procedure was successful

      # Update variables
      i += 1
      p0 = p
      p = g(p0)

  # Method failed after N0 iterations
  print('The method failed after {} iterations, N0 = {}'.format(max_iter, max_iter))
  return None, i

# Get user inputs
expression_g = input("Enter the function g(p): ")
p0 = float(input("Enter the initial approximation p0: "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Define the function based on user input
def g(p):
  return eval(expression_g)

# Call the fixed-point iteration method
result, iterations = fixed_point_iteration(g, p0, tolerance, max_iterations)

# Print the result and number of iterations
if result is not None:
  print('Approximate solution:', result)
  print('Number of iterations used:', iterations)
else:
  print('The method failed to converge after', iterations, 'iterations.')

def newton_raphson_method(f, df, p0, tol, max_iter):
  """
  Newton-Raphson Method to find a solution to f(x) = 0.

  :param f: The function whose root is sought.
  :param df: The derivative of the function f.
  :param p0: Initial approximation.
  :param tol: Tolerance for stopping criterion.
  :param max_iter: Maximum number of iterations.
  :return: Approximate solution p, number of iterations used, or message of failure.
  """

  # Initialize variables
  i = 1
  p = p0

  # Newton-Raphson Iteration
  while i <= max_iter:
      # Compute p
      p = p - f(p) / df(p)

      # Check for convergence
      if abs(p - p0) < tol:
          return p, i  # Procedure was successful

      # Update variables
      i += 1
      p0 = p

  # Method failed after N0 iterations
  print('The method failed after {} iterations, N0 = {}'.format(max_iter, max_iter))
  return None, i

# Get user inputs
expression_f = input("Enter the function f(x): ")
expression_df = input("Enter the derivative f'(x): ")
p0 = float(input("Enter the initial approximation p0: "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Define the function and its derivative based on user input
def f(x):
  return eval(expression_f)

def df(x):
  return eval(expression_df)

# Call the Newton-Raphson method
result, iterations = newton_raphson_method(f, df, p0, tolerance, max_iterations)

# Print the result and number of iterations
if result is not None:
  print('Approximate solution:', result)
  print('Number of iterations used:', iterations)
else:
  print('The method failed to converge after', iterations, 'iterations.')