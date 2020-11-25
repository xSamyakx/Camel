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
# def match_with_gaps(my_word, other_word):
#     my_word_wgaps=''
#     letters_guessed2=[]
#     for char in my_word:
#         if char!=' ':
#           my_word_wgaps +=char
          
#         if char.isalpha():
#             letters_guessed2.append(char)
#     if len(my_word_wgaps) != len(other_word):
#         return False
#     for i in range(len(my_word_wgaps)):
#         current_letter=my_word_wgaps(i)
#         other_letter = other_word(i)
#         if current_letter.isalpha():
#             has_same= current_letter==other_letter
#             if not has_same:
#                 return False
#         else:
#             if current_letter=='_' and other_letter in letters_guessed2:
#                 return False
#     return True        
# def show_possible_matches(my_word):  
#     matched_words = []
#     for word in wordlist:
#         if match_with_gaps(my_word, word):
#             matched_words.append(word)

#     if len(matched_words) > 0:
#         for word in matched_words:
#             print(word, end=' ')
#         print()
#     else:
#         print('No matches found')
   
# def hangman_with_hints(secret_word):
 
#     print("Welcome to the game Hangman!")
#     print("I am thinking of a word that is "+ str(len(secret_word))+" letters long")
#     print("------------------")
#     num = 10
#     lettersum=''
#     warnings = 3
#     print ("You have "+str(warnings)+" warnings left")
#     vowel = 'a'+'e'+'i'+'o'+'u'

#     while num > 0:
        
#        print("You have "+ str(num) +" guesses left")
#        print("Available letters : "+get_available_letters(lettersum))
#        letter = input("Please guess a letter : ")
#        if letter =='*':
#         print ('Possible matches are:')
#         show_possible_matches(get_guessed_word(secret_word, lettersum))
      
#        elif not str.isalpha(letter):
#            warnings -= 1
#            print("Oops! That is not a valid letter. You have "+str(warnings)+" left: "+get_guessed_word(secret_word, lettersum))
#            if warnings==0:
#                num -= 1
#                warnings = 3
#            continue
#        str.lower(letter)
#        if letter in lettersum:
#            warnings -= 1
#            print("Oops! You have already guessed that letter. You have "+str(warnings)+" left:"+get_guessed_word(secret_word, lettersum))
#            if warnings==0:
#                num -= 1
#                warnings = 3
#            continue
        
#        lettersum += letter
#        if letter in secret_word:
#            print ("Good guess : "+get_guessed_word(secret_word, lettersum))
           
#        else: 
#           if letter in vowel:          
#             print ("Oops! That letter is not in my word : "+get_guessed_word(secret_word, lettersum))            
#             num -= 2
#           else:                
#             print ("Oops! That letter is not in my word : "+get_guessed_word(secret_word, lettersum))            
#             num -= 1                       
#        print("------------------")       
#        if get_guessed_word(secret_word, lettersum)==secret_word:
#            print('Congratulations, you won!')
#            total_score = num*(6-num)
#            print('Your total score is : '+str(total_score))
#            break
#     if num<=0:
#      print('Oops! You lost.')
#      print ('The secret word is : '+secret_word) 

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
 # total_words = []
    # for word in wordlist:
    #     if len(word)==len(my_word):
    #         for x in range (len(my_word)):
    #             if my_word(x)=='_'or my_word(x)==' ':
    #                 continue
    #             if my_word(x)!=word(x):
    #                 break
    #             total_words.append(word)
    # if len(total_words)>0:
    #     for word in total_words:
    #         print(word, end=' ')
    #     print()
    # else:
    #     print("No matches found")
