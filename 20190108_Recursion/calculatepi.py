def pi_series_iter(i):
    assert(i>=0)
    if i == 0:
        return 0
    else:
        return pi_series_iter(i-1) + 1 / i**2

def pi_approx_r(n):
    x = pi_series_iter(n)
    return (6*x)**(.5)

pi_approx_r(10)