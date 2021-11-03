def serie(check, n):
    if n > len(check):
        print ("Invalid length")
    else:              
        for i in range(len(check)):
            if len(check[i:i+n]) == n:
                print (check[i:i+n])
 
#serie(str(49142), 3)
x = int(input("Enter digits:" ))
n = int(input("Enter n:" ))
print(serie(str(x), n))
