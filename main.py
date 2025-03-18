
import os
import time
import random

#V2. 1 array random.choice(coordinate) array.pop

#TODO LIST:
#continue Player ship system(1/2). Computer boat placement. POLISH SYSTEM


#Effects=====================================================

def wait():
  for i in range(1,4):
    time.sleep(1)
    print('.')

def win():
  global game
  global playerwin
  winner = ['Y','O','U','.','W','I','N','!','!']
  os.system('clear')
  for i in winner:
    print(i)
    time.sleep(0.5)
  
  input('\nPress Enter to return to lobby')
  playerwin+=1
  os.system('clear')
  game = False

def lose():
  global game
  global computerwin
  losser = ['Y','O','U','.','L','O','S','T','!']
  os.system('clear')
  for i in losser:
    print(i)
    time.sleep(0.5)
  
  
  input('\nPress Enter to return to lobby')
  computerwin+=1
  os.system('clear')
  game = False

#==============================================================


playerwin = 0
computerwin = 0


#Computer

#display
# a = ['_','_','_','_','_','_','_','_',]
# b = ['_','_','_','_','_','_','_','_',]
# c = ['_','_','_','_','_','_','_','_',]
# d = ['_','_','_','_','_','_','_','_',]
# e = ['_','_','_','_','_','_','_','_',]
# f = ['_','_','_','_','_','_','_','_',]
# g = ['_','_','_','_','_','_','_','_',]
# h = ['_','_','_','_','_','_','_','_',]

# #comphidden
# a2 = ['_','_','_','_','_','_','_','_',]
# b2 = ['_','_','_','_','_','_','_','_',]
# c2 = ['_','_','_','_','_','_','_','_',]
# d2 = ['_','_','_','_','_','_','_','_',]
# e2 = ['_','_','_','_','_','_','_','_',]
# f2 = ['_','_','_','_','_','_','_','_',]
# g2 = ['_','_','_','_','_','_','_','_',]
# h2 = ['_','_','_','_','_','_','_','_',]


# #player
# a1 = ['_','_','_','_','_','_','_','_',]
# b1 = ['_','_','_','_','_','_','_','_',]
# c1 = ['_','_','_','_','_','_','_','_',]
# d1 = ['_','_','_','_','_','_','_','_',]
# e1 = ['_','_','_','_','_','_','_','_',]
# f1 = ['_','_','_','_','_','_','_','_',]
# g1 = ['_','_','_','_','_','_','_','_',]
# h1 = ['_','_','_','_','_','_','_','_',]



def menu():
  print('{:^20}'.format('|Battleship|'))
  
  print('')
  print('{:^18}'.format(' 1.Intro'))
  print('{:^18}'.format(' 2.Play'))
  print('{:^18}'.format(' 3.Score'))
  print('{:^18}'.format('4.Exit'))
  print('')
  
def score():
  print(f'\n|Your wins: {playerwin}| Vs |Computer wins: {computerwin}|')
  input('\n\nPress Enter to return to Lobby.')


