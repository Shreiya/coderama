my_list = [1, 2, 3, 4, -3]
my_list = list([3, 4, 5])

my_list = list()

my_list.append(7)
print my_list

print len(my_list)

b = [8]

c = my_list + b

print c

c.append(3)
print c

c.insert(1, 1000)
print c

#slice me up

print c[1:]
print c[1:3]
print c[-1] #since no colon, it'll only return an element
print type (c[-1])
print type (c[:-1])

c.sort()
print c

last_element = c.pop() #the parameters of () define the position of where you want the pop from
print last_element
print c


print "last_element: ", last_element, " rest: ", c

print 12 in c #bool

g = range(0, 40)
print g

g = range(0, 40, 3)
print g

f = ["bread", "elephants", "muffins"]

print " & ".join(f)
