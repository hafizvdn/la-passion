print('hello world');
a = 10;
b = 10;
def sum(a, b):
    c = a + b;
    return c

print(sum(a,b));

# this is a recuresion
d = 20
f = 0
def recursion_find_the_how_time_number(d,f):
    
    while d >= 5:
        d = d-5
        f += 1
    return f


print(recursion_find_the_how_time_number(d,f));
