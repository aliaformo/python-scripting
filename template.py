names = ['John', 'Jane', 'Bill']
assignments = [2,3,1]
grades=[8,7,6]

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
    

'''Hi John,

This is a reminder that you have 2 assignments left to submit before you can graduate. Your current grade is 8 and can increase to 12 if you submit all assignments before the due date.


Hi Jane,

This is a reminder that you have 3 assignments left to submit before you can graduate. Your current grade is 7 and can increase to 13 if you submit all assignments before the due date.


Hi Bill,

This is a reminder that you have 1 assignments left to submit before you can graduate. Your current grade is 6 and can increase to 8 if you submit all assignments before the due date.'''