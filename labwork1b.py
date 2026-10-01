def input_student():
    students = []
    number_of_students = int(input("Enter the number of students: "))
    for _ in range(number_of_students):
        student = {
            "id": input("Enter student's id: "),
            "name": input("Enter student's name: "),
            "dob": input("Enter student's dob: "),
        }
        students.append(student)
    return students


def input_course():
    courses = []
    number_of_courses = int(input("Enter the number of courses: "))
    for _ in range(number_of_courses):
        course = {
            "id": input("Enter course's id: "),
            "name": input("Enter course's name: "),
        }
        courses.append(course)
    return courses


def input_mark(student, course, mark):
    course_id = input("Enter the course id to input marks for: ")
    if course_id not in {c["id"] for c in course}:
        print("Course id not found.")
        return

    if course_id not in mark:
        mark[course_id] = {}

    for s in student:
        student_mark = float(input(f"Enter mark for {s['name']} ({s['id']}): "))
        mark[course_id][s['id']] = student_mark


def list_students(student):
    print("List of students:")
    if not student:
        print("No students available.")
        return
    for s in student:
        print(f"- {s['name']} ({s['id']}), dob: {s['dob']}")


def list_courses(course):
    print("List of courses:")
    if not course:
        print("No courses available.")
        return
    for c in course:
        print(f"- {c['name']} ({c['id']})")


def show_marks(student, course, mark):
    course_id = input("Enter the course id to show marks for: ")
    if course_id not in mark:
        print("No marks available for this course.")
        return

    print(f"Marks for course {course_id}:")
    for s in student:
        if s['id'] in mark[course_id]:
            print(f"- {s['name']} ({s['id']}): {mark[course_id][s['id']]}")
        else:
            print(f"- {s['name']} ({s['id']}): No mark available")


def main():
    student = []
    course = []
    mark = {}
    while True:
        print("\nMenu:")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            student = input_student()
        elif choice == '2':
            course = input_course()
        elif choice == '3':
            input_mark(student, course, mark)
        elif choice == '4':
            list_students(student)
        elif choice == '5':
            list_courses(course)
        elif choice == '6':
            show_marks(student, course, mark)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()