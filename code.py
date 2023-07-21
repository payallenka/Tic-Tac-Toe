import sys
theboard={'top l': " ",'top m':" ",'top r':" ",'mid l':" ",'mid m':" ",'mid r':" ",'bot l':" ",'bot m':" ",'bot r':" "}
def printboard(board):   #To print the empty board
    print(board['top l']+"|"+board['top m']+"|"+board['top r'])
    print("-+-+-")
    print(board['mid l'] + "|" + board['mid m'] + "|" + board['mid r'])
    print("-+-+-")
    print(board['bot l'] + "|" + board['bot m'] + "|" + board['bot r'])
printboard(theboard)
turn="X"
a=1
l=['top l','top m','top r','mid l','mid m','mid r','bot l','bot m','bot r'] #list to ensure later that none of the turns are overwritten 
print("All the best play well")
while a<=9:
    print("player ",turn," turn")
    i = input("enter the location ")
    if i in l:
        theboard[i] = turn
        printboard(theboard)
        if (theboard['top l']==theboard['top m']==theboard['top r']=='X'or theboard['mid l']==theboard['mid m']==theboard['mid r']=='X' or theboard['bot l']==theboard['bot m']==theboard['bot r']=='X'or theboard['top l']==theboard['mid l']==theboard['bot l']=='X'or theboard['top m']==theboard['mid m']==theboard['bot m']=='X' or theboard['top r']==theboard['mid r']==theboard['bot r']=='X' or theboard['top l']==theboard['mid m']==theboard['bot r']=='X' or theboard['top r']==theboard['mid m']==theboard['bot l']=='X'):
            print("player X won")
            sys.exit()
        elif (theboard['top l']==theboard['top m']==theboard['top r']=='O'or theboard['mid l']==theboard['mid m']==theboard['mid r']=='O' or theboard['bot l']==theboard['bot m']==theboard['bot r']=='O'or theboard['top l']==theboard['mid l']==theboard['bot l']=='O'or theboard['top m']==theboard['mid m']==theboard['bot m']=='O' or theboard['top r']==theboard['mid r']==theboard['bot r']=='O' or theboard['top l']==theboard['mid m']==theboard['bot r']=='O' or theboard['top r']==theboard['mid m']==theboard['bot l']=='O'):
            print("player O won")
            sys.exit()
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        a+=1
        l.remove(i)
    else:
        print("that location is already taken")
        a-=1
print("no player won")
