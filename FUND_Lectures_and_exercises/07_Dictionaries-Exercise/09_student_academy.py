n = int(input())

students_dict_info = dict()
for i in range(n):
    name = input()
    grade = float(input())
    if name not in students_dict_info.keys():
        students_dict_info[name] = []
    students_dict_info[name].append(grade)

for key, val in students_dict_info.items():
    avg_score = sum(val) / len(val)
    if avg_score >= 4.50:
        print(f"{key} -> {avg_score:.2f}")