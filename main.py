# Generate the UNO deck of 108 cards
# -19x Red, 19x Yellow, 19x Blue,19x Green, 
# -8x Draw Two(2x Draw Two Red, 2x Draw Two Yellow, 2x Draw two Blue, 2x Draw Two Green)
# -8x Skip, 
# -8x Reverse (2x of each colour),
# -4x Wild, 
# -4x Wild Draw Four
# Return values: deck (list)

def buildDeck():
    deck = []
    #example card: Red 7, Yellow 8, Blue Skip
    colours = ['Red','Yellow','Blue','Green']
    values = [0,1,2,3,4,5,6,7,8,9,'Draw Two','Skip','Reverse']
    wilds = ['Wild','Wild Draw Four']
    #for loop
    print(deck)
    return deck
buildDeck()
