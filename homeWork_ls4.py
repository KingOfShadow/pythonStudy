# Завдання 1

test_lst = [1,2,3]
test_lst.extend([10,20])
test_lst.remove(10)
print(test_lst)

# Завдання 2

sum_lst = [1, 3, 12, 123, 321, 231]

s = 0
for n in sum_lst:
    s += n

print (s)

# Завдання 3

double = [1, 2, 3, 4, 5 ,6]

c = 0

for n in double:
    n *= 2
    double[c] = n
    c += 1

print(double)

# Завдання 4

tpl_1 = ("яблуко", "банан", "апельсин")

c = 0

for item in tpl_1:
    print(tpl_1[c])
    c +=1

# Завдання 5

spl_tpl_1 = (1, 2, 3)
spl_tpl_2 = (4, 5, 6)

new_tpl = spl_tpl_1 + spl_tpl_2
print(new_tpl)

# Завдання 6

dict_1 = {'name': 'Mike', 'age': 35, 'sport': 'footbal', 'country': 'UA'}
print(dict_1['name'], dict_1['age'], dict_1['sport'], dict_1['country'])

# Завдання 7

dict_2 = {'Rework': 2014, 'Harry Potter': 1990}
dict_2.update({'Jobs' : 2018})
print(dict_2)

# Завдання 8

countries_cap = {'Ukraine' : 'Kyiv', 'USA' : 'Washington', 'Germany' : 'Berlin'}

user_say = 'Ukraine'

print(f'In {user_say} capital is {countries_cap.get(user_say, None)}')