def display():

  print('{:^51}'.format('|Computer area|'))
  print('{:^10}''{:^}''{:^11}''{:<5}''{:^4}''{:^7}''{:^5}''{:^7}'.format('1','2','3','4','5','6','7','8'))
 #A
  # for i in range(len(board)):
  #   print(f'{board[0]} [ {board[i][0]} ] [ {board[i][1]} ] [ {board[i][2]} ] [ {board[i][3]} ] [ {board[i][4]} ] [ {board[i][5]} ] [ {board[i][6]} ] [ {board[i][7]} ] [ {board[i][8]} ] [ {board[i][9]} ]')
    
  #computer

  

  print(f'A [ {a[0]} ] [ {a[1]} ] [ {a[2]} ] [ {a[3]} ] [ {a[4]} ] [ {a[5]} ] [ {a[6]} ] [ {a[7]} ]')
 #B
  print(f'B [ {b[0]} ] [ {b[1]} ] [ {b[2]} ] [ {b[3]} ] [ {b[4]} ] [ {b[5]} ] [ {b[6]} ] [ {b[7]} ]')
 #C
  print(f'C [ {c[0]} ] [ {c[1]} ] [ {c[2]} ] [ {c[3]} ] [ {c[4]} ] [ {c[5]} ] [ {c[6]} ] [ {c[7]} ]')
 #D
  print(f'D [ {d[0]} ] [ {d[1]} ] [ {d[2]} ] [ {d[3]} ] [ {d[4]} ] [ {d[5]} ] [ {d[6]} ] [ {d[7]} ]')
 #E
  print(f'E [ {e[0]} ] [ {e[1]} ] [ {e[2]} ] [ {e[3]} ] [ {e[4]} ] [ {e[5]} ] [ {e[6]} ] [ {e[7]} ]')
 #F
  print(f'F [ {f[0]} ] [ {f[1]} ] [ {f[2]} ] [ {f[3]} ] [ {f[4]} ] [ {f[5]} ] [ {f[6]} ] [ {f[7]} ]')
 #G
  print(f'G [ {g[0]} ] [ {g[1]} ] [ {g[2]} ] [ {g[3]} ] [ {g[4]} ] [ {g[5]} ] [ {g[6]} ] [ {g[7]} ]')
 #H 
  print(f'H [ {h[0]} ] [ {h[1]} ] [ {h[2]} ] [ {h[3]} ] [ {h[4]} ] [ {h[5]} ] [ {h[6]} ] [ {h[7]} ]')  
  print('-'*50)

  #================Player====================================================**************************************************************************

  print('{:^51}'.format('|Your Area|'))
  print('{:^10}''{:^}''{:^11}''{:<5}''{:^4}''{:^7}''{:^5}''{:^7}'.format('1','2','3','4','5','6','7','8'))

  print(f'A [ {a1[0]} ] [ {a1[1]} ] [ {a1[2]} ] [ {a1[3]} ] [ {a1[4]} ] [ {a1[5]} ] [ {a1[6]} ] [ {a1[7]} ]')
 #B
  print(f'B [ {b1[0]} ] [ {b1[1]} ] [ {b1[2]} ] [ {b1[3]} ] [ {b1[4]} ] [ {b1[5]} ] [ {b1[6]} ] [ {b1[7]} ]')
 #C
  print(f'C [ {c1[0]} ] [ {c1[1]} ] [ {c1[2]} ] [ {c1[3]} ] [ {c1[4]} ] [ {c1[5]} ] [ {c1[6]} ] [ {c1[7]} ]')
 #D
  print(f'D [ {d1[0]} ] [ {d1[1]} ] [ {d1[2]} ] [ {d1[3]} ] [ {d1[4]} ] [ {d1[5]} ] [ {d1[6]} ] [ {d1[7]} ]')
 #E
  print(f'E [ {e1[0]} ] [ {e1[1]} ] [ {e1[2]} ] [ {e1[3]} ] [ {e1[4]} ] [ {e1[5]} ] [ {e1[6]} ] [ {e1[7]} ]')
 #F
  print(f'F [ {f1[0]} ] [ {f1[1]} ] [ {f1[2]} ] [ {f1[3]} ] [ {f1[4]} ] [ {f1[5]} ] [ {f1[6]} ] [ {f1[7]} ]')
 #G
  print(f'G [ {g1[0]} ] [ {g1[1]} ] [ {g1[2]} ] [ {g1[3]} ] [ {g1[4]} ] [ {g1[5]} ] [ {g1[6]} ] [ {g1[7]} ]')
 #H 
  print(f'H [ {h1[0]} ] [ {h1[1]} ] [ {h1[2]} ] [ {h1[3]} ] [ {h1[4]} ] [ {h1[5]} ] [ {h1[6]} ] [ {h1[7]} ]')  
  print('-'*50)
  ships()
  
# Guide/ intro =============***********************************************
def intro():
  print('Welcome to battleship!...')
  wait()
  print('dont press anything yet! this is still the intro!')
  wait()
  print('In this version the playing area is 8x8 compared to the original 10x10')
  wait()
  print('Play againts a computer.')
  wait()
  print('The rules are simple')
  wait()
  print('-O means miss and X is a confirmed hit on the ship')
  print('-The computer battle ships will be hidden and yours will be hidden from the computer too')
  print('-Keep in mind of orientation and spacing of one boat to another')
  print('Your wins are stored under the 2.score in main menu')
  wait()
  print('Ships have 2 orientation(Horizontal and vertical)')
  print('horizontal ships will be made out of these (<) while vertical will be made out of (A)  ')
  wait()
  print('That is all! goodluck!')
  input('press enter to return main menu')

