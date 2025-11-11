import random        # Imports the random module

# Generates a random integer between 1 and 10 (inclusive)
rand_int = random.randint(1, 10)

print("Random Integer:", rand_int)


#random float between 0 and 1
rand_float = random.random()
print("Random Float:", rand_float)

#random choice from a list
colors = ['red', 'blue', 'green', 'yellow']
rand_color = random.choice(colors)
print("Random Color:", rand_color)

#shuffle a list
random.shuffle(colors)
print("Shuffled Colors:", colors)

# random sample from a list
sample = random.sample(colors, 2)
print("Random Sample:", sample)