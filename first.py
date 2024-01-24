print("first python project")
age = int(input("How old are you? "))

if age < 14:
    print("Too young, sorry.")
elif age == 43:
    hru = input("Hello Kim. How are you? g/b (good or bad) ")
    if hru == "g":
        topic1 = input("I mean, it's not like you'd pick bad right?... ANYWAY, do you want to talk about cars or music next? ")
        if topic1 == "cars":
            cars = input("Vroom Vroom. Audi or Lambo? ")
            if cars == "audi":
                print(" The obvious choice. You have now finished the quiz.")
            if cars == "lambo":
                print("Too pricy.. you failed. lol")
        if topic1 == "music":
            music = input("J Cole or Kanye?")
            if music == "j cole":
                print("no role models and im here right now yea u passed :)")
            if music == "kanye":
                print("nope imma out of here.")
    if hru == "b":
        print("lol u failed 2nd question")
elif age > 30:
    print("You are so old!")
else:
    print("Hello. You are old enough.")
