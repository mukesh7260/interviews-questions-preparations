# l = [23,2,45,98,6,43,987,34]
# # sort assending orde 

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             l[i],l[j] = l[j],l[i]   

# print(l)


# character occurance 

# s = 'rohit sharma'
# d = {}
# for i in s:
#     if i in ' ':
#         continue
#     if i not in d:
#         d[i] = 1
#     else:   
#         d[i] += 1
# print(d)


# s = 'rohit sharma'
# d = {}
# for i in s:
#     if i!= ' ':
#         if i not in d:
#             d[i] = 1
#         else:   
#             d[i] = d[i] + 1 
# for k, v in d.items():
#     print(f'{k} - {v}')


# s = 'rohit sharma'
# d = {}
# for i in s:
#     if i!= ' ':
#         d[i] = d.get(i,0) + 1
# for k, v in d.items():
#     print(f'{k} - {v}') 


# s = 'rohit sharma'
# d = {}
# for i in s:
#     if i!= ' ':
#        a = d.get(i,0) + 1
#        d[i] = a

# for k, v in d.items():
#     print(f'{k} - {v}')