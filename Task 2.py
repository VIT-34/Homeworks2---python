# 1 Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)

# 2 Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)

# 3 В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))

# 4 Написать программу преобразования десятичного числа в двоичное

n = int(input("Введите число: "))
result = []

while n:
    result.append(n % 2)
    n //= 2
result.reverse()
print(result)
