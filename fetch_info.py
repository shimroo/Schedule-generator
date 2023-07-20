import tabula
import pandas as pd

def extract_tables_from_pdf(file_path, pages):
    tables = tabula.read_pdf(file_path, pages=pages, multiple_tables=True)
    
    return tables

def write_tuples_to_file(tuples, file_path):
    with open(file_path, 'w') as file:
        for t in tuples:
            line = ', '.join(str(item) for item in t)  # Convert tuple to comma-separated string
            file.write(line + '\n')


def process_tables(tables):
    courses = []

    last_Title = "hehe" 
    last_code = "hehe" 

    for table in tables:
        # Filter relevant columns
        relevant_columns = table[['Course Code','Course Title', 'Section','Days','Start Time' ,'End Time' ,'Instructor']]
        # Extract course information
        for _, row in relevant_columns.iterrows():
            course_code = row['Course Code']
            course_Title = row['Course Title']
            Section = row['Section']
            Days = row['Days']
            Start_Time = row['Start Time']
            End_Time = row['End Time']
            Instructor = row['Instructor']

            # Process the course information as needed
            # You can store it in a data structure or perform further operations here
                
            if not pd.notna(course_code):
                course_code = last_code
            
            if pd.notna(Days) and pd.notna(Start_Time) and pd.notna(End_Time): 
                courses.append((course_code, Section, Days, Start_Time, End_Time, Instructor))
                last_code = course_code 

            #diagnoses             
            # print(course_code)

    return courses

#5,8
content = extract_tables_from_pdf('Schedule.pdf','1-4,6-7,9-18')
# content = extract_tables_from_pdf('Schedule.pdf','1-18')
# content = extract_tables_from_pdf('Schedule.pdf','5')

courses = process_tables(content)

# Final_courses.append(courses)
# Final_content.append(content)



for course in courses:
    print(course)


print(len(courses))

file_path = 'output.txt'
write_tuples_to_file(courses, file_path)
