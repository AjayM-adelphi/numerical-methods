def gradient_descent(grad_f, x0, learning_rate, n_steps):
    x = x0
    history = [x]
    
    for _ in range(n_steps):
        x = x - learning_rate * grad_f(x)
        history.append(x)
    
    return x, history