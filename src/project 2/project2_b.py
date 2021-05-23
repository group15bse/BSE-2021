def open_file():
    while True:
        file = input('Enter input file:')
        try:
            handle = open(file,'r')
            return handle
        except:
            print('File not found!!!')
            continue


def process_file(file_object):
    year = input('Enter year: ')
    income = input('Enter the income level: ')
    if income == '1':
        income = "WB_LI"
    elif income == '2':
        income = "WB_LMI"
    elif income == '3':
        income = "WB_UMI"
    elif income == '4':
        income = "WB_HI"
    else:
        print("Invalid income")

    list = []
    country_list = []
    for line in file_object:
        if year in line[88:92] and income in line[51:57]:
            percent = int(line[59:61].strip())
            list.append(percent)
            #print(line[59:62])
            #print(list)
            country_list.append(line[0:49].strip())
    print('Count of records: ',len(list))
    print('Average percentage: ',round(sum(list)/len(list), 1))
    # highc = max(list)
    # hcountry = None
    # for i in country_list:
    #     pass
    print(max(list))
    print(min(list))
    print('Country with highest percentage: ',max(country_list))
    print('Country with lowest percentage: ',min(country_list))
process_file(open_file())