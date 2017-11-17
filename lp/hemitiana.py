def fibonacci(n):
  if n < 1:
    return n 
  else:
    print(fibonacci(n-1) + fibonacci(n-2))
      
fibonacci(5)
