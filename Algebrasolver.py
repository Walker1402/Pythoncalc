from sympy import symbols, Eq, solve

def algebra_solver():
    x = symbols('x')
    while True:
        equation = input("Please enter an equation (or 'quit' to stop): ")
        if equation.lower() == 'quit':
            break
        equation = equation.replace("x", "*x")
        equation = Eq(*map(eval, equation.split("=")))
        solution = solve(equation)
        print(f"The solution is: {solution}")

# Run the function
algebra_solver()
