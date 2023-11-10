def add_student_score(student_dict, name, course, points):
    if name not in student_dict.keys():
        student_dict[name] = {'language': course, 'score': []}
    student_dict[name]['score'].append(points)
    return student_dict


def banned_student(student_dict, name):
    del student_dict[name]
    return student_dict


students = dict()

while True:
    input_line = input()
    if input_line == "exam finished":
        break
    split_line = input_line.split("-")
    name_student = split_line[0]
    technology_or_banned_command = split_line[1]
    if technology_or_banned_command == "banned":
        students = banned_student(students, name_student)
    else:
        task_points = int(split_line[2])
        students = add_student_score(students,
                                     name_student,
                                     technology_or_banned_command,
                                     task_points)
