sum = 0
on = True
digits = ['0','1','2','3','4','5','6','7','8','9']
controller = ""

def test_off():
    if ("off" in controller.lower()):
        on = False

def test_on():
    if("on" in controller.lower()):
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

    

string = input('type something\n')
for char in string:
    if (char == '='):
            print('sum equals ' + str(sum))

    elif (char.lower() in "ofn"):
            controller + char
            print("antes" + controller)
            switch()     
            print("depois" + controller)

    elif (on and char in digits):
        sum += int(char)
        
            
        

# test = 182on5=0off1701=2On103