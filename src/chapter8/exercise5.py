mail_box = input('Enter a file name: ')
file = open(mail_box, 'r')
count = 0
for line in file:
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count += 1
print('There are', count, 'lines in the file with From as the first word')
