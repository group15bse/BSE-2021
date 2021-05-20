handle = open('measles.txt','r')
inp = input('Enter a year: ')
output = input('Enter a file name for output: ')
if not '.txt' in output:
    print('File name should be in txt format with .txt ext.')
    exit()
save = open(output,'w')
for line in handle:
    if inp in line[88:92]:
        if line[88:92].startswith(inp):
            save.write(line)
    else:
        if inp =='' or inp == 'all' or inp =='ALL':
            save.write(line)
handle.close()