#========================Computer play==================================



def compplay():
  global z
  
  global compscore

  x = 1
  y1 = 1
  y2 = 1 
  y3 = 1
  y4 = 1
  y5 = 1
  y6 = 1
  y7 = 1
  y8 = 1
  
  letter = random.randint(1,8)
  while True:
    if letter == x and 1 == y1:
      letter = a1
      break
    elif letter == x+1 and 1 == y2:
      letter = b1
      break
    elif letter == x+2 and 1 == y3:
      letter = c1
      break
    elif letter == x+3 and 1 == y4:
      letter = d1
      break
    elif letter == x+4 and 1 == y5:
      letter = e1
      break
    elif letter == x+5 and 1 == y6:
      letter = f1
      break
    elif letter == x+6 and 1 == y7:
      letter = g1
      break
    elif letter == x+7 and 1 == y8:
      letter = h1
      break
    else:
      x+=1
  

  Ccords = random.randint(0,7)
  if letter[Ccords] == '_':
    letter[Ccords] = "O"
  
  
  
  
  elif letter[0] == 'O' or letter[0] == 'X' and letter[1] == 'O' or letter[1] == 'X'and letter[2] == 'O' or letter[2] == 'X' and letter[3] == 'O' or letter[3] == 'X'and letter[4] == 'O' or letter[4] == 'X'and letter[5] == 'O' or letter[5] == 'X' and letter[6] == 'O' or letter[6] == 'X'and letter[7] == 'O' or letter[7] == 'X':
    if letter == a1:
      y1 = 0
    elif letter == b1:
      y2 = 0
    elif letter == c1:
      y3 = 0
    elif letter == d1:
      y4 = 0
    elif letter == e1:
      y5 = 0
    elif letter == f1:
      y6 = 0
    elif letter == g1:
      y7 = 0
    elif letter == h1:
      y8 = 0
  

  elif letter[Ccords] != '_' and letter[Ccords] != 'O':
    letter[Ccords] = "X"
    compscore += 1
#====================Computer Placement=========================

def aiship():

  # shaip1=0
  # shaip2=0
  # shaip3=0
  # shaip4=0
  # shaip5=0

  aishipcount =[]

  while len(aishipcount) != 5:
    shaip1=0
    shaip2=0
    shaip3=0
    shaip4=0
    shaip5=0
    
    randomship = random.randint(1,5)
    aiYcord = random.randint(1,8)
    aiXcord = random.randint(0,7)
    
    if aiYcord == 1 :
      aiYcord= a2
    elif aiYcord == 2 :
      aiYcord = b2
    elif aiYcord == 3 :
      aiYcord = c2
    elif aiYcord == 4 :
      aiYcord = d2
    elif aiYcord == 5 :
      aiYcord = e2
    elif aiYcord == 6 :
      aiYcord= f2
    elif aiYcord == 7 :
      aiYcord = g2
    elif aiYcord == 8 :
      aiYcord = h2




    if  randomship == 1:
      if shaip1 == 0:
        if (aiXcord-1) + 4 <= 8 and aiYcord[(aiXcord-1)+3] == '_':

          for i in range(4):
            aiYcord[aiXcord-1] = '<'
            aiXcord += 1

          aishipcount.append(1)
          shaip1 += 1
        else:
          pass
    elif  randomship == 2:
      if shaip2 == 0:
        if (aiXcord-1) + 5 <= 8 and aiYcord[(aiXcord-1)+4] == '_':

          for i in range(5):
            aiYcord[aiXcord-1] = '<'
            aiXcord += 1
          aishipcount.append(1)
          shaip2 += 1
        else:
          pass
    elif  randomship == 3:
      if shaip3 == 0:
        if (aiXcord-1) + 3 <= 8 and aiYcord[(aiXcord-1)+2] == '_':

          for i in range(3):
            aiYcord[aiXcord-1] = '<'
            aiXcord += 1
          aishipcount.append(1)
          shaip3 += 1
        else:
          pass
    elif  randomship == 4:
      if shaip4 == 0:
        if (aiXcord-1) + 3 <= 8 and aiYcord[(aiXcord-1)+2] == '_':

          for i in range(3):
            aiYcord[aiXcord-1] = '<'
            aiXcord += 1
          aishipcount.append(1)
          shaip4 += 1
        else:
          pass
    elif  randomship == 5:
      if shaip5 == 0:
        if (aiXcord-1) + 2 <= 8 and aiYcord[aiXcord] == '_':

          for i in range(2):
            aiYcord[aiXcord-1] = '<'
            aiXcord += 1
          aishipcount.append(1)
          shaip5 += 1
        else:
          pass



