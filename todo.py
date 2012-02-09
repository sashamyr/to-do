print 'Hello!'
import sys
from sqlite3 import *
def preparer():
    conn = connect('todo.db')
    curs = conn.cursor()
    try:
        curs.execute('''create table item
            (id integer primary key, scancode text)''')
    except OperationalError, x:
        pass
    starter()

def starter():
    print "MENU\n  1. Create task\n  2. Current tasks\
    \n  3. Delete task\n  4. Quit"
    global chs
    chs = int(raw_input(''))
    choice()

def choice():
    print '\n'
    try:
        if chs == 1:
            writer()
        if chs == 2:
            reader()
        if chs == 3:
            deleter()
        if chs == 4:
            quit()
    except ValueError:
        print 'Oops! Looks like you are naughty one :)'
        sys.exit(None)

def writer():
    conn = connect('todo.db')
    curs = conn.cursor()
    print 'So, print your task: '
    a = raw_input('')
    curs.execute("insert into item values (NULL, ?)", [a])
    conn.commit()
    print "Task saved\n"
    starter()

def reader():
    print "Your tasks are:"
    conn = connect('todo.db')
    curs = conn.cursor()
    curs.execute("select * from item")
    for row in curs:
        print row
    print '\n'
    starter()

def deleter():
    print 'So, here are your current tasks:'
    conn = connect('todo.db')
    curs = conn.cursor()
    curs.execute("select * from item")
    for row in curs:
        print row
    delch = int(raw_input('Type ID of task you want to be deleted\n'))
    curs.execute("DELETE FROM item WHERE id = ?", [delch])
    conn.commit()
    print '\nDeleted successfully\n'
    starter()

def quit():
    print '\nBye!'
    sys.exit()
    
if __name__ == '__main__':
    preparer()