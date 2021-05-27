def madlib():
    adj1 = input('Adjective: ')
    adj2 = input('Another adjective: ')
    part1 = input('Body part: ')
    noun1 = input('Noun: ')
    emotion = input('Emotion: ')
    noun2 = input('Another noun: ')

    madlib = f"I've got some bad news for you bro, I've put the {adj1} curse on you. \
        Odds are you'll begin to feel {adj2} around your {part1}. \
        It will probably resemble something like a {noun1}. \
        Don't waste too much time feeling {emotion}, because living is all about {noun2}."

    print(madlib)
