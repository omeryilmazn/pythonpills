import os,time
def tictactoe():
  map = [[0,0,0],[0,0,0],[0,0,0]]

  print("   j, k, l")
  for counter,i in enumerate(map):
    
    print(counter, i)
  time.sleep(1)
  os.system("cls")

tictactoe()
# map[0][1] =  ---- USE THIS LINE OF CODE FOR MAKING YOUR MOVE TO DESIRED COORDINATES AND CALL THE FUNCTION AGAIN.
