

# import list of 5 letter words I pulled from a dictionary
f = open(r"C:\Users\benja\OneDrive\Desktop\TRAINING\WORDLE/wordlist_s.csv", "r")
word_list_completed = list(f) 
masterlist = [x.upper() for x in word_list_completed] # CHANGE ALL WORDS IN THE LIST TO UPPER CASE
masterlist2 = []
masterlistcopy = []
templist = []
firstword = ""
included = ""
positn = int
correctpos = None
dictlist = []

answer = ""

for x in masterlist:
    updatedword = x[:5 - 0] #specify the lenth of the string and the number of charachters to remove.
    masterlist2.append(updatedword)

masterlist = masterlist2[:] # change back to masterlist and make masterlist immutable
masterlistcopy[:] = masterlist


###### WORD IS 'UPSET'### EVENTUALLY I WANT THESE VALUES TO BE PULLED LIVE AS THE PLAYER PLAYS THE GAME AND FOR A SCROLL ACCROSS THE TOP OF THE SCREEN TO SHOW THE AVAILABLE WORDS.
######################### THOSE WORDS WILL BE RANKED BY THE NUMBER OF TIMES PUBLISHED IN GOOGLE BOOKS.
######################### I WILL THEN POSITION THE WORDS ALREADY USED AS ANSWERS IN WORDLE TO DATE LOWER THAN ANY THAT HAVEN'T
######################### ONCE I HAVE DONE THIS I CAN AUTOMATE A BOT THAT WILL ENTER A STARTING WORD AND USING THESE PARAMETERS DECIDE AT EACH JUNCTION WHICH WORD WOULD BE BEST TO ENTER INTO THE PUZZLE

letterpositions1 = {'included?' : ['exc', 'exc', 'exc', 'inc', 'exc'], 'lettr' : ['A', 'R', 'I', 'E', 'L'], 'positn' : [0, 1, 2, 3, 4], 'correct Pos?' : [False, False, False, True, False]} #made a dictionary for the positions and properties of the letters
letterpositions2 = {'included?' : ['inc', 'exc', 'exc', 'inc', 'inc'], 'lettr' : ['S', 'H', 'E', 'E', 'T'], 'positn' : [0, 1, 2, 3, 4], 'correct Pos?' : [False, False, False, True, True]} #made a dictionary for the positions and properties of the letters
letterpositions3 = {'included?' : ['inc', 'exc', 'inc', 'inc', 'inc'], 'lettr' : ['U', 'N', 'S', 'E', 'T'], 'positn' : [0, 1, 2, 3, 4], 'correct Pos?' : [True, False, True, True, True]} #made a dictionary for the positions and properties of the letters
letterpositions4 = {'included?' : [None, None, None, None, None], 'lettr' : [None, None, None, None, None], 'positn' : [0, 1, 2, 3, 4], 'correct Pos?' : [None, None, None, None, None]} #made a dictionary for the positions and properties of the letters
letterpositions5 = {'included?' : [None, None, None, None, None], 'lettr' : [None, None, None, None, None], 'positn' : [0, 1, 2, 3, 4], 'correct Pos?' : [None, None, None, None, None]} #made a dictionary for the positions and properties of the letters
letterpositions6 = {'included?' : [None, None, None, None, None], 'lettr' : [None, None, None, None, None], 'positn' : [0, 1, 2, 3, 4], 'correct Pos?' : [None, None, None, None, None]} #made a dictionary for the positions and properties of the letters



def positionofletters(dictlist, masterlist):
    global lettr####### Global v's?
    global included
    global positn
    global correctpos
    dictlist = [letterpositions1, letterpositions2, letterpositions3, letterpositions4, letterpositions5, letterpositions6]

    i = 1 #for the iterations
    l = 0
    
    while i <= len(dictlist): 
        if len(masterlist) == 1:
            break

        dictbeingused = dictlist[i-1]#this will select the dictionary from the list of dictionaries [i-1]
        
        while l <= 4:
        
            included = dictbeingused ['included?'][l] #select the key 'included' and then grab the 'i' instance from the list -1 obvs
            lettr = dictbeingused ['lettr'][l] #select the key 'lettr' and then grab the 'i' instance from the list -1 obvs
            positn = dictbeingused ['positn'][l] #select the key 'positn' and then grab the 'i' instance from the list -1 obvs
            correctpos = dictbeingused ['correct Pos?'][l] #select the key 'correct Pos?' and then grab the 'i' instance from the list -1 obvs
            
            if included == 'inc':#if letter included then...
                letterinc()
                l += 1

            elif included == 'exc':#if letter excluded then...
                letterexc()
                l += 1
                
            elif included == None:#if 'none' then...
                break #will move to next higher level if
                
        if len(masterlist) == 1:
            break
        l = 0#reset l so that the dictionary iterations can restart
        i += 1# will move to next dictionary


def letterinc(): #will remove any words that don't contain the letter

    if correctpos == True:    #is the letter in the correct position? - yes. then...
        letterincpostrue()

    elif correctpos == False: #is the letter in the correct position? - no. then...
        letterincposfalse()


def letterincpostrue(): #will remove any words that don't hold the letter in the given position
        for word in masterlist2:
            if lettr not in word [positn]:
                if word in masterlist:
                    masterlist.remove(word)
        masterlist2[:] = masterlist
        
def letterincposfalse(): #will remove any words that do have the letter in the given position
        for word in masterlist2:
            if lettr in word [positn]:
                if word in masterlist:
                    masterlist.remove(word)
        masterlist2[:] = masterlist


def letterexc(): # will remove any words containing the letter
    for word in masterlist2:
            if lettr in word [positn]:
                if word in masterlist:
                    masterlist.remove(word)                    
    masterlist2[:] = masterlist

positionofletters(dictlist, masterlist) #starts!!

print(masterlist)#prints the final list - "UPSET"