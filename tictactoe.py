def sum (a,b,c):
    return a+b+c






def game_board(xchance,zchance):
   zero='x' if xchance [0] else ('o' if zchance[0]else 0)
   one='x' if xchance [1] else ('o' if zchance[1]else 1)
   two='x' if xchance [2] else ('o' if zchance[2]else 2)
   three='x'if xchance [3] else ('o' if zchance[3]else 3)
   four='x' if xchance [4] else ('o' if zchance[4]else 4)
   five='x' if xchance [5] else ('o' if zchance[5]else 5)
   six='x' if xchance [6] else ('o' if zchance[6]else 6)
   seven='x' if xchance [7] else ('o' if zchance[7]else 7)
   eight='x' if xchance[8] else ('o' if zchance[8]else 8)

   print(f"{zero}  | {one}   |{two} ")
   print(f"---------------------- ")
   print(f"{three}  | {four}   | {five}")
   print(f"-----------------------" )
   print(f"{six}  | {seven}   | {eight} ")






             
def checkwinner(xchance,zchance):

    wins=[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
    for win in wins:
        if(sum(xchance[win[0]],xchance[win[1]],xchance[win[2]])==3):
            print("x won this match:)")
            return 1
        if (sum(zchance[win[0]],zchance[win[1]],zchance[win[2]])==3):
             print("O won this match :)")
             return 0
    return -1     

if __name__=='__main__':
   xchance=[0,0,0,0,0,0,0,0,0]
   zchance=[0,0,0,0,0,0,0,0,0]
   turn=1
   print("Tic Tac Toe Game")
   while(True):
       game_board(xchance,zchance)
       if (turn==1):
            print("X's Chance")
            value= int(input("please enter a value:"))
            xchance[value]=1
       else:
           print("O's Chance")
           value= int(input("please enter a value:"))
           zchance[value]=1
       cwin= checkwinner (xchance,zchance)
       if (cwin != -1):
            print("match over")
            print(cwin)
            break
       turn=1-turn
else:
   print("match is draw")
