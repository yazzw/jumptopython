# list function practice code
# Easy practice with sequential numbers
data = [10,1,9,2,8,3,7,4,6,5]
data_s = data[:]
data_r = data[:]
data_p = data[:]

data_s.sort()
print(data_s)

data_r.reverse()
print(data_r)

data_p.pop()
print(data_p)
data_p.pop(0)
print(data_p)

