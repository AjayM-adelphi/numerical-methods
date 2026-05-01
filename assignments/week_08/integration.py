# Students should edit this Python file (just as you would a Python cell in a Jupyter Notebook)
# this module will contain functions for numerical integration



def trapezoidal_rule(f, a, b, N):
    h = (b - a) / N
    s = 0.5 * (f(a) + f(b))
    
    for i in range(1, N):
        s += f(a + i*h)
    
    return h * s


def simpsons_rule(f, a, b, N):
    if N % 2 != 0:
        raise ValueError("N must be even for Simpson's rule")
    
    h = (b - a) / N
    s = f(a) + f(b)
    
    for i in range(1, N):
        x = a + i*h
        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)
    
    return (h / 3) * s