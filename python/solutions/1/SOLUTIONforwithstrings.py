# TODO you shall write out every first letter of the sentence
# -> to get more comfortable with using strings and for loops

basicString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# split implementation -> throws word to separate array element
splitText = basicString.split()


# my way ->
print(" Code 1:")
for word in splitText:
    print(word[0], end='')

print("\n Code 2: ")
# or without split
beforeElement = ' '
for element in range(len(basicString)):
    if beforeElement == ' ':
        print(basicString[element], end='')
        beforeElement = basicString[element]
    else:
        beforeElement = basicString[element]

#output : LidsacaesdetiuledmaUeamvqneulnuaeeccDaidirivvecdefnpEsocnpsicqodmaiel
