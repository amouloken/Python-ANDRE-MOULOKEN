def sum_difference(n=2):
 
    sum_of_squares = 0
    square_of_sum = 0
    for num in range(1, n+1):
        sum_of_squares += num * num
        square_of_sum += num
 
    square_of_sum = square_of_sum ** 2
 
    return square_of_sum - sum_of_squares
#message = int(input("Enter a message you want to be decrypt: "))
x = int(input("Enter your first n natural number:" ))
print(sum_difference(x))
