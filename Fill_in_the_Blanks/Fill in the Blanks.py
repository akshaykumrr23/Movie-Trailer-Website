#Hard level
hard = {
    'quiz': """Last vacation, my __1__ decided we would make a Middle East trip for about 5-7 __2__ and return and so the __3__ for the same was being carried on. We had our relatives and friends down there who had been __4__ us for some time and this time we decided we would make it.""",
    'questions': ["__1__", "__2__", "__3__", "__4__"],
    'answers': ["family","days","preparations","inviting"]
}

#Medium level
medium = {
    'quiz': ("__1__ is unconditional and selfless. Love knows __2__ boundaries. Love may happen __3__ sisters, brothers, friends, siblings, parents, neighbors, pet, relatives, partners etc. You are always available for the __4__ whom you love."),
    'questions': ["__1__", "__2__", "__3__", "__4__"],
    'answers': ["Love", "no", "among", "person"]
}

#Easy level
easy = {
    'quiz': """Love is the __1__ to happiness. We all want to lead a __2__ life. People look around for __3__ in power, fashion, wealth, drugs etc. But these things can only give __4__ pleasures.""",
    'questions': ["__1__", "__2__", "__3__", "__4__"],
    'answers': ["key", "happy", "happiness", "temporary"]
}

#function for matching answers with the correct answers and also manages the number of tries and prints the paragraph again and again with correct answers
def goanswers(level):
    max_tries, ques_no = 4, 0
    final_ques = 4
    print "\nLets Start :)\n"
    print level['quiz']

    while(ques_no < final_ques and max_tries > 0):
        inp = raw_input("Enter Replacement for %s: " %(level['questions'][ques_no]))
        if(inp == level['answers'][ques_no]):
            print "Correct Answer :)\n"
            print "Updated Quiz: \n"
            level['quiz'] = level['quiz'].replace(level['questions'][ques_no], level['answers'][ques_no])
            print level['quiz']
            ques_no = ques_no + 1
        else:
            max_tries = max_tries - 1
            print "\nWrong answer :(\nTry Again!\n"
            if(max_tries > 0):
                print "Tries Available Now: ", max_tries
            
    if ques_no == final_ques:
        print "Congo! You Have Completed the quiz! :)"

#first function which prompts user for the difficulty level
def starting():
    print ("Welcome To The Quiz of Love and Vacations!!!!\n")
    choice = raw_input("Enter level((E)asy, (M)edium Or (H)ard): ").lower()
    if (choice == "e"):
        return goanswers(easy)#it sends the difficulty level to function goanswers
    elif (choice == "m"):
        return goanswers(medium)#it sends the difficulty level to function goanswers
    elif (choice == "h"):
        return goanswers(hard)#it sends the difficulty level to function goanswers
    else:
        print ("\nWrong Option Selected! Run the quiz again!!")
        starting()

#starting of program
starting()
