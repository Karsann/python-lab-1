import time

print("ЗАВДАННЯ 1: Списки")
numbers = [10, 23, 45, 12, 67, 89, 34, 56, 78, 90]
print("Початковий список:", numbers)

print("Елемент за додатним індексом 2:", numbers[2])
print("Елемент за від’ємним індексом -1:", numbers[-1])

slice_1 = numbers[1:6]
slice_2 = numbers[:4]
slice_3 = numbers[1:8:2]
print("Зріз 1 [1:6]:", slice_1)
print("Зріз 2 [:4]:", slice_2)
print("Зріз 3 [1:8:2]:", slice_3)

numbers.append(99)
print("Після додавання 99:", numbers)

numbers.pop(3)
print("Після видалення числа з індексом 3:", numbers)
print()


print("ЗАВДАННЯ 2: Кортежі")
products = (
    (1, "Клавіатура", 15, 1200.50),
    (2, "Мишка", 30, 850.00),
    (3, "Монітор", 5, 9500.00),
)

print("Записи товарів:")
for p in products:
    print("ID:", p[0], "| Назва:", p[1], "| Кількість:", p[2], "| Ціна:", p[3])

total_value = 0
for p in products:
    total_value = total_value + (p[2] * p[3])

print("Загальна вартість інвентарю:", total_value, "грн")

try:
    products[0] = (9, "Тест", 1, 1.0)
except TypeError:
    print("Помилка: кортеж незмінний, змінити елемент не можна.")
    print()


print("ЗАВДАННЯ 3: Словники")
text = "python це круто пайтон це мова програмування"
words = text.split()
print("Вхідні слова:", words)

freq_dict = {}
for word in words:
    if word in freq_dict:
        freq_dict[word] = freq_dict[word] + 1
    else:
        freq_dict[word] = 1

print("Словник частот:", freq_dict)

print("Сортування за ключем:")
for key in sorted(freq_dict.keys()):
    print(key, ":", freq_dict[key])
print()


print("ЗАВДАННЯ 4: Множини")
collection_a = [101, 102, 103, 104, 102, 105]
collection_b = [103, 105, 106, 107, 101]

set_a = set(collection_a)
set_b = set(collection_b)

print("Множина A:", set_a)
print("Множина B:", set_b)

print("Перетин (A & B):", set_a & set_b)
print("Об'єднання (A | B):", set_a | set_b)
print("Симетрична різниця (A ^ B):", set_a ^ set_b)

sub = {101, 103}
print("Чи є {101, 103} підмножиною A?", sub.issubset(set_a))
print()


print("ЗАВДАННЯ 5: Бенчмарк")
n = 5000
data_list = list(range(n))
data_set = set(data_list)
target = n - 1

start_time = time.time()
for i in range(100):
    res = target in data_list
list_time = time.time() - start_time

start_time = time.time()
for i in range(100):
    res = target in data_set
set_time = time.time() - start_time

print("Час пошуку у списку для n =", n, ":", list_time)
print("Час пошуку у множині для n =", n, ":", set_time)
