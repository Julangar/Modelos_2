#factorial usando función lambda de forma recursiva
lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
print(lambda_factorial(4)) # 4 * 3 * 2 * 1 = 12 * 2 = 24

#fibonacci usando función lambda de forma recursiva
fibo = lambda f: f if f < 2 else fibo(f-1)+fibo(f-2) 
print ([fibo(n) for n in range(10)]) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]