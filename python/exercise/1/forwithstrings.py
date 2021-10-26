# TODO you shall write out every first letter of the sentence
# -> to get more comfortable with using strings and for loops

basicString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# look for 'string split'

# implement split on string above / or use if statement to check for 'whitespace' the print only element that is after 'whitespace'

splitText = basicString.split()
firstLetters = ""
print(splitText)
for word in splitText:
    #print(word)
    for i in word:
        #print(i)
        if i == word[0]:
            print(i, end= "")

# TODOimplement for loop that iterates over 'splitText' -> print outupu

# to print it on one line search for 'print' and its usage, arguments, formating...
#output : LidsacaesdetiuledmaUeamvqneulnuaeeccDaidirivvecdefnpEsocnpsicqodmaiel


# if done try different way