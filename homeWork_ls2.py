string = 'ipsum lorem text'
num_1 =10
num_2 = 3.5
bbb = True
lst = ['apple', 'samsung', 'xiaomi']
dct = {'brand': 'apple', 'model': 'iphone'}
tpl = (1,2,3,4)

result = (len(string) >= num_1 and lst[0] in dct.get('brand')) == bbb
print(result)


num_str = 125
num_str  = str(num_str)

message = 'Hi, my name is Python!'
message = message.replace('y','0')
message = message.replace('i', '1')

split_test = 'This is a split test'
split_test = split_test.split()
string_join = ' '.join(split_test)

ln = len(string_join)

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])

print(list_extend.index(6))
print(len(list_extend))


dict_test = {'car': 'Toyota', 'price': 4900, 'where': "EU"}
print(dict_test.get('car'), dict_test.get('where'))

print(dict_test.keys(), dict_test.values())

print(dict_test.items())
