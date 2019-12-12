li = [1, 3, 4, 9, 5, 6, 6, 2]

li = sorted(li, reverse=True)

li = [1, -3, -4, -9, 5, 6, 6, 2]

li = sorted(li)

li = sorted(li, key=abs)


class employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age

e1 = employee('Waqar', 22)
e2 = employee('Nishat', 19)
e3 = employee('Zaheen', 18)

li = [e1, e2, e3]

def e_sort (emp):
    return emp.age

li = sorted(li, key=e_sort)
for e in li:
    print(e.name)


from operator import itemgetter

my_dict = {'Waqar': 22,
           'Zaheen': 18,
           'Nishat': 19}
my_dict = sorted(my_dict.items(), key=itemgetter(0))

print(my_dict)              # based on key of dict


from operator import itemgetter

my_dict = {'Waqar': 22,
           'Zaheen': 18,
           'Nishat': 19}
my_dict = sorted(my_dict.items(), key=itemgetter(1))
print(my_dict)              # based on value of dict
