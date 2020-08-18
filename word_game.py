#!/usr/bin/env python3

""" This function will create  a word game and display the history

# Ask the user to enter noun,verb and adjective
   
def enter_info(noun,verb,adjective):
    noun_f = input('Enter a noun: ')
    verb_f = input('Enter a verb: ')
    adjective_f = input('Enter an adjective: ')
    
   

# This function will display the  result of the history

def display_history():
    print('{} {} {}.'.format(noun_f,verb_f,adjective_f))


enter_info('noun', 'verb', 'adjective')
display_history() """



def get_word(word_type):
    """Get a word from a user  and return that word."""
    

    # The lower() function converts the the string to the lowercase before testing it
    

    if word_type.lower() == 'adjective':
       # Use 'an' in front of 'adjective'
       a_or_an = 'an'
    else:
        # Otherwise,use 'a' in front of 'noun' or 'verb'
        a_or_an = 'a'
    return input('Enter a word that is {0} {1}: '.format(a_or_an,  word_type))

def fill_in_the_blanks(noun, verb, adjective):
    """Fills in the blanks  an returns  a complete history"""

    # The \ lets the string continue on the next line to make each code easier to read
    story = " In this course you will learn how to {1}. "\
            " it's so easy even a {0} can do it. " \
            "Trust me,it wil be very {2}.".format(noun,verb,adjective)
    return story
def display_story(story):
    """Displays a story."""
    print()
    print('Here is the story created . Enjoy !')
    print()
    print(story)


def create_story():
    """Creates a story by capturing the input and displaying a finished story . """
    noun = get_word('noun')
    verb = get_word('verb')
    adjective = get_word('adjective')

    the_story = fill_in_the_blanks(noun, verb, adjective)
    display_story(the_story)

create_story()                        

                         
    
