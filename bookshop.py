# import mysqlite 
import sqlite3

# create create_table funtion and populate
def create_table():
    try:
        # create variable for db file
        db = sqlite3.connect('ebookstore_db')

        # create variable for db.cursor
        cursor = db.cursor()

        # create variables for table info 
        id1 = 3001
        title1 = 'A Tale of Two Cities'
        author1 = 'Charles Dickens'
        qty1 = 30

        id2 = 3002
        title2 = 'Harry Potter and the Philosopher\'s Stone'
        author2 = 'J.K. Rowling'
        qty2 = 40

        id3 = 3003
        title3 = 'The Lion, the Witch and the Wardrobe'
        author3 = 'C.S. Lewis'
        qty3 = 25

        id4 = 3004
        title4 = 'The Lord of the Rings'
        author4 = 'J.R.R. Tolkien'
        qty4 = 37

        id5 = 3005
        title5 = 'Alice in Wonderland'
        author5 = 'Lewis Carroll'
        qty5 = 12

        # create list
        book_list = [
            (id1, title1, author1, qty1),
            (id2, title2, author2, qty2),
            (id3, title3, author3, qty3),
            (id4, title4, author4, qty4),
            (id5, title5, author5, qty5)
            ]

        print('''--------------------------------------------------------------
                      System starting
--------------------------------------------------------------''')
        # create table id primary key
        cursor.execute('''
        CREATE TABLE books(id INTERGER PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), qty INTERGER)''')
        print('''                       Table created
--------------------------------------------------------------''')

        # execute many insert book_list into table 
        cursor.executemany(''' 
            INSERT INTO books(id, title, author, qty)
            VALUES(?,?,?,?)''',
            book_list)
        
        #commit changes
        db.commit()
    
    # except Exception rollback and raise error
    except Exception as e:
        db.rollback()
        print('''                   Table already created
--------------------------------------------------------------''')

    # finally close db
    finally:
        db.close()

# create enter_book function
def enter_book():
    # try expect to cstch errors
    try:
        # create variable for db file
        db = sqlite3.connect('ebookstore_db')

        # create variable for db.cursor
        cursor = db.cursor()

        # while True until int input with try except to catch ValueError
        while True:
            try:
                # get user input new id
                new_book_id = int(input('''--------------------------------------------------------------
Enter ID:                                               '''))
                break
            except ValueError:
                print('''--------------------------------------------------------------
                    Please enter a number''')
                continue
        # get user input new title
        new_book_title = input('''--------------------------------------------------------------
Enter new book title:                                   ''')
        # get user input new author
        new_book_author = input('''--------------------------------------------------------------
Enter new book author:                                  ''')

        # while True until int input with try except to catch errors
        while True:
            try:
                # get user input qty
                new_book_qty = int(input('''--------------------------------------------------------------
Enter new book quantity:                                '''))
                break
            except ValueError as e:
                print('''--------------------------------------------------------------
                    Please enter a number''')
                continue

        # write new book to table
        cursor.execute('''
            INSERT INTO books(id, title, author, qty)
            VALUES(?,?,?,?)''', (new_book_id, new_book_title, new_book_author, new_book_qty))
        
        # commit changes
        db.commit()        
        print('''--------------------------------------------------------------
                    New book entered
--------------------------------------------------------------''')
    
    except Exception as e:
        db.rollback()
        raise e
    
    # finally close db
    finally:
        db.close()

# create update_book function
def update_book():
    try:
        # create variable for db file
        db = sqlite3.connect('ebookstore_db')

        # create variable for db.cursor
        cursor = db.cursor()

        # while True until int input with try except to catch error
        while True:
            try:
                search_id = int(input('''--------------------------------------------------------------
Please enter the ID of the book to edit:                '''))
                break
            except ValueError:
                print('''--------------------------------------------------------------
                     Please enter a number''')
                continue

        # while True get value to update 
        while True:
            update = input('''--------------------------------------------------------------
Value to update: Title(1)/Author(2)/Qty(3) or Exit(0):  ''').lower()

            # if statement for different choices
            if update == '1':

                edit_info = input('''--------------------------------------------------------------
Enter new title:                                        ''')
                cursor.execute(f'''
                    UPDATE books
                    SET title = ?
                    WHERE id = ?''', (edit_info, search_id))
                db.commit()
                print('''--------------------------------------------------------------
                        Value updated''')

            elif update == '2':
                edit_info = input('''--------------------------------------------------------------
Enter new Author:                                       ''')
                cursor.execute(f'''
                    UPDATE books
                    SET author = ?
                    WHERE id = ?''', (edit_info, search_id))
                db.commit()
                print('''--------------------------------------------------------------
                        Value updated''')

            elif update == '3':
                while True:
                    try:
                        edit_info = int(input('''--------------------------------------------------------------
Enter new Quantity:                                     '''))
                        break

                    except ValueError:
                        print('''--------------------------------------------------------------
                        Please enter a number''')
                        continue
                
                cursor.execute(f'''
                    UPDATE books
                    SET qty = ?
                    WHERE id = ?''', (edit_info, search_id))
                db.commit()
                print('''--------------------------------------------------------------
                        Value updated''')

            elif update == '0':
                print('''--------------------------------------------------------------
                        Update aborted
--------------------------------------------------------------''')
                break

            # else incorrect
            else:
                print('''--------------------------------------------------------------
                Incorrect input, try again''')

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()

