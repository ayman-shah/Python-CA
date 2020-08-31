#Student lists
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]
students_absent = ["iliana", "olympia", "juan", "kelsey"]

#Print out students present:
for student in students_present:
  print(student)


#Print number of students present
print("Total students present: {}.".format(len(students_present)))

#Print out students absent
for student in students_absent:
  print(student)


#Print number of students absent
print("Total students absent: {}.".format(len(students_absent)))
