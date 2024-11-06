#завдання 1

user_dict = {'Name': 'Stepan', 'pass': 'password123'}
user_write = 'Password123'

if user_dict.get('pass') == user_write:
    print('Ви увійшли в систему')
else:
    print("Неправильний пароль")

#завдання 2

days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
d =10
if d >= 1 and d < 8:
    print(days[d-1])
else:
    print('Go to home, you drunk')

# Завдання 3

a = 3
numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 10
for num in numb :
    print(f"{num} x {a} = {num * a}")

# Завдання 4

a = 0
list_number = [1, 12, 45, 143, 247, 641]
s = 0
while a <= len(list_number) - 1:
    s += list_number[a]
    a += 1
    print(s)

# Завдання 5

a = 2
f = a

while a > 1:
    f = f * (a-1)
    a -= 1
    print(f)

# Завдання 6

pair_num = []
t = 1

while t <= 50:
     if t % 2 == 0 :
         pair_num.append(t)
     t += 1
print(pair_num)


# Завдання 7

lst = []
dp_1 = 1
dp_2 = 432

for num in range(dp_1, dp_2 + 1):
    if num > 1:
      for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
          break
      else:
        lst.append(num)
print(lst)