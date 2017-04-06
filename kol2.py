import json


def add_classes(classes, name_of_class):
    if(name_of_class not in classes.keys()):
        classes.update({name_of_class:[]})
    else:
        print "This class already exists"

def add_student_to_class(classes, name_of_class, name_of_student):
    student = {}
    if (type(name_of_student) == str):
        student.update({name_of_student: []})
    if (name_of_class not in classes.keys()):
        print "The class doesn't exist, you must add the class before"
    else:
        exist=False
        for temp_student in classes[name_of_class]:
            if(name_of_student in temp_student.keys()):
                exist=True
                break
        if(exist == True):
            print "This student already exists"
        else:
            classes[name_of_class].append(student)

def add_grade_to_student(classes, name_of_class, name_of_student, grade_of_student):
    if (name_of_class not in classes.keys()):
        print "The class doesn't exist, you can\'t add the grade"
    else:
        exist=False
        for temp_student in classes[name_of_class]:
            if(name_of_student in temp_student.keys()):
                exist=True
                temp_student[name_of_student].append(grade_of_student)
                break
        if(exist == False):
            print "The student doesn't exist in this class"

def del_classes(classes, name_of_class):
    if (name_of_class in classes.keys()):
        del(classes[name_of_class])
        print "The class "+name_of_class+" has been deleted"
    else:
        print "This class doesn't exists"

def del_student_to_class(classes, name_of_class, name_of_student):
    if (name_of_class not in classes.keys()):
        print "The class doesn't exist"
    else:
        exist=False
        for temp_student in classes[name_of_class]:
            if(name_of_student in temp_student.keys()):
                exist=True
                classes[name_of_class].remove(temp_student)
                break
        if(exist == True):
            print "The student "+name_of_student+" has been deleted"
        else:
            print "The student doesn't exist in this class"

def average_student_in_one_class(classes, name_of_class, name_of_student):
    average = 0.0
    if (name_of_class not in classes.keys()):
        print 'The class doesn\'t exist'
    else:
        exist=False
        for temp_student in classes[name_of_class]:
            if(name_of_student in temp_student.keys()):
                exist=True
                sum=0.0
                for grade in temp_student[name_of_student]:
                    sum+= grade
                average = sum/len(temp_student[name_of_student])
                break
        if(exist == False):
            print "The student doesn't exist in this class"
    return average

def average_student_in_all_class(classes, name_of_student):
    average = 0.0
    exist = False
    count = 0.0
    sum = 0.0
    for temp_class in classes.keys():
        for temp_student in classes[temp_class]:
            if (name_of_student in temp_student.keys()):
                exist = True
                for grade in temp_student[name_of_student]:
                    sum += grade
                    count += 1
                break
    if(count == 0):
        print "No grade for "+ str(name_of_student)
    else:
        average = sum / count

    if (exist == False):
            print "The student doesn't exist in any class"
    return average

def update_file_class(all_class, name_file="test.txt"):
    output_file = open(str(name_file), "w")
    json.dump(all_class,output_file)
    output_file.close()
    print "Written file"

def read_file_class(name_file="test.txt"):
    input_file = open(str(name_file),"r+")
    all_class = json.load(input_file)
    input_file.close()
    print "Read file"
    return all_class




classes = {}

#add class
add_classes(classes,"python")
add_classes(classes,"pattern")
add_classes(classes,"web app")
print classes
# {'python': [], 'pattern': [], 'web app': []}


#add student to class
add_student_to_class(classes,"python","giulio")
add_student_to_class(classes,"python","merkel")
add_student_to_class(classes,"pattern","merkel")
add_student_to_class(classes, "pattern","renzi")
print classes
# {'python': [{'giulio': []}, {'merkel': []}], 'pattern': [{'merkel': []}, {'renzi': []}], 'web app': []}

#add grade to student
add_grade_to_student(classes, "python","merkel",2)
add_grade_to_student(classes, "python","merkel",3)
add_grade_to_student(classes, "python","giulio",5)
add_grade_to_student(classes, "python","giulio",4.5)
add_grade_to_student(classes, "pattern","merkel",4)
add_grade_to_student(classes, "pattern","merkel",3)
print classes
# {'python': [{'giulio': [5, 4.5]}, {'merkel': [2, 3]}], 'pattern': [{'merkel': [4, 3]}, {'renzi': []}], 'web app': []}

#average grade student in one class
print "Average grade of giulio in python: " + str(average_student_in_one_class(classes, "python", "giulio"))
print "Average grade of merkel in python: " + str(average_student_in_one_class(classes, "python", "merkel"))
# Average grade of giulio in python: 4.75
# Average grade of merkel in python: 2.5

#average grade student in all class
print "Average grade of merkel in all classes: "+ str(average_student_in_all_class(classes, "merkel"))
# Average grade of merkel in all classes: 3.0

#delete classes
del_classes(classes,"web app")
print classes
# The class web app has been deleted
# {'python': [{'giulio': [5, 4.5]}, {'merkel': [2, 3]}], 'pattern': [{'merkel': [4, 3]}, {'renzi': []}]}


#delete student to class
del_student_to_class(classes, "pattern", "renzi")
print classes
# The student renzi has been deleted
# {'python': [{'giulio': [5, 4.5]}, {'merkel': [2, 3]}], 'pattern': [{'merkel': [4, 3]}]}

#Write the dictionary in the file
update_file_class(classes,"all_classes_agh.txt")
#Written file

#Read file
classes_after_read_file = read_file_class("all_classes_agh.txt")
print classes_after_read_file
# Read file
# {u'python': [{u'giulio': [5, 4.5]}, {u'merkel': [2, 3]}], u'pattern': [{u'merkel': [4, 3]}]}

print "Average grade of merkel in all classes: "+ str(average_student_in_all_class(classes, "merkel"))
# Average grade of merkel in all classes: 3.0

# control on class or student that doesn't exist
print "Average grade of giulio in sandwich: " + str(average_student_in_one_class(classes, "sandwich", "giulio"))
print "Average grade of renzi in all classes: "+ str(average_student_in_all_class(classes, "renzi"))
# The class doesn't exist
# Average grade of giulio in sandwich: 0.0
# No grade for renzi
# The student doesn't exist in any class
# Average grade of renzi in all classes: 0.0
