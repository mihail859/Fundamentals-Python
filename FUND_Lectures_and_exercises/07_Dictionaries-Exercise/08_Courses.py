def add_student(dict_courses, course, student):
    if course not in dict_courses.keys():
        dict_courses[course] = []
    dict_courses[course].append(student)
    return dict_courses

dict_courses_info = dict()
while True:
    input_data = input()
    if input_data == "end":
        break
    course_name, student_name = input_data.split(" : ")
    dict_courses_info = add_student(dict_courses_info, course_name, student_name)

for key, value in dict_courses_info.items():
    print(f"{key}: {len(value)}")
    for c in range(len(value)):
        print(f"-- {value[c]}")