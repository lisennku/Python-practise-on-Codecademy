# https://www.codecademy.com/courses/python-intermediate-en-rCQKw/1/1?curriculum_id=4f89dab3d788890003000096
# create a reverse function

def reverse(x):
    l = len(x)
    r_x = ''
    for i in range(l):
        r_x = r_x + x[l - 1 - i]
    return r_x
reverse('asdfa')
