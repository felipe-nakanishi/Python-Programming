
#function of computer's move:
def computer_choose(n,m):
  for x in range(1,m+1): #return the value of x, if this value let a number of pieces multiple of m+1.
    if (n-x) % (m+1) == 0:
      return x
      break #if the function is interrupted, it means that it isn't possible to let a 'n' multiple of m+1 for the player, so we must to take out the max number possible of pieces.
  return m

#prompts for the user to make his move:
def user_choose(n,m):
  while True:
    play = int(input('How many pieces are you taking?'))
    if play > 0 and play <= m:
      break
    print('Oops! invalid try! try again.')
  return play

#function that makes the match:
def match():
  n = int(input('How many pieces?')) #get the number of pieces in the match.
  m = int(input('What is the limit of pieces per round?')) #get the limit of pieces per round in the match.
  if n % (m+1) == 0: #if the number is divisible for m+1 then the user starts.
    print('\nYou start!\n')
    while (n>0):
      user = user_choose(n,m) #takes the user's move and remove it from the total number of pieces in the game.
      n=n-user
      print('you took {} piece(s) and now there are {} remaining piece(s)'.format(user, n))
      if n == 0: #if the total number of pieces remaining is 0 then the user won.
        return print('You won!')
        break
      computer = computer_choose(n,m) #takes the computer's move and remove it from the total number of pieces in the game.        
      n=n-computer
      print('the computer removed {} piece(s) and now there are {} remaining piece(s)'.format(computer, n))
      if n == 0:
        return print('The computer won!') #if the total number of pieces remaining is 0 then the computer won.
        break
  else:
      print('Computer starts!')
      while (n>0):
        computer = computer_choose(n,m) #takes the computer's move and remove it from the total number of pieces in the game.
        n=n-computer
        print('the computer removed {} piece(s) and now there are {} remaining piece(s)'.format(computer, n)) 
        if n == 0:
          return print('The computer won!') #if the total number of pieces remaining is 0 then the computer won.
          break
        user = user_choose(n,m) #takes the user's move and remove it from the total number of pieces in the game.
        n=n-user
        print('you removed {} piece(s) and now there are {} remaining piece(s)'.format(user, n)) 
        if n == 0: 
          return print('you won!') #if the total number of pieces remaining is 0 then the user won.
          break

#function that creates the championship:
def championship():
    #scores:
    user = 0
    computer = 0
    #runs 3 times:
    for _ in range(3):
      #runs the match:
      winner = match()
      #verifies the result:
      if winner == 1:
        user += 1
      else:
        computer = computer + 1

    #Shows the final score:
    print("Final Score: You {} x {} Computer".format(user, computer))

#start the game of NIM: 
print('Welcome to the NIMs game! Choose:')
mode = int(input('1 - to play only one game\n2 - to play a championship\n')) #prompts for the user to choose if he wants to play only one game or a championship.
if mode == 1:
  print('you chose an isolate match!')
  match() #if the user type 1 then calls the match function. 
elif mode == 2:
  print('you chose a championship!')
  championship() #if the user type 2 then calls the championship function.

