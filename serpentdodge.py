name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
if age <= 17:
    print('Sorry! This game features mildly graphic scenarios & you must be 18 years old to play!')
    print('Feel free to reboot and lie about your age ;)')
else:
    print(f'Welcome to Serpent Dodge, {name}!')
    admission = input('Would you like to play? (y/n) ')
    if admission == 'y':
        print('Let the journey begin!')
        hp = 10
        print(f'You are beginning with {hp} HP.')
        print('At the start of your adventure, you have encountered a massive body of water.')
        across_or_around = input('Do you wish to swim across it or walk around? (swim/walk) ')
        if across_or_around == 'walk':
            print('Bad news! You encountered a Martian Pygmy Serpent which was 300 feet in length and were promptly swallowed whole. R.I.P.')
        elif across_or_around == 'swim':
            print('Congratulations on selecting the safer option! You paddled to the furthest shore unscathed.')
            print('Next, you have encountered a fairly large brush which is serving as a blockade on your path.')
            chop_or_flee = input('Do you wish to spend an hour chopping through the brush or find a new route? (chop/flee) ')
            if chop_or_flee == 'chop':
                print('Bad news! At the base of the brush was an extremely transparent Nail Python who bit you in your jugluar vein! R.I.P.')
            elif chop_or_flee == 'flee':
                print('Congratulations! A new path made itself available to you after only moments of searching.')
                camp_or_continue = input('It is getting dark now. Do you wish to find an alcove to camp in or forage on into the unknown? (camp/continue) ')
                if camp_or_continue == 'continue':
                    print('Bad news! You were confronted by a Limnal Star Python a quarter mile down the trail and it constricted you until suffocation. R.I.P.')
                elif camp_or_continue == 'camp':
                    print('Excellent choice! You survived the night and the Sun is now rising.')
                    east_or_west = input('There appears to be a storm coming in from the west. Do you wish to contine towards it or head more east? (east/west) ')
                    if east_or_west == 'east':
                        print('So be it.')
                        descend_or_go_around = input('There is a cliff with a massive overhang and no realistic way of getting around it. Do you wish to descend the cliff or walk alongside until it appears easier to cross? (descend/walk) ')
                        print('Bad news! An earthquake shook you off the ledge and you fell to your death. R.I.P.')
                    elif east_or_west == 'west':
                        print('So be it.')
                        print('The clouds are becoming lower in the sky and a cold wind blows...')
                        ladder = input('A makeshift jungle ladder appears alongside the trail. Do you wish to climb it beyond the vibility of the rainforest treeline or ignore it? (climb/ignore) ')
                        if ladder == 'ignore':
                            print('Very well.')
                            input('A 523 foot Blazer Serpent has emerged along the path! Do you wish to flee or attempt to battle it? (flee/battle) ')
                            print('Your advances were no match for this anomaly of nature and you were made into supper! R.I.P.')
                        elif ladder == 'climb':
                            print('The view is astounding.')
                            hut = input('A hut appears at the tip of the ladder. Do you wish to inspect or descend the ladder? (inspect/descend) ')
                            if hut == 'descend':
                                print('Bad news! You lost your grip descending the ladder and fell to your death. R.I.P.')
                            elif hut == 'inspect':
                                rest_or_descend = input('There is a makeshift cot within the hut. Do you wish to rest for a while or venture back down? (rest/descend) ')
                                if rest_or_descend == 'descend':
                                    print('Bad news! You lost your grip descending the ladder and fell to your death. R.I.P.')
                                elif rest_or_descend == 'rest':
                                    print('Bad news! The resident of the hut returned from hunting and has imprisoned you. The tussle cost you 5 HP.')
                                    hp = 5 
                                    escape_or_chill = input('Now you are in a bamboo jail cell. Do you wish to attempt to escape or lay low as to not upset your captor? (escape/chill) ')
                                    if escape_or_chill == 'chill':
                                        print('Bad news! The captor shape-shifted into a 200 foot long prehistoric Cave Stone Cobra and ate you promptly. R.I.P.')
                                    elif escape_or_chill == 'escape':
                                        print('You have managed to escape your cell, but only to witness your captor transform into a 200 foot long prehistoric Cave Stone Cobra!')
                                        print('Its eyes are sapphire blue and its tongue has over 30 point jutting out violently in all directions.')
                                        strike_or_flee = input('Do you wish to strike the cobra or attempt to flee? (strike/flee) ')
                                        if strike_or_flee == 'flee':
                                            print('Bad news! The Cave Stone Cobra is capable of teleportation and blocked your escape by swallowing you whole. R.I.P.')
                                        elif strike_or_flee == 'strike':
                                            print('The strike was partially effective. It whipped you with its tail and cost you 3 HP.')
                                            hp = 3
                                            heal_or_battle = input('Do you wish to produce and consume a healing potion from your person or carry on with the fight? (heal/battle) ')
                                            if heal_or_battle == 'heal':
                                                print('Bad news! The time you wasted amounted in the cobra gaining on you and piercing your skull with its tongue. R.I.P.')
                                            elif heal_or_battle == 'battle':
                                                print('Your bravery was greatly rewarded. Upon jumping to dodge a jab from the cobras tongue, you manage to grab on to the top of its head.')
                                                print('It attempted to shake you off, but your grip was too strong and you levereged it to twist its head 180 degrees.')
                                                print('After a few moments, it stopped resisting and accepted its own fate.')
                                                feast_or_continue = input('Now that the cobra has been defeated, do you wish to feast on the flesh of the beast or carry on your path? (feast/continue) ')
                                                if feast_or_continue == 'feast':
                                                    print('Bad news! Every inch of the cobra was poisonous! You collapse in frailty until you submit to cardiac arrest. R.I.P.')
                                                elif feast_or_continue == 'continue':
                                                    print('Wise choice. The path is clear and your boots squish victoriously in the mud leftover from the passing storm.')
                                                    print('Only a mere 2 miles ahead, you arrive at the city of El Dorado where you are greeted by 27 beautiful virgins and a celebratory feast of fruits and delicacies which would satisfy the highest of royalty.')
                                                    print(f'The journey was the expedition of a lifetime, and your title was solidified by the legends of time: "{name}: Dodger Of Serpents".') 
    else:
        print('See you later!')