#=======================|PLAYER FUNCTIONS|==================================
def ships():
  print('1.| <<<< : Battleship : 4 boxes')
  print('2.| <<<<<< : Carrier : 5 boxes')
  print('3.| <<< : Destroyer : 3 boxes')
  print('4.| <<< : Submarine : 3 boxes')
  print('5.| << : boat : 2 boxes')



#======================================================

def playersetup():
  global confirm
  global ship
  global vh

 

  ship1=0
  ship2=0
  ship3=0
  ship4=0
  ship5=0
  shipcount = []
  sublist = []

  #vertical or horizontal
  while True:
    os.system('clear')
    display()
    
    confirm = False
    #confirm system=====================================
    try:
      if len(shipcount) == 5:
        try:
          confirm = input('Confirm Setup *this will automatically move to attack mode* \ntype ->(y)yes:')
          if confirm.lower() == 'y':
            confirm = True
            break
        # elif confirm.lower() == 'n':
        #   try:
        #     delete = int(input('pick ship to delete (1-5)'))
        #     if delete == 1:
        #       shipcount.pop(0)

        #   except ValueError:
        #     input('Wrong input... Press Enter')
        except ValueError:
          input('Wrong input... Press Enter')
        
          

    except NameError:
      input('Wrong input... Press Enter')

    #Main setup system============================================
    try:
      ship = int(input('\nChoose ship to place (1-5) :'))
      vh = str(input('Vertical or horizontal? (type v or h) :'))
      try:
        Ysetup = str(input('Input letter/Y coordinate (A-H) :'))
        placeX = int(input('Input X coordinate (1-8) :'))
        
        if Ysetup.lower() == 'a' :
          placeY= a1
        elif Ysetup.lower() == 'b' :
          placeY = b1
        elif Ysetup.lower() == 'c' :
          placeY = c1
        elif Ysetup.lower() == 'd' :
          placeY = d1
        elif Ysetup.lower() == 'e' :
          placeY = e1
        elif Ysetup.lower() == 'f' :
          placeY= f1
        elif Ysetup.lower() == 'g' :
          placeY = g1
        elif Ysetup.lower() == 'h' :
          placeY = h1
        
        if placeY[placeX-1] == '<' or placeY[placeX-1] == 'A':
              input('Space already occupied... Press Enter')
        
        else:

          if vh.lower() == 'v':
            input('Underconstruction.. press enter')
            # if ship == 1:
            #   if ship1 == 0:
            #     if placeY[placeX-1] != f1 and e1[placeX-1] == '_':
                  
            #       try:
                          
            #         for i in range(4):
            #           placeY[placeX-1] = 'A'
            #           vertical()
                    
                      
            #         ship1 += 1

                  
            #       except IndexError:
                    
            #         input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
            #     else:
            #       input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
            #   else:
            #     input('You only can use this ship once... Press Enter')

          elif vh.lower() == 'h':
            

            if ship == 1:
              if ship1 == 0:
                if (placeX-1) + 4 <= 8 and placeY[(placeX-1)+3] == '_':
                  
                  try:
                    sublist.append(placeY)
                    sublist.append(placeX)
                    shipcount.append(sublist)

              

                    for i in range(4):
                      placeY[placeX-1] = '<'
                      placeX += 1
                  
                   
                    ship1 += 1

                  
                  except IndexError:
                    
                    input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
                else:
                  input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
              else:
                input('You only can use this ship once... Press Enter')
            if ship == 2:
              if ship2 == 0:
                if (placeX-1) + 5 <= 8 and placeY[(placeX-1)+4] == '_' :
                  try:
                    sublist.append(placeY)
                    sublist.append(placeX)
                    shipcount.append(sublist)
                    for i in range(5):
                      placeY[placeX-1] = '<'
                      placeX += 1 
                    
                    
                   
                    ship2 += 1
                  except IndexError:
                    debug()
                    input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
                else:
                  input('Error OutofBound.Ship please makesure the ship fits... Press Enter') 
              else:
                input('You only can use this ship once... Press Enter')

            if ship == 3:
              if ship3 ==0:
                if (placeX-1) + 3 <= 8 and placeY[(placeX-1)+2] == '_':
                  
                  try:
                    sublist.append(placeY)
                    sublist.append(placeX)
                    shipcount.append(sublist)
                    for i in range(3):
                      placeY[placeX-1] = '<'
                      placeX += 1 
                    
                    ship3 += 1  
                  except IndexError:
                    input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
                else:
                  input('Error OutofBound.Ship please makesure the ship fits... Press Enter') 
              else:
                input('You only can use this ship once... Press Enter')
            if ship == 4:
              if ship4 == 0:
                if (placeX-1) + 3 <= 8 and placeY[(placeX-1)+2] == '_':
                  try:
                    sublist.append(placeY)
                    sublist.append(placeX)
                    shipcount.append(sublist)
                    for i in range(3):
                      placeY[placeX-1] = '<'
                      placeX += 1
                    
                    ship4 += 1 
                  except IndexError:
                    input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
                else:
                  input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
              else:
                input('You only can use this ship once... Press Enter')
            if ship == 5:
              if ship5 == 0:
                if (placeX-1) + 2 <= 8 and placeY[(placeX)] == '_':
                  try:
                    sublist.append(placeY)
                    sublist.append(placeX)
                    shipcount.append(sublist)
                    for i in range(2):
                      placeY[placeX-1] = '<'
                      placeX += 1 
                    
                    ship5 += 1
                  except IndexError:
                    input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
                else:
                  input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
              else:
                input('You only can use this ship once... Press Enter')

      except NameError or ValueError:
        input('Wrong input... Press Enter')



    except ValueError or NameError:
      input('Wrong input... Press Enter')

