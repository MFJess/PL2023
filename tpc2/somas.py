sum = 0
on = False
digits = ['0','1','2','3','4','5','6','7','8','9']
controller = ""
    

string = input('type something\n')
for char in string:
    if (char == '='):
        print('sum equals ' + str(sum))

    elif (char.lower() in "ofn"):
        controller = controller + str(char.lower())
        if("on" in controller):
            on = True
            print("now on")
            controller = ""
        if("off" in controller):
            on = False
            print("now off")
            controller = ""

    elif (on and char in digits):
        sum += int(char)
        print("somei " + char)
        
            
        

# test = 182on5=0off1701=2on103=