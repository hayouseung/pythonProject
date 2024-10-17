# Quiz 1
import random


def generate_lotto_numbers():
    result = []
    while len(result) < 6:
        num = random.randint(1, 45)
        if num not in result:
            result.append(num)
    return result


print(generate_lotto_numbers())


# Quiz 2
class Gugudan:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1, 10):
            print(f"{self.num} X {i} = {self.num * i}")


# 예시 사용
three_dan = Gugudan(3)
three_dan.output()


# Quiz 3
class Student:
    def __init__(self, student_id, name):
        # 학생의 ID와 이름을 초기화
        self.student_id = student_id
        self.name = name
        # 학생의 성적을 저장할 딕셔너리 초기화
        self.grades = {}

    def add_grade(self, subject, grade):
        # 특정 과목의 성적을 추가
        self.grades[subject] = grade

    def get_average_grade(self):
        # 성적이 없을 경우 평균 성적은 0
        if not self.grades:
            return 0
        # 모든 성적의 평균을 계산한 뒤 반환
        return sum(self.grades.values()) / len(self.grades)

    def display_info(self):
        # 학생의 정보를 출력
        print(f"Student ID: {self.student_id}, Name: {self.name}")
        # 각 과목의 성적을 출력
        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")
        # 평균 성적을 출력(소수점 둘째 자리)
        print(f"  Average Grade: {self.get_average_grade():.2f}")


class Subject:
    def __init__(self, name):
        # 과목의 이름을 초기화
        self.name = name


class Grade:
    def __init__(self):
        # 학생들 정보를 저장할 딕셔너리를 초기화
        self.students = {}

    def add_student(self, student):
        # 학생을 성적부 기록
        self.students[student.student_id] = student

    def add_grade(self, student_id, subject, grade):
        # 특정 학생의 성적을 추가
        if student_id in self.students:
            self.students[student_id].add_grade(subject, grade)
        else:
            print("Student not found!")

    def display_all_students(self):
        # 모든 학생의 정보를 출력
        for student in self.students.values():
            student.display_info()


# 예시 사용
student1 = Student(1, "Alice")
student2 = Student(2, "Bob")

grade_book = Grade()
grade_book.add_student(student1)
grade_book.add_student(student2)

grade_book.add_grade(1, "Math", 95)
grade_book.add_grade(1, "Science", 88)
grade_book.add_grade(2, "Math", 78)
grade_book.add_grade(2, "Science", 85)

grade_book.display_all_students()
