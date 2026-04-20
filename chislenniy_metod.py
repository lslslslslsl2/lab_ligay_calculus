import time
import numpy as np

# исходная функция
def f(x):
    return 1 / (x + 1)

# f_n(x) = floor(2^n * f(x)) / 2^n
def f_n(x, n):
    return np.floor((2 ** n) * f(x)) / (2 ** n)

# Численное вычисление интеграла Лебега функции f_n на [a, b]
def integrate_lebesgue(n, a=0.0, b=4.0, steps=200000):
    xs = np.linspace(a, b, steps + 1)
    ys = f_n(xs, n)
    return np.trapezoid(ys, xs)

# Численное вычисление интеграла Лебега–Стилтьеса
def integrate_stieltjes(n, a=0.0, b=4.0, steps=200000):
    xs = np.linspace(a, b, steps + 1)
    ys = 4 * xs * f_n(xs, n)
    return np.trapezoid(ys, xs)


# Значения параметра n, для которых строится приближение f_n
n_values = [10, 100, 1000]

exact_lebesgue = np.log(5)# Аналитическое значение интеграла Лебега:
exact_stieltjes = 16 - 4 * np.log(5)# Аналитическое значение интеграла Лебега–Стилтьеса:

print(f"Аналитическое значение интеграла Лебега: {exact_lebesgue:.10f}")
print(f"Аналитическое значение интеграла Лебега–Стилтьеса: {exact_stieltjes:.10f}")
print()

print("Численные расчеты:")
print()
print(f"{'n':>6} | {'Инт. Лебега':>14} | {'Ошибка':>14} | {'Инт. Стилтьеса':>18} | {'Ошибка':>14} | {'Время, с':>10}")
print()

for n in n_values:
    start = time.perf_counter()

    lebesgue_value = integrate_lebesgue(n)
    stieltjes_value = integrate_stieltjes(n)

    elapsed = time.perf_counter() - start

    lebesgue_error = abs(lebesgue_value - exact_lebesgue)
    stieltjes_error = abs(stieltjes_value - exact_stieltjes)

    print(
        f"{n:6d} | "
        f"{lebesgue_value:14.10f} | "
        f"{lebesgue_error:14.3e} | "
        f"{stieltjes_value:18.10f} | "
        f"{stieltjes_error:14.3e} | "
        f"{elapsed:10.6f}"
    )


