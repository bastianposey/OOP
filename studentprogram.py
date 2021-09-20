import studentclass as sc

studentid = 1001
name = 'John'
dob = '1/1/2000'
classification = 'Junior'

john = sc.Student(studentid, name, dob, classification)

john.calc_age()
john.register()

print("Student age is:", john.get_age())

print("Student can register", john.get_register())
