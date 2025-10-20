word_input = input()
if "A" <= word_input <= "Z":
    print(word_input.lower())
elif "a" <= word_input <= "z":
    print(word_input.upper())
else :
    print(word_input)