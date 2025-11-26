#start time 14 : 35
contacts = {


}

#main
def main_menu():
    print()
    print("""--- Personal Data Manager ---
          
    1. Add a new contact
    2. View all contacts
    3. Edit a contact
    4. Delete a contact
    5. Save and Quit """)
    print()

    try:
     print()
     choice = int(input('Enter your choice:'))
     print()
     return choice
    
    except ValueError : 
        print()
        print('---Invalid choice---')
        print()
        return 0
   
    



#adding
def adding_new_contact():
    new_name = input('Enter name:')
    new_phone = input('Enter phn no:')
    new_email = input('Enter email id:')
        
    key = 0
    for i in contacts.keys():
            key = i

    contacts[key+1] = {'name':new_name,'phone': new_phone,'email':new_email}
    print()
    print(f'---Contact Added {new_name} ---')
    print()
  


#view

def view_contact():

    print('---Contacts---')
    print()
    for key,value in contacts.items():
         name = value.get('name')
         phone = value.get('phone')
         email = value.get('email')
         print(f' Contact no.{key} | name:{name} | phone:{phone} | email:{email}')
         print()

         


def edit_contact():
     contact_name_to_edit = input('Enter the contact name to edit:')
     main_key_of_edit = 0
     found = False

     for key,value in contacts.items():
          
          #gets name,phone,email (value)
          for i in value.values():    
               
               if i == contact_name_to_edit:
                 found = True
                 main_key_of_edit = key
      
               else: found = False
     if main_key_of_edit != 0:
        edited_name = input('Enter name:')
        edited_phone = input('Enter phn no:')
        edited_email = input('Enter email id:')
        contacts[main_key_of_edit] = {'name':edited_name,'phone': edited_phone,'email':edited_email}
        print()
        print(f'---Contact edited {edited_name} ---')
        print()


     else: 
        print()
        print(f'---No contacts found {contact_name_to_edit}---')
        print()
        
                    
def delete_contact():
     contact_name_to_delete = input('Enter the contact name to delete:')
     main_key_of_delete = 0
     found = False

     for key,value in contacts.items():
          
          #gets name,phone,email (value)
          for i in value.values():    
               
               if i == contact_name_to_delete:
                 found = True
                 main_key_of_delete = key
      
               else: found = False


     try:
      del contacts[main_key_of_delete]
      print()
      print(f'---Contact deleted {contact_name_to_delete} ---')
      print()
     except KeyError :
         print()
         print(f'--Contacts not found {contact_name_to_delete}--')
         print()
    


while True:

  choice = (main_menu())


  if choice == 1:
      adding_new_contact()  

  elif choice == 2:
      view_contact()

  elif choice == 3:
      edit_contact()

  elif choice == 4:
      delete_contact()

  elif choice == 5:
      break
  
#end time 16:41


      
    



