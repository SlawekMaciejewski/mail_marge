PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    # names = []
    # for name in names_file.readlines():
    #     names.append(name.strip("\n"))
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", "w") as new_letter_file:
            new_letter_file.write(new_letter)
