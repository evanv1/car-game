import sys


started = False
command = ""
while True:
      command = input('> ')
      if command == "start":
          if started:
              print('car is already started')
          else: 
             started = True     
             print(f'car is started')

      elif command == "stop":
          if started != True:
              print('car is already stopped!')
          else:
              started = False   
              print(f'car stopped')

      elif command == "quit":
          break
      elif command == "help":
          print('''
start - starts car 
stop - stops car
help - displays help
quit - quits app'''
          )
      else:
          print('not recognized.') 