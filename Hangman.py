# -*- coding: utf-8 -*-

import random
import string

WORDLIST_FILENAME = "words.txt"
def load_words():    
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def choose_word(wordlist):  
    return random.choice(wordlist)
wordlist = load_words()
def is_word_guessed(secret_word, letters_guessed):   
    for char in secret_word:
        if char not in letters_guessed:
            return False
        return True
def get_guessed_word(secret_word, letters_guessed):   
    secret_print = ''
    for char in secret_word:
        if char in letters_guessed:
            secret_print += char
        else:
            secret_print += '_ '            
    return secret_print        
def get_available_letters(letters_guessed):    
    available_letters = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char         
    return available_letters                
def hangman(secret_word):   
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+ str(len(secret_word))+" letters long")
    print("------------------")
    num = 6
    lettersum=''
    warnings = 3
    print ("You have "+str(warnings)+" left")
    vowel = 'a'+'e'+'i'+'o'+'u'
    while num > 0:        
        print("You have "+ str(num) +" guesses left")
        print("Available letters : "+get_available_letters(lettersum))
        letter = input("Please guess a letter : ")      
        if not str.isalpha(letter):
            warnings -= 1
            print("Oops! That is not a valid letter. You have "+str(warnings)+" left: "+get_guessed_word(secret_word, lettersum))
            if warnings==0:
                num -= 1
                warnings = 3
            continue
        str.lower(letter)
        if letter in lettersum:
            warnings -= 1
            print("Oops! You have already guessed that letter. You have "+str(warnings)+" left:"+get_guessed_word(secret_word, lettersum))
            if warnings==0:
                num -= 1
                warnings = 3
            continue        
        lettersum += letter
        if letter in secret_word:
            print ("Good guess : "+get_guessed_word(secret_word, lettersum))           
        else: 
          if letter in vowel:           
            print ("Oops! That letter is not in my word : "+get_guessed_word(secret_word, lettersum))            
            num -= 2
          else:                 
            print ("Oops! That letter is not in my word : "+get_guessed_word(secret_word, lettersum))            
            num -= 1
        print("------------------")       
        if get_guessed_word(secret_word, lettersum)==secret_word:
            print('Congratulations, you won!')
            total_score = num*(6-num)
            print('Your total score is : '+str(total_score))
            break
    if num==0:
      print('Oops! You lost.')
      print ('The secret word is : '+secret_word)       


if __name__ == "__main__":
   
    secret_word = choose_word(wordlist)
    hangman(secret_word)