def debug():
  global placeY
  global placeX
  if IndexError:
    for i in range(4):
      placeY[placeX-1] = '_'
      placeX += 1


def vertical():
  global num
  global Ysetup
  global placeY
  
  if placeY == a1:
    placeY = b1
    return
  elif placeY == b1:
    placeY = c1
    return
  elif placeY == c1:
    placeY = d1
    return
  elif placeY == d1:
    placeY = e1
    return
  elif placeY == e1:
    placeY = f1
    return
  elif placeY == f1:
    placeY = g1
    return
  elif placeY == g1:
    placeY = h1
    return



# Player score/ ATtack===============





def playerattack():
  global computermove
  global player
  try:
    letter1 = (input('Type letter(Y coordinate)(a-h) :'))
    xcord = int(input('Type x cordinate (1-8) :'))
  
    if letter1.lower() == 'a' :
      ycord = a
    elif letter1.lower() == 'b' :
      ycord = b
    elif letter1.lower() == 'c' :
      ycord = c
    elif letter1.lower() == 'd' :
      ycord = d
    elif letter1.lower() == 'e' :
      ycord = e
    elif letter1.lower() == 'f' :
      ycord = f
    elif letter1.lower() == 'g' :
      ycord = g
    elif letter1.lower() == 'h' :
      ycord = h
    
    if letter1.lower() == 'a' :
      hidden = a2
    elif letter1.lower() == 'b' :
      hidden = b2
    elif letter1.lower() == 'c' :
      hidden = c2
    elif letter1.lower() == 'd' :
      hidden = d2
    elif letter1.lower() == 'e' :
      hidden = e2
    elif letter1.lower() == 'f' :
      hidden = f2
    elif letter1.lower() == 'g' :
      hidden = g2
    elif letter1.lower() == 'h' :
      hidden = h2
 
    


    if hidden[xcord-1] == '<' or hidden[xcord-1] =='A':
      ycord[xcord-1]='X'
      hidden[xcord-1] ='X'
      print('Enemy ship HIT!')
      time.sleep(2.5)
      computermove = True

      player += 1
    
    else:
      ycord[xcord-1]='O'
      hidden[xcord-1] ='O'
      computermove = True

  except NameError or ValueError:

    input('Wrong input... Press Enter')
    computermove = False

