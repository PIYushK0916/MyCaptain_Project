def fibonaaci_no(n):
    if n == 0:
        return "Put Positive integer Invalid Value"
    elif n == 1 :
        return 0 
    elif n == 2 :
        return [0,1]
    else :
        fibonacci_series = [0, 1]
        for i in range (2, n):
            next_fibonacci_number = fibonacci_series[-1] + fibonacci_series[-2]
            fibonacci_series.append(next_fibonacci_number) 
        return fibonacci_series

number = int(input("ENTER THE TERM FOR FIBONACCI SERIES  : "))
result = fibonaaci_no(number)
print(f"THE FIBONACCI SERIES WITH TERM {number} IS : {result} ")
