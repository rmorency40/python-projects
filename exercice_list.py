#!/usr/bin/env python3

"""" This function will ask the user to enter the tasks  in his to-do list """

def to_do_list():
    to_do_list = []
    finished = True
    while finished:
        task = input('Enter a task for your to-do list.   Press <enter> when done:  ')
        if len(task) == 0:
            finished = False
        else:
            to_do_list.append(task)
            print('Task added to your list.')

    # Display to-do list .
    print()
    print('Your To-Do list:   ')
    print('-' * 20)
    for task in to_do_list:
        print(task)
        
        


to_do_list()

