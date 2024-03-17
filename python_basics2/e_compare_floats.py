def compare_float(a: float, b: float, tol: float) -> bool:  # tol: tolerance
    absolute = abs(a - b)
    print(f"{a} - {b} = {a - b}")
    return absolute < tol


first = 0.8
second = 0.1 + 0.7

print(compare_float(first, second, tol=1e-10))
