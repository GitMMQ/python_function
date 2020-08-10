import math

#求函数的最小值
def solve_min(dy_dx, lr=0.001, epoches = 2000):
    dx = lambda x,lr : -lr * dy_dx(x)
    x = 1
    for _ in range(epoches):
        x += dx(x,lr)
    return x

#求函数等于特定的值
def solve(y,dy_dx,value, lr=0.01, epoches = 2000):
    loss = lambda x : (y(x) - value)**2
    dloss_dx = lambda x:2*(y(x) - value) * dy_dx(x)
    dx = lambda x,lr : -lr * dloss_dx(x)
    x = 1
    for _ in range(epoches):
        x += dx(x,lr)
    return x

if __name__ == "__main__":
    # 求sin(x)在0.5处函数的最小值
    n = 0.5
    y = lambda x: math.sin(x)
    dy_dx = lambda x: math.cos(x)
    loss = lambda x: (y(x) - n) ** 2
    dloss_dx = lambda x: 2 * (y(x) - n) * dy_dx(x)
    print(f"arcsin({n}) = {solve_min(dloss_dx, n) * 180 / math.pi}")

    # 求根号2
    n = 2
    y = lambda x: x ** 2
    dy_dx = lambda x: 2 * x
    loss = lambda x: (y(x) - n) ** 2
    dloss_dx = lambda x: 2 * (y(x) - n) * dy_dx(x)
    print(f"result({n}) = {solve_min(dloss_dx)}")

    """
    求 y = e^(sinx) 的最大值
    """
    n = math.e
    y = lambda x: (math.e) ** (math.sin(x))
    dy_dx = lambda x: y(x) * math.cos(x)
    loss = lambda x: (y(x) - n) ** 2
    dloss_dx = lambda x: 2 * (y(x) - n) * dy_dx(x)
    print(f"result(e)={solve(y, dy_dx, math.e)}")