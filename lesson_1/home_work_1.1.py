# Написать программу,определяющую,что
# число трёхзначное и средняя цифра равна 5.

numbers = 457 #int(input())

is_three_digits = 0 < numbers // 100 <= 9
num = numbers % 100 // 10

print(is_three_digits, end=' ')
print(num == 5)

