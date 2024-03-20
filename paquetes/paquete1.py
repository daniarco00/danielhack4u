
class Course:
    def __init__(self, name, duration, link):
        self.name = name
        self.duration = duration
        self.link = link

    def __repr__(self):
        return f'Name: {self.name}, Duration: {self.duration}, Link: {self.link}'


courses = [
    Course('Python', '6 months', 'https://www.python.org/'),
    Course('JavaScript', '6 months', 'https://www.javascript.com/'),
    Course('Java', '6 months', 'https://www.java.com/'),
]
def list_courses():
    for course in courses:
        print(course)

def search_course_by_name():
    for course in courses:
        if course.name == 'Python':
            return course
    return None

list_courses()
search_course_by_name()