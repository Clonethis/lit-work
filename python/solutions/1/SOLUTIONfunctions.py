# TODO  create usefull function with help of 'forwithstring.py' to iterate it on given data, 
#you will return to 'forwithstring' and refactor code to functio so you could use it in this file
from SOLUTIONforwithstrings import splitFunction

#TODO refactor function that it takes on input 'splitting parameter', 'data' that it will get in string -> to be usefull
basicString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
splitArray= [' ',', ','u',]
# splitFunction(basicString," ")

#TODO iterate over 'splitArray' to show how 'splitFunction' could be used, as a value for 'splitFunction' use 'basicString'
for splitChar in splitArray:
    # print('split char',splitChar)
    splitFunction(basicString,splitChar)
    print()
# output
# LidsacaesdetiuledmaUeamvqneulnuaeeccDaidirivvecdefnpEsocnpsicqodmaiel
# Lcsqs
# Lmrsntaidltiaitrpm glrrpnlinm