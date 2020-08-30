students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]
students_absent = ["iliana", "olympia", "juan", "kelsey"]

print("There are {} students present today and {} students absent".format(len(students_present), len(students_absent)))

student = input("Enter a name to find out if the student is present or absent: ").strip().lower()

if student in students_present:
  print("{} is present today.".format(student.title()))
elif student in students_absent:
  print("{} is absent today.".format(student.title()))
else:
  print("Sorry, no student called {} exists!".format(student.title()))
