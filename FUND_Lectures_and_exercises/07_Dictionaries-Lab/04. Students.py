students_dict = dict()
while True:
    split_command = input().split(":")
    if len(split_command) == 1:
        searched_course = split_command[0]
        break
    student_name = split_command[0]
    student_id = int(split_command[1])
    course_name = split_command[2]
    students_dict[student_name] = {"id": student_id, "course": course_name}

for key, value in students_dict.items():
    id_student = value["id"]
    course_searched = value["course"]
    if searched_course.startswith(value["course"][0:3]):
        print(f"{key} - {value['id']}")
