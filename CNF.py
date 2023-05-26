"""
First take input and slice it into states and
put them into dictionarys
"""
print("Please Enter the States and Terminals seperated by a space:")
tempinput = input().split(" ")
CFG = {}
#taking input and forming the dictionary
while tempinput[0] != "end" :
    CFG[tempinput[0]] = tempinput[1].split("|")
    tempinput = input().split(" " )


#function to elimenata the epsilons from terminals
#should take the terminal, and the State to know what letter to 
# reduce from the string
l = []
def returnNewVals(terminals, key, Tset):
    for terminal in terminals: #for each string in the list
        for i in range (len(terminal)): #for the length of this string MAX
            terminal = terminal.replace(key, "", 1) #replace the character from this string if it exists
            Tset.add(terminal) #add the modified string to the set

    

newTerminals = set()
currentkey = ""
for State in CFG.keys(): #for each state in the dict
    if "e" in CFG[State]: #if it has e in its Transitions
        CFG[State].remove("e")      #remove the epsilon
        for i in CFG[State]:        #add the current states into the set
            newTerminals.add(i)
        returnNewVals(CFG[State], State, newTerminals)     # process the current transtitions
        CFG[State] = newTerminals.copy()                #take a copy of the set to be the new transitions. 
                                                #else, future changes will affect the set of the states
        newTerminals.clear()                    # clear the set to be used for the next State

print(CFG)



        


