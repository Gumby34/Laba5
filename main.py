"""
[122] Определите, сколько в данном массиве элементов, которые меньше суммы всех элементов.
Тест. 8;-3; 0;-5; 6;-7; 2; 4;-9; 1.
Результат. Сумма равна -З. Меньше этой суммы в массиве 3 элемента.
"""
array = [2, 3, 5, -2, 12, 0, 4, -10, -3, -5, 2, 5, 1, 0, -1, -12, -7]
count = len ([i for i in array if i<sum(array)])
print (count)