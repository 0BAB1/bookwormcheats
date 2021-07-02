'''petit programe de triche dans les jeux de lettres (scrabble, bookworm, etc...)'''

def removeChar(char,str):
    '''le but est de supprimer un charactère une fois placé'''
    i = 0
    for char2 in str: 
        if char == char2: #on reagrde le nombre de fois ou le caractère est présent
            i+=1
    if i == 1: #s'il n'es present qu'une seule fois ..
        return str.replace(char, '')
    elif i > 1: #sinon, on retire les charactères et on replace ceux qui on été enlevés sans etre utilisés
        str = str.replace(char, '')
        for j in range (i-1):
            str = str + char
        return str

def IsValid(word,request):
    '''verifier si un mot peut être formé par les lettres'''
    i = 0
    for char in word:
        if char in request:
            request = removeChar(char, request) 
            #si une lettre est presente, on la retire car elle ne peut pas etre utilisée 2x
            continue
        else: 
            return False
    return True

#open file and load it
wordlist = open("wordlist.txt", "r")
print("file successfuly opened ! initializing ...")

#charger les lignes et les traiter
lines = wordlist.read().splitlines()
print("file loaded")

while True:
    valid_words = []
    request = input("entrez vos lettres, les unes a la suite des autres sans separateur : \n ---> ")
    request = request.lower() #tout en minuscules
    print("... recherche de mots ...")
    for word in lines:
        if IsValid(word, request):
            valid_words.append(word)

    print("mots valides : " + str(valid_words))


print("bye")