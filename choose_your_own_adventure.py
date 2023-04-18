name = input("The 'Choose Your Own Adventure' Game\nType your name: ")
print("Welcome", name, "to this adventure!")
answerQ1 = input("You are presented a white pill and a black pill. Which color pill do you take? (Type 'black' or 'white'): ")
if answerQ1 == "black":
    answerQ2 = input("You take the black pill and next thing you remember is waking up in Canada on a park bench. You wake up in a panic and see a lady asleep on the next bench over. Do you wake her up? (Type 'yes' or 'no'): ")
    if answerQ2 == "yes":
        answerQ3 = input("You nudge the sleeping woman on the bench and she wakes up in a fright. When she realizes it's you she says 'hey shouldn't you be gone by now? Last night you kept saying how someone was chasing you and you had to take the next bus going north to get away.' Memories come flooding back from the night before and you take off in a sprint to the bus stop. Next thing you know you're at Greenland International Airport and are being asked for a passport. Do you present your American passport or Sri Lankan passport? (Type 'american' or 'sri lankan): ")
    
    elif answerQ2 == "no":
        answerQ3 = input("You do not have the courage to talk to the lady so you get up and start walking along. You start to notice all the bypassers on the street are staring and gasping as you walk by and you begin to wonder why. A mother from the kid's playground nearby notices you and calls the police. By the time you realize you don't have pants on its too late, you are being arrested for public indecency. From a jail cell now you are given one call, who do you call: Option 1 or Option 2? (Type '1' or '2'): ")
        if answerQ3 == "1":
            answerQ4 = input("You call your mom, she bails you out.")

        if answerQ3 == "2":
            answerQ4 = input("You call your ex-wife who you seperated with 5 months ago. She does not take your call and you are stuck in jail forever.\nYou lose. Goodbye.")

        else:
            answerQ3 = input("Not a valid option.\nYou lose. Goodbye.")


    else:
        answerQ2 = input("Not a valid option.\nYou lose. Goodbye.")

elif answerQ1 == "white":
    answerQ2 = input("You take the white pill and nothing ever happens to you. You wonder until your dying day what that pill was for and never figure it out.\nYou lose. Goodbye.")

else:
    answerQ1 = input("Not a valid option.\nYou lose. Goodbye.")
