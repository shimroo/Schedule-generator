from datetime import datetime
from itertools import product
import util
import sys


class Course:

    def __init__(self,code,section,days,stime,etime,instructor):
        self.code = code 
        self.section = section 
        self.days = days 
        #changing the code for sunday from SU to U for ease
        if "SU" in self.days:
            self.days = self.days.replace("SU", "U")
        self.SH, self.SM, self.stime = time_to_24(stime)
        self.EH, self.EM, self.etime = time_to_24(etime)
        self.instructor = instructor 


#convert time to 24 hr format and also seperate var for hr and min
def time_to_24(time):
    time_obj = datetime.strptime(time, "%I:%M%p")
    hour = time_obj.hour
    minute = time_obj.minute
    time_24_hour = time_obj.strftime("%H:%M")

    return hour, minute, time_24_hour
#checks if the new_course causes clash in time table
def is_valid(timetable,new_course):
    if len(timetable) == 0:
        return True
    for course in timetable:
        for day in range(len(course.days)):             #to compare all days of course
            for day2 in range(len(new_course.days)):    #with all days of new_course
                if course.days[day] == new_course.days[day2]:   #if days match it then compares time for clash
                    if new_course.stime >= course.stime and new_course.stime <= course.etime:
                        return False

                    if new_course.etime >= course.stime and new_course.etime <= course.etime:
                        return False
    
    return True
#takes input from course_info.txt
def input_data(filepath):
    courses = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('(') and line.endswith(')'):
                line = line[1:-1]
                values = line.split(',')

                if len(values) == 6:
                    code =values[0].strip()
                    section =values[1].strip()
                    days =values[2].strip()
                    stime =values[3].strip()
                    etime =values[4].strip()
                    instructor =values[5].strip()

                    course = Course(code, section, days, stime, etime, instructor)
                    courses.append(course)

    return courses
#processes courses entered by user
def input_list(listpath):
    List = []
    with open(listpath, "r") as file:
        List =  [line.strip() for line in file]

    return List
#
def prod():
    pass

#fetching course info
file_path = 'course_info.txt'
courses = input_data(file_path)

list_path = sys.argv[1]
make_timetable = False      #False: text form of time table | True: screenshots the visaul time table
try:
    if "save" in sys.argv:   #second argument passed is save makes the visual time table 
        make_timetable = True
except:                         #no second argument means just text time table
    pass

#fetching entered courses from file passed in terminal
course_list = input_list(list_path)
num_courses = len(course_list)


combinations_list = []
All_course_section = []

for i in range(num_courses):
    #makes a list of all sections 
    new_list = []
    for course in courses:
        if course.code == course_list[i] and "LEC" in course.section:
            new_list.append(course)

    #add the list to a list of lists of all courses
    All_course_section.append(new_list)

check_var = True

if num_courses == 4:
    for combination in product(All_course_section[0], All_course_section[1],All_course_section[2],All_course_section[3]):
        combinations_list.append(combination)

elif num_courses == 5:
    for combination in product(All_course_section[0], All_course_section[1],All_course_section[2],All_course_section[3],All_course_section[4]):
        combinations_list.append(combination)

elif num_courses == 6:
    for combination in product(All_course_section[0], All_course_section[1],All_course_section[2],All_course_section[3],All_course_section[4],All_course_section[5]):
        combinations_list.append(combination)

elif num_courses == 7:
    for combination in product(All_course_section[0], All_course_section[1],All_course_section[2],All_course_section[3],All_course_section[4],All_course_section[5],All_course_section[6]):
        combinations_list.append(combination)

else:
    print("enter between 4-7 valid course codes")
    check_var = False

if check_var:
    
    print("Following are the possible clash-free time tables for",num_courses,"selected requested courses")
    print("")
    valid_timetable = 0

    for combination in combinations_list:
        timetable = []
        for course in combination:
                if is_valid(timetable,course):
                    timetable.append(course)
        
        for course in timetable:
            if len(timetable) == num_courses and not make_timetable:
                print(course.code,course.section,course.days,course.stime,course.etime , course.instructor)
        
        if len(timetable) == num_courses:
            valid_timetable = valid_timetable+1

        if not make_timetable and len(timetable) == num_courses:
            print("")

        if make_timetable == True and len(timetable) == num_courses:
            name = list_path.split('.')[0]
            util.web_hhandler(timetable,name,valid_timetable)

    if valid_timetable == 0 and not make_timetable:
        print("OPPS: There is no valid timetable for this combination")
