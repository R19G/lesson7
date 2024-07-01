grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = grades[0]
a_1 = sum(a) / len(a)   # найдено среднее арифметическое для [5, 3, 3, 5, 4]
# print(a_1)
b = grades[1]
b_1 = sum(b) / len(b)   # найдено среднее арифметическое для [2, 2, 2, 3]
# print(b_1)
c = grades[2]
c_1 = sum(c) / len(c)   # найдено среднее арифметическое для [4, 5, 5, 2]
# print(c_1)
d = grades[3]
d_1 = sum(d) / len(d)   # найдено среднее арифметическое для [4, 4, 3]
# print(d_1)
e = grades[-1]
e_1 = sum(e) / len(e)   # найдено среднее арифметическое для [5, 5, 5, 4, 5]
# print(e_1)
students1 = sorted(students)   # преобразовал множество в список, благодаря которому упорядочил имена учащихся
# print(students1)
grades1 = [a_1, b_1, c_1, d_1, e_1]  # список средних арифметических
students1_and_grades1 = dict(zip(students1, grades1))
print(students1_and_grades1)