#========MAIN SYSTEM============================================

while True:
  os.system('clear')
  game = True
  confirm = False
  aistop = False
  player = 0
  compscore = 0

  #display
  a = ['_','_','_','_','_','_','_','_',]
  b = ['_','_','_','_','_','_','_','_',]
  c = ['_','_','_','_','_','_','_','_',]
  d = ['_','_','_','_','_','_','_','_',]
  e = ['_','_','_','_','_','_','_','_',]
  f = ['_','_','_','_','_','_','_','_',]
  g = ['_','_','_','_','_','_','_','_',]
  h = ['_','_','_','_','_','_','_','_',]

  #comphidden
  a2 = ['_','_','_','_','_','_','_','_',]
  b2 = ['_','_','_','_','_','_','_','_',]
  c2 = ['_','_','_','_','_','_','_','_',]
  d2 = ['_','_','_','_','_','_','_','_',]
  e2 = ['_','_','_','_','_','_','_','_',]
  f2 = ['_','_','_','_','_','_','_','_',]
  g2 = ['_','_','_','_','_','_','_','_',]
  h2 = ['_','_','_','_','_','_','_','_',]


  #player
  a1 = ['_','_','_','_','_','_','_','_',]
  b1 = ['_','_','_','_','_','_','_','_',]
  c1 = ['_','_','_','_','_','_','_','_',]
  d1 = ['_','_','_','_','_','_','_','_',]
  e1 = ['_','_','_','_','_','_','_','_',]
  f1 = ['_','_','_','_','_','_','_','_',]
  g1 = ['_','_','_','_','_','_','_','_',]
  h1 = ['_','_','_','_','_','_','_','_',]
  menu()
  try:
    #main Components*************************************************


    menuselect = int(input('Type choice (1-4) :'))
    os.system('clear')
    
    #PLAY==============================================================
    if menuselect == 2:
      while game == True:
        os.system('clear')
        if compscore == 17:
          lose()
          game = False
          break
        elif player == 17:
          win()
          game = False
          break
        display()
        
        while confirm == False:
          os.system('clear')
          playersetup()
        if aistop == False:
          aiship()
          aistop = True

        os.system('clear')
        display()
        print('\n|Attack mode|\n')
        
        time.sleep(3)
        playerattack()
        os.system('clear')
        display()
        if computermove != False:
          print('\n\nCOMPUTER TURN')
          time.sleep(2)
          compplay()
        elif computermove == False:
          game=True
          computermove = True
          continue




    
    #Score==============================================================
    elif menuselect == 3:
      score()
    #Extra stuff*****************************************************
    #intro
    elif menuselect == 1:
      intro()

    #Exit
    elif menuselect == 4:
      break
  
  
  
  
  except ValueError:
    input('Wrong input... Press Enter')




#*********************Idea pit*******************************


#   if placeY[(placeX-1)+4]>placeY[7]:
#                   input('Error OutofBound.Ship please makesure the ship fits... Press Enter')
                  
#                 else:
#                   for i in range(4):
#                     placeY[placeX-1] = '<'
#                     placeX += 1
                  
#                   shipcount.append(1)
#                   ship1 += 1


# y = input('pick ship to delete')

# a1 = ['_','_','_','_','_','_','_','_']
#           b1 = ['_','_','_','_','_','_','_','_']
#           c1 = ['_','_','_','_','_','_','_','_']
#           d1 = ['_','_','_','_','_','_','_','_']
#           e1 = ['_','_','_','_','_','_','_','_']
#           f1 = ['_','_','_','_','_','_','_','_']
#           g1 = ['_','_','_','_','_','_','_','_']
#           h1 = ['_','_','_','_','_','_','_','_']