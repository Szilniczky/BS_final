import os 

table1 = [[0,0,0,0,0,0,0,0,0,0],  #for store the place of the ships of the first player
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

table2 = [[0,0,0,0,0,0,0,0,0,0], #for store the coordinates of the ships of the second player
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

# counts the scores of player1
def counthit1():
    q = 0
    for a in range(0, 10):
        table2[a].count(2)
        q = q + table2[a].count(2)
    return q

# counts the scores of player2
def counthit2():
    r = 0
    for z in range(0, 10):
        table1[z].count(2)
        r = r + table1[z].count(2)
    return r

# player1 placing the ships in the table1
def makingships1():
    print("Hello first player!")
    for shipsize in range(1,4):
         print("Let's make your " + "%d" % shipsize + " size ships" )
         for i in range(1,3):
             x=int(input("first ship1 coordinate: "))
             y=int(input("second ship1 coordinate: "))
             for h in range(1,shipsize+1):
                 table1[x+h-2][y-1] = 1
             os.system('cls' if os.name == 'nt' else 'clear')
             printthetableplayer1ships()
    ask=input("press enter")

# player2 placing the ships in his table2
def makingships2():
     
     for shipsize in range(1,4):                                          #for making diff sized ships
         print("Let's make your " + "%d" % shipsize + " size ships" )
         for i in range(1,3):                                             #for making 3 ships/size
             x=int(input("first ship2 coordinate: "))
             y=int(input("second ship2 coordinate: "))
             for h in range(1,shipsize+1):                                 #for making as many shipunit as big ship is making in the cycle
                 table2[x+h-2][y-1] = 1
             os.system('cls' if os.name == 'nt' else 'clear')
             printthetableplayer2ships()
     ask=input("press enter")

# printing the table1 with the ships
def printthetableplayer1ships():
   print("   ABCDEFGHIJ")
   for row in range(0,10):
       print( "%2d " % (row+1), end= "")
       for column in range(0,10):
              if table1[row][column] == 0:
                  print("~", end= "")
              if table1[row][column] == 1:
                  print("O", end= "")
              if table1[row][column] == 2:
                  print("X", end= "")
              if table1[row][column] == 3:
                  print("*", end= "")
       print("") # print a newline char

# printing the table2 with the ships
def printthetableplayer2ships():
   print("   ABCDEFGHIJ")
   for row in range(0,10):
       print( "%2d " % (row+1), end= "")
       for column in range(0,10):
              if table2[row][column] == 0:
                  print("~", end= "")
              if table2[row][column] == 1:
                  print("O", end= "")
              if table2[row][column] == 2:
                  print("X", end= "")
              if table2[row][column] == 3:
                  print("*", end= "")
       print("") # print a newline char

# printing the table2 with the hits and/or misses
def printthetableplayer1shoots():
   print("   ABCDEFGHIJ")
   for row in range(0,10):
       print( "%2d " % (row+1), end= "")
       for column in range(0,10):
              if table2[row][column] == 0:
                  print("~", end= "")
              if table2[row][column] == 1:
                  print("~", end= "")
              if table2[row][column] == 2:
                  print("X", end= "")
              if table2[row][column] == 3:
                  print("*", end= "")
       print("") # print a newline char

# printing the table1 with the hits and/or misses
def printthetableplayer2shoots():
   print("   ABCDEFGHIJ")
   for row in range(0,10):
       print( "%2d " % (row+1), end= "")
       for column in range(0,10):
              if table1[row][column] == 0:
                  print("~", end= "")
              if table1[row][column] == 1:
                  print("~", end= "")
              if table1[row][column] == 2:
                  print("X", end= "")
              if table1[row][column] == 3:
                  print("*", end= "")
       print("") # print a newline char

# player1 shoot in table2
def shootplayer1():
    print("")
    print("PLAYER1")
    printthetableplayer1shoots()
    a = int(input("First shoot1 coordinate"))
    b = int(input("Second shot1 coordinate"))

    if table2[a-1][b-1] == 1:
        table2[a-1][b-1] = 2
    if table2[a-1][b-1] == 0:
        table2[a-1][b-1] = 3
    os.system('cls' if os.name == 'nt' else 'clear')
    printthetableplayer1shoots()
    e = counthit1()
    print("PLAYER1 SCORE:", e)
    if e == 12:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("***PLAYER1 WINS***")
        return True

# player2 shoot in table1
def shootplayer2():
    print("")
    print("PLAYER2")
    printthetableplayer2shoots()
    a = int(input("First shot2 coordinate"))
    b = int(input("Second shot2 coordinate"))

    if table1[a-1][b-1] == 1:
        table1[a-1][b-1] = 2
    if table1[a-1][b-1] == 0:
        table1[a-1][b-1] = 3
    os.system('cls' if os.name == 'nt' else 'clear')
    printthetableplayer2shoots()
    u = counthit2()
    print("PLAYER2 SCORE:", u)
    if u == 12:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("***PLAYER2 WINS***")
        return True


print("Hello, let's begin the play.")
print("Someone has to go out or close his/her eyes while the other player places his/her ships in the table")

makingships1()
print("Now you're ready, it's the other player's turn")
os.system('cls' if os.name == 'nt' else 'clear')

makingships2()
os.system('cls' if os.name == 'nt' else 'clear')


# gives 100 possible shoots and if player1 or player2 reach 12 score then end the game
shootnum = 0
while(shootnum<=100):
    k = shootplayer1()
    if k == True:
        break
    l = shootplayer2()
    if l == True:
        break
    shootnum = shootnum + 1 