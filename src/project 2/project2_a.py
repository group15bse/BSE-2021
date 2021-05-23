try:
    handle = open('measles.txt','r')
    inp = input('Enter a year: ')
    if inp == '' or inp == 'all' or inp == 'ALL':
        pass
    elif int(inp):
        if len(inp) <= 4:
           pass
        else:
            print("Invalid inp length!!!")
            exit()
    else:
        print('Invalid input!!!')

    output = input('Enter a file name for output: ')

    if not '.txt' in output:
        print('File name should be in txt format with .txt extension.')
        exit()
    save = open(output,'w')

    for line in handle:
        if inp in line[88:92]:
            if line[88:92].startswith(inp):
                save.write(line)
        #else:
           #if inp =='' or inp == 'all' or inp =='ALL':
               # save.write(line)


    save.close()
    handle.close()

except:
    print('Error....,Invalid input!!!!')
