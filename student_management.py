import random

student = []

def delete_student():
    if student != []:
     while True:
        try:
         student_roll = int(input('Enter students roll no:'))
         break
        except ValueError: print('Please enter a valid roll no!')

     for i in student:
        remove = False
        if student_roll == i.get('Roll_no'):
            student.remove(i)
            print(f'Student of roll no({student_roll}) removed!✅')
            remove = True
     if remove == False:
        print(f'Student of roll no({student_roll}) not found⁉️')
    else: print('No students for now!')
   
    

        
def view_all_students():
    if student == []:
        print('No students for now!')
    else:  
        print('--Detail of students--')
    
        for i in student:
          print()
          print(i)

   
       

def student_add(a='',b='',c='',append=True,index='',roll=''):
    student_name= input(f'Enter students name {a}:')

    while True:
       try:
          student_age= int(input(f'Enter students age{b}:'))
          break
       except ValueError: print('Please enter a valid age')
    
    while True:
       try:
          student_grades= (input(f'Enter students grades with space{c}:')).strip().split(' ')
          student_grade_number = []

          for i in student_grades:

            grade = int(i)
            student_grade_number.append(grade)

          break
       except ValueError: print('Please enter a valid grade with proper space!')
    

        
    if append == True:
        new_roll = random.randint(1000,2000)      
        details = {
            'Roll_no':new_roll,
            'Name':student_name,
            'Age':student_age,
            'Grades':student_grade_number
        }
        student.append(details)

        print()
        print(f'Student added roll no:{new_roll}✅')
        print()
    if append == False:
       

        student[index] = {
            'Roll_no':roll,
            'Name':student_name,
            'Age':student_age,
            'Grades':student_grade_number
        }

def student_search():
    try:
        search_roll = int(input('Enter roll no:'))
        found = False
        for i in student:
            if search_roll in i.values():
                index = (student.index(i))
                print()
                print(f'Student found!✅ {student[index]} ')
                print()
                found = True
        if found == False:print('Student not found!')
    except ValueError: print('Please enter a valid roll no!⁉️')

def update_student():
    try:
        search_roll = int(input('Roll no of student to update:'))
        found = False
        for i in student:
            if search_roll in i.values():
                
                index = (student.index(i))
                # new_name = input(f'Enter new name{i.get('Name')}')
                # new_age = input(f'Enter new age{i.get('age')}')
                # new_grade = input(f'Enter new grade{i.get('age')}')
                print()
                student_add(f'({i.get('Name')})',f'({i.get('Age')})',f'({i.get('Grades')})',False,student.index(i),search_roll)
                print()
                print("Student's detail sucessfully updated✅")
                
                found = True
        if found == False:print('Student not found!')
    except ValueError: print('Please enter a valid roll no!⁉️')

def show_statistics():
    for i in student:
        total = sum(i.get('Grades'))
        count = len(i.get('Grades'))
        average = total/count

        print(f'{i.get('Name')} - Average grade: {average}')
        
def main_menu():
    print()
    print('--- Student Management System ---\n1. Add Student\n2. View All Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Show Statistics\n7. Exit')
    print()
    while True:
     try:
      print()
      choice = int(input('Enter your choice:'))
      print()
      break
     except ValueError:
         print()
         print('Please enter a valid option')
         print()
    return choice

while True:
    choice = main_menu()
    if choice == 1:
        student_add()
    elif choice == 2:
        view_all_students()
    elif choice == 3:
        student_search()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        show_statistics()
    elif choice == 7:
        print('Thank you,👋')
        break
    else : print('Please enter option from 1-7!')
    


