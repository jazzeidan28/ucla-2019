name = input("What is your name?")




print("Nice to meet you,",name)

age = input("How old are you?")
age = int(age)
print("Oh, I'm actually"+ str(age-4)+"years old.")
print("You look "+ str(age-5)+" LOL!")

joke = input("Wanna hear a joke?")
print("I was going to tell you either way.")
joke = input("Knock knock.")
joke = input("Europe.")
print("No you're a poo! HAHA!")
question = input("Did you like it? ")
if question == "Yes" or question == "YES" or question == "yes" or question == " yes":
    print("Thanks!")
elif question == "Meh" or question == "meh" or question == " meh": 
    print("Wow, ouch.")
    question = input("How can I get better?")
    print("Okay, whatever. I'll work on my material I guess.")
    
elif question == "No" or question == "NO" or question == "no" or question == " no" :
    print("That's just rude!")
    print("I'll just leave, you're so mean! Bye.")