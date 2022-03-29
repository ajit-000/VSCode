def minion_game(x):
    comb_v,comb_c=0,0
    for i in range(0, len(x)):
        if x[i] == "a" or x[i] == "A" or x[i] == "e" or x[i] == "E" or x[i] == "i" or x[i] == "I" or x[i] == "o" or x[i] == "O" or x[i] == "u" or x[i] == "U":
            comb_v+=len(x[i:])
        else:
            comb_c+=len(x[i:])
    if comb_c>comb_v:
        print("X",comb_c)
    elif comb_c<comb_v:
        print("Y",comb_v)
    else:
        print("Draw")

if __name__=="__main__":
    x=input("Enter the string you want for game: ")
    minion_game(x)
