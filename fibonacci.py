def trinacci(n):
    a, b = 0, 1
    for y in range(n):
        print(a, end=" ")
        a, b = b, a + b

terms = float(input("Enter the number of terms: "))
fibonacci(terms)
