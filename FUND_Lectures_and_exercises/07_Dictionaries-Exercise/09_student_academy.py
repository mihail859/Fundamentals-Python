n = int(input())

students_dict_info = dict()
for i in range(n):
    name = input()
    grade = int(input())
    if name not in students_dict_info.keys():
        students_dict_info[name] = []
    students_dict_info[name].append(grade)