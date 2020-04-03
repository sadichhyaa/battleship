from os import system,sys
import random
ships = [
      {"name":"destroyer","length":2},
      #{"name":"submarine","length":3},
      #{"name":"cruiser","length":3},
      #{"name":"battleship","length":4},
      #{"name":"carrier","length":5}
]
class player:
  playersb=[]
  playerab=[]
  ship_coordinates=[]
  
  def __init__(self,name):
    self.name=name
    board=[]
    for i in range(10):
      temp=[]
      board.append(temp)
      for j in range(10):
          board[i].append(0) 
    self.playerab=board
    board=[]
    for i in range(10):
      temp=[]
      board.append(temp)
      for j in range(10):
          board[i].append(0)
    self.playersb=board
    display_board(self.name,self.playersb,self.playerab)
  
  def takeposition(self):
    temp_ship_list={}
    for ship in ships:
      flag= True
      while flag:
        orientation=input("Enter orientation of {} ,(V/H):".format(ship["name"]))
        x,y=input("enter starting position of {} (0-9) ,(ord(A)-ord(j))): ".format(ship["name"])).split()
        x=x.upper()
        if int(y)<10 and int(ord(x))<75:
          flag=False
          coordinate_list = []
          for i in range(ship["length"]):
            if orientation.upper() == "V":
              coordinate=(ord(x)-65 + i, int(y)-1)
            if orientation.upper() == "H":
              coordinate=(ord(x)-65, int(y)-1 + i * 1)
            coordinate_list.append(coordinate)
            if coordinate[0]>9 or coordinate[1]>9 or coordinate[0]<0 or coordinate[1]<0:   
              flag=True
              break;
            if self.playersb[coordinate[0]][coordinate[1]]=="O":
              flag=True
              break;
        if flag:
          print("enter again")
          
        
      for coordinate in coordinate_list:
        self.playersb[coordinate[0]][coordinate[1]]="O"   
      display_board(self.name,self.playersb,self.playerab)
      temp_ship_list[ship["name"]] = coordinate_list  
      self.ship_coordinates=temp_ship_list 
  
  def generate_shifts(self):
    temp_ship_list={}
    for ship in ships:
      flag= True
      while flag:
        orientation=random.randint(0,1)
        if orientation==0:
          orientation="V"
        else:
          orientation="H"
        x=random.randint(0,9)
        y=random.randint(0,9)
        if int(y)<10 and int(x)<10:
          flag=False
          coordinate_list = []
          for i in range(ship["length"]):
            if orientation.upper() == "V":
              coordinate=(x + i, int(y)-1)
            if orientation.upper() == "H":
              coordinate=(x, int(y)-1 + i * 1)
            coordinate_list.append(coordinate)
            if coordinate[0]>9 or coordinate[1]>9 or coordinate[0]<0 or coordinate[1]<0:   
              flag=True
              break;
            if self.playersb[coordinate[0]][coordinate[1]]=="O":
              flag=True
              break;
          
        
      for coordinate in coordinate_list:
        self.playersb[coordinate[0]][coordinate[1]]="O"   
      display_board(self.name,self.playersb,self.playerab)
      temp_ship_list[ship["name"]] = coordinate_list  
      self.ship_coordinates=temp_ship_list 
  




def display_board(name,shipboard,attackboard):
  system("cls")
  print(name +"'s turn \n")
  print("attack board")
  print("      1   2   3   4   5   6   7   8   9   10")
  print("   "+"-"*41)
  for row, column in enumerate(attackboard):
    print((" "+chr(row + 65) + " |" + " {} |"*10).format(*[x if x != 0 else " " for x in column]))
    if row <9:
      print("   |" + "---+"*9 + "---|")
    else:
      print("   "+ "-"*41)
  print()
  print(" "*15+"ship board\n")
  print("     1   2   3   4   5   6   7   8   9  10")
  print("   "+ "-"*41)
  for row, column in enumerate(shipboard):
    print((" "+chr(row + 65) + " |" + " {} |"*10).format(*[x if x != 0 else " " for x in column]))
    if row <9:
      print("   |" + "---+"*9 + "---|")
    else:
      print("   "+ "-"*41)
  
def missile_fire(playerab,playersb):
  x,y= input("enter the coordinate of fire").split()
  x=x.upper()
  x=ord(x)-65
  y=int(y)-1
  if playersb[x][y]==0:
    playerab[x][y]="*"
  if playersb[x][y]=="O":
    playerab[x][y]="$"
    playersb[x][y]="x"

def check_victory(playersb, name):
    victory = True
    for row in playersb:
        if "O" in row:
            victory = False
    if victory:
        system("cls")
        print(name,"WON THE GAME")
        ch = sys.stdin.read(1)
        main()


def match(player1,player2):
  turn = random.randint(0,1)
  players=[player1,player2]
  print("game begin")
  ch=sys.stdin.read(1)
  while True:
    print("player",str(turn +1)+"'s turn\n")
    display_board(players[turn].name,players[turn].playersb,players[turn].playerab)
    
    missile_fire(players[turn].playerab,players[(turn+1)%2].playersb)
    display_board(players[turn].name,players[turn].playersb,players[turn].playerab)
    check_victory(players[(turn+1)%2].playersb,players[turn].name)
    turn=(turn + 1) % 2
    ch=sys.stdin.read(1)

def main():

  player1=player("player 1")
  player1.generate_shifts()
  ch=sys.stdin.read(1)
  player2=player("player2")
  player2.generate_shifts()
  ch=sys.stdin.read(1)
  match(player1,player2)
  ch=sys.stdin.read(1)

  #print(player1)

if __name__=="__main__":
  main()
..

