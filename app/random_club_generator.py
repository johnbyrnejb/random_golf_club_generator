import random

clubs = ['Dr',
         '3 Wood',
         'Hybrid',
         '4 Iron',
         '5 Iron',
         '6 Iron',
         '7 Iron',
         '8 Iron',
         '9 Iron',
         'PW',
         'Gap Wedge',
         'Lob Wedge'
         ]


def select_random_club():
    random_club = random.choice(clubs)
    return f'Your random club is {random_club}'
