def my_function(x):
 # your code here
    y = str()
    i = -1
    while x[i] != x[0]:
        y = y+x[i]
        i = i-1
    y = y+x[0]
    return y


x = 'I can do it'
assert my_function(x) == "ti od nac I"

x = 'apricot'
print(my_function(x))