# create delete_book function
def delete_book():
    try:
        # create variable for db file
        db = sqlite3.connect('ebookstore_db')

        # create variable for db.cursor
        cursor = db.cursor()

        # while true to check if correct book if not repeat search
        while True:
            # while True until int input with try except to catch errors
            while True:
                try:
                    # get user input id to search
                    search_id = int(input('''--------------------------------------------------------------
Please enter the ID of the book to delete:              '''))
                    break
                except ValueError:
                    print('''--------------------------------------------------------------
                    Please enter a number''')
                    continue

            # show selected book
            print('--------------------------------------------------------------')
            cursor.execute(f'''
                SELECT * FROM books
                WHERE id = ?''', (search_id,))
            # for loop to print rows
            for row in cursor:
                print(f'''
Book:           {row[1]}
Author:         {row[2]}
Qty:            {row[3]}
--------------------------------------------------------------''')
            # correct book confirm
            confirm = input('Is this the book you were looking for? y/n:             ').lower()

            # if yes break else continue
            if confirm == 'y':
                break
            else:
                continue    
    
        # confirm delete
        delete_choice = input('''--------------------------------------------------------------
Delete this book? y/n:                                  ''').lower()

        # if statement to delete or not
        if delete_choice == 'y':
            cursor.execute(f'''
            DELETE FROM books
            WHERE id = ?''', (search_id,))
            db.commit()
            print('''--------------------------------------------------------------
                        Book deleted
--------------------------------------------------------------''')
        
        else:
            print('''--------------------------------------------------------------
                       Delete aborted
--------------------------------------------------------------''')

    except Exception as e:
        db.rollback()
        raise e
    
    finally:
        db.close()

# create search book function
def search_book():
    try:
        # create variable for db file
        db = sqlite3.connect('ebookstore_db')

        # create variable for db.cursor
        cursor = db.cursor()

        # while true get user input which vlue to search
        while True:
            search_choice = input('''--------------------------------------------------------------
Which value do you want to search by:
ID(1)/Title(2)/Author(3)/Qty(4):                        ''').lower()

            # if statement for each value try except for in input
            if search_choice == '1':
                while True:
                    try:
                        search_id = int(input('''--------------------------------------------------------------
Enter ID to search:                                     '''))
                        break
                    except ValueError:
                        print('''--------------------------------------------------------------
                    Please enter a number''')
                        continue

                cursor.execute(f'''
                SELECT * FROM books
                WHERE id = ?''', (search_id,))
                # for loop to print rows
                for row in cursor:
                    print(f'''--------------------------------------------------------------
ID:         {row[0]}
Title:      {row[1]}
Author:     {row[2]}
Qty         {row[3]}
--------------------------------------------------------------''')
                break

            elif search_choice == '2':
                search_title = input('''--------------------------------------------------------------
Enter Title to search:                                  ''')
                cursor.execute(f'''
                SELECT * FROM books
                WHERE title = ?''', (search_title,))
                for row in cursor:
                    print(f'''--------------------------------------------------------------
ID:         {row[0]}
Title:      {row[1]}
Author:     {row[2]}
Qty         {row[3]}
--------------------------------------------------------------''')
                break

            elif search_choice == '3':
                search_author = input('''--------------------------------------------------------------
Enter Author to search:                                 ''')
                cursor.execute(f'''
                SELECT * FROM books
                WHERE author = ?''', (search_author,))
                for row in cursor:
                    print(f'''--------------------------------------------------------------
ID:         {row[0]}
Title:      {row[1]}
Author:     {row[2]}
Qty         {row[3]}
--------------------------------------------------------------''')
                break

            elif search_choice == '4':
                while True:
                    try:
                        search_qty = int(input('''--------------------------------------------------------------
Enter Qty to search:                                '''))
                        break
                    except ValueError:
                        print('''--------------------------------------------------------------
                        Please enter a number''')
                        continue

                cursor.execute(f'''
                SELECT * FROM books
                WHERE qty = ?''', (search_qty,))
                for row in cursor:
                    print(f'''--------------------------------------------------------------
ID:         {row[0]}
Title:      {row[1]}
Author:     {row[2]}
Qty         {row[3]}
--------------------------------------------------------------''')
                break

            # else incorrect input 
            else:
                print('''--------------------------------------------------------------
                Incorrect input please try again''')
                continue

    except Exception as e:
        db.rollback()
        raise e
    
    finally:
        db.close()

# create extra feature show_all
def show_all():
    try:
        # create variable for db file
        db = sqlite3.connect('ebookstore_db')

        # create variable for db.cursor
        cursor = db.cursor()

        # select all from books
        cursor.execute(f'''
            SELECT * FROM books''')
        # for loop to print rows 
        for row in cursor:
            print(f'''--------------------------------------------------------------
ID:             {row[0]}
Book:           {row[1]}
Author:         {row[2]}
Qty:            {row[3]}
--------------------------------------------------------------''')
    
    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()