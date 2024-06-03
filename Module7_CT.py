# Name: J. Lewis

# The requested dictionaries:
course_rooms = {"CSC101": 3004, "CSC102": 4501, "CSC103": 6755, "NET110": 1244, "COM241": 1411}
course_instructors = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich", "NET110": "Burke", "COM241": "Lee"}
course_times = {"CSC101": "8:00 AM", "CSC102": "9:00 AM", "CSC103": "10:00 AM", "NET110": "11:00 AM", "COM241": "1:00 PM"}

# My variant of the solution:
course_information = {"CSC101": (3004, "Haynes", "8:00 AM"),
                      "CSC102": (4501, "Alvarado", "9:00 AM"),
                      "CSC103": (6755, "Rich", "10:00 AM"),
                      "NET110": (1244, "Burke", "11:00 AM"),
                      "COM241": (1411, "Lee", "1:00 AM")}

# User Input:
selection = input("Please input a course designation to view it's information, such as 'CSC101': ")
print(f"{selection} meets at {course_information[selection][2]} in room {course_information[selection][0]}.")
print(f"This course is taught by Professor {course_information[selection][1]}-be sure to attend their office hours!")
