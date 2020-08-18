import random


quotes=['“The elevator to success is out of order. You’ll have to use the stairs, one step at a time.” Joe Girard',
'“I didn’t fail the test. I just found 100 ways to do it wrong.” Benjamin Franklin',
'“Always remember that you are unique – just like everybody else.” Unknown',
'Your limitation—it’s only your imagination.',
'Push yourself, because no one else is going to do it for you.',
'Success doesn’t just find you. You have to go out and get it.',
'The harder you work for something, the greater you’ll feel when you achieve it.',
'Don’t stop when you’re tired. Stop when you’re done.',
'It’s going to be hard, but hard does not mean impossible.',
'Sometimes we’re tested not to show our weaknesses, but to discover our strengths.',
'The key to success is to focus on goals, not obstacles.']

def get_random_quote():
	global quotes
	return random.choice(quotes)