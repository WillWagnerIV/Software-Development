clubMembers = {   
    '523-8943' : {'Name': 'Ariel Gonzalez', 'Address': '3 Wisteria Lane', 'Sex': 'M'},
    '112-7832' : {'Name': 'Anna-Marie Smith', 'Address': '221B Baker Street', 'Sex': 'F', 'Role': 'Chair'}
}

while True:
    phNumber = input('Please enter phone number (0 to Quit): ')
    if phNumber == "0":
        break
    else:
        print ("Details for person with phone number " + phNumber + ':')
        for x,y in clubMembers[phNumber].items():
            print (x + ": "+ y )
        print ()


