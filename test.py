import os
import random
import string

def generate_unique_words(count, length):
    words = set()
    alphabet = string.ascii_lowercase
    while len(words) < count:
        word = ''.join(random.choices(alphabet, k=length))
        words.add(word)
    return list(words)

# Ensure folder exists
os.makedirs("uke12", exist_ok=True)

with open("uke12/l3.txt", "w") as f:
    # First batch
    f.write("30000\n")
    words1 = generate_unique_words(30000, 30)
    for word in words1:
        f.write(word + "\n")

    # Second batch
    f.write("30000\n")
    words2 = generate_unique_words(30000, 30)
    for word in words2:
        f.write(word + "\n")

print("File 'uke12/l3.txt' generated successfully.")
