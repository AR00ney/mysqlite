# import bookshop file
import bookshop

# call create table
bookshop.create_table()

print('''==============================================================
            Welcome to the book management system''')

# while True
while True:  
    # get user input .lower 
    menu = input('''==============================================================
                  Please choose an option
==============================================================
                       Enter book(1)
                       Update book(2)
                       Delete book(3)
                       Search book(4)
                      Show all books(5)
                           Exit(0)
==============================================================                           
:                               ''').lower()
    # if else statement to call required fuction from bookshop
    if menu == '1':
        bookshop.enter_book()
        continue
    elif menu == '2':
        bookshop.update_book()
        continue
    elif menu == '3':
        bookshop.delete_book()
        continue
    elif menu == '4':
        bookshop.search_book()
        continue
    elif menu == '5':
        bookshop.show_all()
        continue
    # exit system
    elif menu == '0':
        print('''==============================================================
                          Goodbye!!
==============================================================''')
        break
    # else incorrect try again.
    else:
        print('''==============================================================
                Incorrect input please try again''')
        continue