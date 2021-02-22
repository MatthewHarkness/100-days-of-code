import random

adj1 = ['is the colour of', 'is the maiden name of', 'is the point of', 'is the worst part of', 'is your favourite thing about',
    'was the hometown of', 'is the last name of', 'is the most kissable part of', 'is crispy about', 'is', 'was the collage of',
    'is the birthday of', 'was your reaction when you heard about', 'would like to know about', 'is innovative about',
    'is stopping you from seeing', 'is the favourite location of'
    ]
adj2 = ['your latest', "your mother's", "your father's", "your aunty's", 'the latest',
    "your best friend's", "your grandmother's", "the US president's", "Bill Gates'",
    "a gremlin's", "the Prime Minister of the UK's", "Australia's", 'your']

noun = ['dog', 'brother', 'boyfriend', 'mother', 'home town', 'pet', 'fish',
    'cat', 'lover', 'house', 'fast car', 'friend', 'personal CTHULHU', 'maiden', 'pringle',
    'fad', 'internet history', 'butt', 'face', 'girlfriend', 'nuclear bomb', 'program', 'favourite number',
    'favourite colour', 'favourite candy', 'favourite child', 'childhood nickname', 'Queen']

x = random.randrange(0, len(adj1))
y = random.randrange(0, len(adj2))
z = random.randrange(0, len(noun))

#What is the colour of your last dog?
print()
print('What ' + adj1[x] + ' ' + adj2[y] + ' ' + noun[z] +'?')
print()