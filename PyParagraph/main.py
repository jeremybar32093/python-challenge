import os
import re

# Define path for output analysis file
outputpath = os.path.join('analysis','paragraph_analysis.txt')

# Paragraph pulled from https://www.penguinrandomhouse.ca/books/108336/a-game-of-thrones-hbo-tie-in-edition-by-george-r-r-martin/9780553386790/excerpt
paragraph = "The morning had dawned clear and cold, with a crispness that hinted at the end of summer. They set forth at daybreak to see a man beheaded, twenty in all, and Bran rode among them, nervous with excitement. This was the first time he had been deemed old enough to go with his lord father and his brothers to see the king's justice done. It was the ninth year of summer, and the seventh of Bran's life."

# Split using space to get approximate number of words
words = paragraph.split()
number_words = len(words)

# Split using regex to determine end of sentence
sentences = re.split("(?<=[.!?]) +", paragraph)
number_sentences = len(sentences)

# Print outputs of analysis
print("Paragraph Analysis\n-------------------------")
print(f"Approximate Word Count: {number_words}")
print(f"Approximate Sentence Count: {number_sentences}")


# Write outputs of analysis to text file