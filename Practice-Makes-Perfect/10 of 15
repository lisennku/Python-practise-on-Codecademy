# https://www.codecademy.com/courses/python-intermediate-en-rCQKw/1/4?curriculum_id=4f89dab3d788890003000096
# repalce with asterisks

def censor(text,word):
    ast = ["*"] * len(word)
    ast = ''.join(ast)
    replace = []
    data = text.split(" ")
    for index,item in enumerate(data):
        if item == word:
            replace.insert(index,ast)
        else:
            replace.insert(index,item)
    res = ' '.join(replace)
    return res
  
