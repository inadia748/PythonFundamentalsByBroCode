text = "Yooo \n This is some text. \n Have a good one"


with open('test.txt', 'w') as file:
    file.write(text)

mytext = '\nThis is extra for appending'

with open('test.txt', 'a') as file:
    file.write(mytext)
