def user_prompt(text, number_of_choices):
    print(text)
    user_input = input("What do you want to do?")
    print(user_input)

    while True:
        if not (user_input.isalpha() and len(user_input) == 1):
            user_input = input("Please enter your choice as a letter: ")
        else:
            break

 # lower_case_input = user_input.lower()
    return user_input

text = "You are in the emergency room at the local hospital. Thank heavens it is a weekend so you are taken back to a bed fairly quickly and avoid the usual 5 hour wait - you are in an immense amount of pain from a chronic health condition and already know that you need to have a procedure done. You will likely be admitted. You explain your symptoms to the nurse and eventually the doctor comes in to see you. The doctor pulls up your details on the computer and says that the ER treatment plan is to offer you benadryl and another sedative. Although you expected this, you are horrified to know that, rather than treat your pain, they're offering medications to simply knock you out. You are enraged but do everything you can to remain calm because you do not want to be labeled as \"drug seeking\" and know the staff will not take you seriously if you lose your temper. You are accompanied by your partner and you best friend who have offered to advocate for you. You can (a) say nothing and take whatever drugs or tests the medical staff eventually order or, (b) allow yourself to get angry, lose your temper (you have been through this so many times before and are sick of not being listened to or taken seriously), or (c) Ask your friend and partner to advocate for you and keep your own mouth shut (while writhing in pain)\n\n"

user_prompt(text, 3)





