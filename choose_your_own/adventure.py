print('Welcome to Serpent Dodge!')
name = input('What is your name? ')
age = int(input('How old are you? '))
print('Hello', name, 'you are', age, 'years old.')
health = 10
if age >= 18:
    print('You are old enough to play!')
    wants_to_play = input('Do you want to play Serpent Dodge? (y/n) ').lower()
    if wants_to_play == 'y':
        print('Let\'s go!')
        print('You are starting out with', health, 'health.')
        left_or_right = input('First decision... Left or right? (left/right) ')
        if left_or_right == 'left':
            print('Well done, you followed the path and reached a lake. ') 
            across_or_around = input('Do you want to swim across or go around? (across / around) ')
            if across_or_around == 'around':
                print('You went around and reached the other side of the lake.')
            elif across_or_around == 'across':
                print('You swam across and were bit by a snake, and unfortunately lost 5 HP.')
                health -=5
                print('Next you have approached a massive log in the path.')
                above_or_around = input('Do you wish to go above or around? (above/around) ')
                if above_or_around == 'above':
                    print('Way to stay alive!')
                    print('OK so a 128 foot serpent has appeared along the path.')
                    print('You have two choices at defeating it, wielding your broadsword and decaptitating it or grabbing its tail and performing a ricohet-style decapitation.')
                    sword_or_snap = input('What is your move? (broadsword/ricohet)' )
                    if sword_or_snap == 'broadswod':
                        print('Bad news, your broadsword draw was not fast enough and you were venomized to death. R.I.P.')               
                    elif sword_or_snap == 'ricochet':
                        print('This was unexpectedly effective and the serpent was annihilated. You continue onwards to the city of El Dorado.')
                        print('Very well played!')
                    else:
                        print('Your lack of a valid answer caused a degree of procrostination which ammounted to you being swallowed alive! R.I.P.')
                else:
                    print('Bad news! There was a 300 foot anaconda tha swallowed you whole on the periphery of the log. R.I.P.')
        else:
            print('You fell into a pothole and died!')
    else:
        print('Later!')
else:
    print('Sorry, you are not old enough to play!')
