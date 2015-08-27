# https://www.codecademy.com/courses/python-intermediate-en-rCQKw/2/4?curriculum_id=4f89dab3d788890003000096
# need to update to make it simple

def remove_duplicates(x):
    r_x = []
    # copy parameter x due to the requirement
    z = []
    for i in x:
        z.append(i)
    # to sort the list for following compare
    z.sort()
    for i in z :
        if z.count(i) == 1:
            r_x.append(i)
        else:
            r_x.append(i)
            if len(r_x) >1:
                if r_x[len(r_x)-1] == r_x[len(r_x)-2]:
                    r_x.pop()
    return r_x
