fs = open('students.txt', 'r', encoding ='utf-8')

students = []
for student in fs:
    s = student.split(';')
    id = int(s[0])
    name = s[1]
    var = int(s[2])
    group = int(s[3])
    students.append({'id': id, 'full_name': name, 'var': var, 'group': group})
 
for student in students: 
    print(student)
fs.close()

