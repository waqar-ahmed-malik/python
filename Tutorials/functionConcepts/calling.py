"""
Call By Value Or Call by reference

In python both kind of behaviors can be seen.
Run the below code and observe the output:

------------------------------------------------------------------------------------------------------------------------
def change_value(a: int, b:str, c:list, d:dict):
    a = a+2
    b = b + 'Ahmed'
    c[1] = c[2] * 2
    d['key'] = 'new_value'


a = 0
b = 'Hello '
c = [1, 2, 3]
d = {'key': 'value'}

print('Original Values')
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)

change_value(a, b, c, d)

print('Modified Values')
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)

------------------------------------------------------------------------------------------------------------------------

After looking at the output we can observe two behaviors:
1.  Call By Value
    a and b values doesn't change at all

2.  Call By Reference
    c and d values got modified

Conclusion: Mutable Objects show call by reference behavior and Immutable Objects show call by value behavior.

A.  Mutable Objects
    Objects whose size in memory can change.
    e.g. list, dict.

B.  Immutable Objects
    Objects whose size in memory can not change.
    e.g. string, integer, tuple(it's value can not be modified at all).

"""
