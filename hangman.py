import random
name=input("enter your name")
print("wlcome",name,"!")
print("------------------")
def hangman():
    print("try to guess the word in less than 10 attempts")
    list_words=["ujala","hangman","roshni","shubhkirti","neetu","ruchi"]
    words=random.choice(list_words)
    turns=10
    guessmade=""
    valid_entery=set("abcdefghijklmnopqrstvwxyz")
    print("guess the characters")
    while len(words)>0:
        main_words=""
        for letter in words :
            if letter in guessmade:
                main_words=main_words+letter
            else:
                main_words+="_ "
        if main_words==words:
            print(main_words)
            print("you won!!!")
            break
        print("guess the words",main_words)
        guess=input("guess a letter")
        if guess in valid_entery:
            guessmade=guessmade+guess
        else:
            print("enter valid character")
        
        if guess not in words:
            turns=turns-1
            if turns==9:
                print("9 turns left !!!")
                print("-----------------")
            if turns==8:
                print("8 turns left !!!")
                print("-----------------")
                print("       o        ")
            if turns==7:
                print("7 turns left !!!")
                print("-----------------")
                print("        o        ")
                print("        |        ")
            if turns==6:
                print("6 turns lift !!!")
                print("-----------------")
                print("        o        ")
                print("        |        ")
                print("       /         ")
            if turns==5:
                print("5 turns lift !!!")
                print("-----------------")
                print("        o        ")
                print("        |        ")
                print("       / \        ")
            if turns==4:
                print("4 turns lift !!!")
                print("-----------------")
                print("      \ o        ")
                print("        |        ")
                print("       / \        ")
            if turns==3:
                print("3 turns lift !!!")
                print("-----------------")
                print("      \ o /       ")
                print("        |        ")
                print("       / \        ")
            if turns==2:
                print("2 turns lift !!!")
                print("-----------------")
                print("      \ o / |    ")
                print("        |        ")
                print("       / \        ")
            if turns==1:
                print("only 1 turns lift !!! hangman on his last breath")
                print("-----------------")
                print("      \ o /__|    ")
                print("        |        ")
                print("       / \        ")
            if turns==0:
                print("you loose")
                print("you let a good man die")
                print("would you like toplay again")
                again=input("enter Y or N:")
                if again=='Y':
                    hangman()
                else:
                    print("thanks for playing")
                    break
hangman()
