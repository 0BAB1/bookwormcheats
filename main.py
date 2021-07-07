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
print("\n \nfichier overt avec success, chargement...")

#charger les lignes et les traiter
lines = wordlist.read().splitlines()
print("fichier chargé !")

while True:
    #mainloop
    valid_words = []
    request = input("\n \n ==================================== \nentrez vos lettres, les unes a la suite des autres sans separateur : \n ---> ")
    request = request.lower() #tout en minuscules
    print(" \n \n ... recherche de mots ...")
    for word in lines:
        if IsValid(word, request):
            valid_words.append(word)

    #phase de tri du plus grand au plus petit
    higherLen = 0
    bestWords = []
    for word in valid_words:
        if len(word) > higherLen:
            bestWords = []
            bestWords.append(word)
            higherLen = len(word)
        elif len(word) == higherLen:
            bestWords.append(word)
    
    print("\n meilleurs mot avec " + str(len(bestWords[0])) + " caractères : \n \n" + str(bestWords))


print("bye")