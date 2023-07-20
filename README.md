# Schedule-generator
 This three-part project generates clash-free timetables from user provided course codes.
 
## Part 1: Fetching & Cleaning Course Info
 We will fetch, clean, and process course information from the provided schedule in this part. We'll identify the source of the data, read it into our program using appropriate pdf tools & libraries, and handle any inconsistencies or missing values. Then, we'll organize the data for easy manipulation. 

## Part 2: Processing data & Producing All valid Combinations of Timetables
 Firstly, we'll create functions to handle user input of course codes, ensuring a user-friendly interface. Once we have clean and processed course information, we'll create a clash detection method to check for overlapping course timings. Then proceed to generate all possible combinations of timetables without any clashes. These combinations will be presented in a text format, providing users with various options for their schedules.  

## Part 3: Producing a Visual Timetable Using Web Automation (Selenium)
 In the final part, we'll take the valid timetable combinations and produce visual representations of the schedules. To achieve this, we'll utilize web automation through Selenium, a powerful tool for web scraping and interaction. The program will automatically generate & save visual timetables on a web page, allowing users to see their clash-free schedule options in an easy-to-read format.



 # Missing:
 1. **Inconsistencies & missing values**: The code is not able to generate text for all courses as the pdf has some minor faults. 
 2. **Missing variable supp**: Due to time shortage, I ditched some essential variables, e.g., Course title.
 3. **Course conditioning**: Some additional checks on courses with 'LAB' and  'REC' components in addition to 'LEC 'Still needs to be implemented.
 4. **Course limit**: A user can only add 4-7 courses right now. Adding more or less is not an issue, but I wanted to find a better way of handling this before improving the limit constraint.
 5. **More input options**: Adding more input options like restricting sections based on instructor
 6. **plug and play**: once cloned, there needs to be a few changes needed to make sure path for all the drivers and files are properly defined
   
# Files:
1. **Schedule.pdf**: Contains the pdf of courses' timeslots provided by LUMS for **FALL 23'**.
2. **backtrack.py**: Contains the code for **part 2**.
3. **chromedriver**: Is the driver needed by Selenium to function with google chrome on your machine. Please download the version that is compatible with your machine and the Chrome version installed on it.
4. **course_info.txt**: Contains the processed course details in the form of tuples after the **fetch_info.py** is executed on the pdf **schedule.pdf** 
5. **fetch_info.txt**: Contains the code for **part 1**
6. **input.txt**: users enter the course code in this file
7. **util.py**: Contains the code for **part 3**


**NOTE**: Feel free to suggest improvements. You can always mail me at arafayb@gmail.com and make a pull request
