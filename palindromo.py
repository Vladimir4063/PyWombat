def palindromo(sentencia):
    id1 = 0
    id2 = len(sentencia) -1

    while(id1 < id2):
        if (sentencia[id1] != sentencia[id2]):
            print('False')
            return
        id1 = id1 + 1
        id2 = id2 - 1
    print('True')

palindromo("anitalavalatina")
palindromo("Holalala")
