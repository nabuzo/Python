#################################################################################
# Author: Nicole Abuzo                                                          #
# Date : 11 / 20 / 16                                                           #
# Purpose: Understanding the importance of strings by creating a gibberish game #
#################################################################################

print("Welcome to Nicole's Gibbersih Game!")
print('')

# Initializing important input
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
wildCard = '*'


while True:
    syl = input("Please enter your 1st Gibberish syllable (add '*' if you want a vowel substitution):")
    syl_2 = input("Please enter your 2nd Gibberish syllable ('*' for vowel substitution):")
    user = input("Enter a word you want to be translated\n--------> ")
    
    copy = ''
    p_item = 'd'
    v_item = 'd'
    z = '*'
    for i in range(len(user)):
        item = user[i]
        if item in vowels and p_item not in vowels and v_item not in vowels and wildCard not in syl:
            replace = user.replace(user, syl + item)
            copy = copy + replace
            p_item = item
            v_item = item
            z = item
        elif p_item in vowels:
            copy = copy + item
            p_item = item
        elif v_item in vowels and item in vowels and wildCard in syl_2:
            syl_s2 = item + syl_2[1:]
            replace = user.replace(user, syl_s2 + item)
            copy = copy + replace
            p_item = item
        elif item in vowels and v_item in vowels and wildCard not in syl_2:
            replace = user.replace(user, syl_2 + item)
            copy = copy + replace
            p_item = item
        elif wildCard in syl and item in vowels:
            syl_s = item + syl [1:]
            replace = user.replace(user, syl_s + item)
            copy = copy + replace
            p_item = item
            v_item = item
        else:
            copy = copy + item
            p_item = item

    print("And your final word is...\n", copy, ':)')
    print('')
    replay = input("Play again? (y/n): ")
    if replay == 'y' or replay == "yes":
        continue
    elif replay == 'n' or replay == "no":
        print("Thank you for playing!")
        break
    elif replay != 'y' or replay != 'n' or replay != "yes" or replay != "no":
        print("Enter 'y' to play again or 'n' to quit")
        replay = input("Play again? (y/n):")

    

