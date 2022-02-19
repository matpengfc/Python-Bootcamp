# Day 3
# ASCII art at https://ascii.co.uk/art

print('''
                                                                   ,-,
                                                             _.-=;~ /_
                                                          _-~   '     ;.
                                                      _.-~     '   .-~-~`-._
                                                _.--~~:.             --.____88
                              ____.........--~~~. .' .  .        _..-------~~
                     _..--~~~~               .' .'             ,'
                 _.-~                        .       .     ` ,'
               .'                                    :.    ./
             .:     ,/          `                   ::.   ,'
           .:'     ,(            ;.                ::. ,-'
          .'     ./'.`.     . . /:::._______.... _/:.o/
         /     ./'. . .)  . _.,'               `88;?88|
       ,'  . .,/'._,-~ /_.o8P'                  88P ?8b
    _,'' . .,/',-~    d888P'                    88'  88|
 _.'~  . .,:oP'        ?88b              _..--- 88.--'8b.--..__
:     ...' 88o __,------.88o ...__..._.=~- .    `~~   `~~      ~-._ Seal _.
`.;;;:='    ~~            ~~~                ~-    -       -   -
''')
print("Welcome to Fox Island.")
print("Your mission is to find the treasure.")

level_1 = input('You\'re at a crossroad. Where do you want to go> Type "left" or "right" ')
if level_1.lower() != "left":
    print("You fell into a hole. Game Over.")
else:
    level_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if level_2.lower() != "wait":
        print("You get attacked by an angry trout. Game Over.")
    else:
        level_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if level_3.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif level_3.lower() == "blue":
            print("You enter a room of beasts. Game Over.")
        elif level_3.lower() == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")

print("The End")
    


