# Checklist for a sleepover
# Main function = checklist()
def checklist():
    question = input("Are you having a sleepover? ")
    if question.lower() == "yes":
        print("Nice!")
    else:
        print("Too bad.")
        exit()


# Clothes function
    # Clothes lists
    clothes_list = []
    clothes_needed = ["hoodie", "pants", "t-shirt", "underwear", "sweatpants"]


    def allclothes():
        while clothes_list is not clothes_needed:
            if clothes_list == clothes_needed:
                print("\nOkay great. Next one.\n")
                book = "yes"
                break
            print("Okay you need a hoodie, pants, t-shirt, underwear and sweatpants.")
            clothes = input("\nWhat clothes are you taking with you? ")
            if clothes in clothes_needed:
                clothes_list.append(clothes)
                print(f"You now have packed a {clothes_list}.")
            elif clothes in clothes_list:
                print("You don't need more of that.")
            else:
                print("I don't know what that is...")


    # Book question
        if book == "yes":
            book_taken = input("Did you pack a book? ")

            if book_taken.lower() == "yes":
                book_choice = input("Great! Which one? ")
            elif book_taken.lower() != "yes":
                print("Don't forget your book!")
                book_taken = input("Did you pack a book now? ")
                if book_taken.lower() == "yes":
                    book_choice = input("Great! Which one? ")


    # Pillow question
        take_pillow = input("Do you want to take your pillow? ")

        if take_pillow.lower == "yes":
            pillow = True
            print("Okay, okay. Let's go to the next.")
            print(pillow)
        else:
            print("\nOkay, next question.\n")

    # Travel bag question
        take_travel_bag = input("Do you have everything you need in your travel bag? ")
        if take_travel_bag == "yes":
            travel_bag = input("So you have your glasses, lenses, perfume, wax and toothbrush? ")
            if travel_bag == "yes":
                print("Okay okay, just checking...")
            else:
                print("\nYou should put those in the washbag.\n")

    # Extra pair of shoes?
        extra_shoes = input("I was wondering, do you need an extra pair of shoes? ")
        if extra_shoes == "yes":
            print("You don't need them. But okay...")
        else:
            print("Great choice!")

    # Jacket question
        weather = input("Is it cold outside? ")
        if weather == "yes":
            print("\nYou should wear a thick jacket.\n")
        else:
            print("\nGreat, then you won't need a thick jacket. Grab a denim jacket.\n")
        jacket = input("So... did you grab a jacket? ")
        if jacket == "yes":
            print("\nOkay great. Let's get the rest.\n")

    # Wallet question
        wallet = input("This one is important. Do you have your wallet? ")
        if wallet == "yes":
            print("Nice one.")
        else:
            print("Get up and get it!")
            wallet = "yes"


    # Car keys
        car = input("Are you driving there? ")
        if car == "yes":
            car = True
            if car == True:
                car_keys = input("Great, drive safe! Did you grab the keys and papers? ")
                if car_keys == "yes":
                    print("\nThank you. Next.\n")
                else:
                    car_keys == "yes"
                    print("\nGrab the keys.\n")
        else:
            print("\nOkay, no worries.\n")

    # House keys
        if car == True:
            house_keys = input("So you have your car keys. But do you have the keys of the house? ")
        else:
            house_keys = input("Do you have the keys of the house? ")
            if house_keys == "yes":
                print("\nOkay. Good.\n")
            else:
                print("\nGrab the keys.\n")

    # Sunglasses
        sun = input("You think the sun will shine while you're driving? ")
        if sun == "yes":
            sunglasses = input("Do you have your sunglasses? ")
            if sunglasses == "yes":
             print("Great, then you're almost done!")
            else:
                print("\nYou might want to grab those.\n")
        else:
            print("Just take them with you...")
            sunglasses = "yes"

    # Summary
        print("Okay let's sum it up.")
        print(f"""You now have packed: \n
            These clothes:  {clothes_list}\n
            This book:      {book_choice}\n""")
        if pillow == True:
            print("Your pillow.")
        else:
            pass
        if travel_bag == "yes":
            print("You packed your travel bag.")
        if extra_shoes == "yes":
            print("Some extra shoes.")
        if jacket == "yes":
            print("You have a jacket.")
        if wallet == "yes":
            print("You have your wallet.")
        if car_keys == "yes":
            print("You have your car keys.")
        else:
            pass
        print("You grabbed the house keys.")
        print("You have your sunglasses.")
        print("That should be all. You're good!")

        quit()

    # End main function


    allclothes()





checklist()