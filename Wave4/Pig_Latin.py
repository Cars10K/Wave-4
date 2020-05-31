Ay = "ay"
Way = "way"
Consonant = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z')
Vowel = ('A','E','I','O','U')
pig_latin_string = ""
user_sentence = input('Please enter a word or sentence to translate into Pig Latin: ')
words = user_sentence.split()
for user_word in words:
    print(user_word)
    first_letter = user_word[0]
    first_letter = str(first_letter)
    first_letter=first_letter.upper()
    
    if first_letter in Consonant:
        length_of_word = len(user_word)
        remove_first_letter = user_word[1:length_of_word]
        pig_latin = remove_first_letter + first_letter + Ay
        pig_latin_string = pig_latin_string + " " + pig_latin
    elif first_letter in Vowel:
        pig_latin = user_word + Way
        pig_latin_string = pig_latin_string + " " + pig_latin
    else:
        print('Unable to define what that word is')
    
print(pig_latin_string)