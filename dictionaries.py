studentchomu = {'name': 'Zain', 'Age': 20, 'courses': ["Python", "DSA"]}
print(studentchomu)
print(studentchomu.keys())
print(studentchomu.values())
print(studentchomu.items())
print(studentchomu['name'])
print(len(studentchomu['name']))
studentchomu.update({'name': 'Mohmmad'})
print(studentchomu)
del studentchomu['courses']
print(studentchomu)
print(studentchomu.get('phone', 'Not found'))
print(studentchomu.get('Age'))
age = studentchomu.pop('Age')
print(age)
print(studentchomu)

