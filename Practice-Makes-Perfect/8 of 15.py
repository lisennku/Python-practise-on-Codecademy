# https://www.codecademy.com/courses/python-intermediate-en-rCQKw/1/2?curriculum_id=4f89dab3d788890003000096
# create a function to delete a vowel charactor from the parameter

def anti_vowel(x):
    vowel = ['a','A','e','E','i','I','o','O','u','U']
    xl = []
    for i in x:
        if i not in vowel:
            xl.append(i)
            rem = ''.join(xl)
    return rem
