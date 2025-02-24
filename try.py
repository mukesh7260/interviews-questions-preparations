

# sorting list eithor assending or desending

l = [23,45,8,47,27,54] 
for i in range(len(l)):
    for j in range(len(l)):
        if l[i] > l[j]:
            l[i] , l[j] = l[j] , l[i] 

print(l)