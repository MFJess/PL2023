sum = 0
on = True
digits = ['0','1','2','3','4','5','6','7','8','9']
offoptions = ["Off", "OFf", "OFF", "OfF", "oFF", "oFf", "off", "ofF"]
onoptions = ["ON", "on", "On", "oN"]
controller = ""

def test_off():
    for word in offoptions:
        if (word in controller):
            on = False

def test_on():
    for word in onoptions:
        if(word in controller):
             on = True

def turn_off():
    on = False
    controller = ""
    print('sum is now off')

def turn_on():
    on = True
    controller = ""
    print('sum is now on')

def switch():
    if(on and test_off):
        turn_off()
    elif(not on and test_on):
        turn_on()

    


while True:
    string = input('type something\n')
    for char in string:
        if (char == '='):
             print('sum equals ' + str(sum))

        elif (char == 'o' or char == 'O' or char == 'F' or char == 'f' or char == 'n' or char == 'N'):
             controller += char
             switch()     

        elif (on and char in digits):
            sum += int(char)
        
            
        

# test = 182on5=0off1701=2On103