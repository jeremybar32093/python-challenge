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

# Create loop to count how many letters are in the paragraph
# Then divide by number of words to get average letter count

# First, create list defining letters - will compare characters in paragraph string to see if they are in this list
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# counter variable to count number of letters in paragraph string
letter_count = 0
# iterate through each character in paragraph, count letter if it falls within above defined list
for letter in paragraph:
    if letter in letters:
        letter_count += 1

# calculate average letter count by doing letter count / number of words
average_letter_count = letter_count / number_words
average_letter_count_format = "{:.1f}".format(average_letter_count)

# Calculate average sentence length by doing number of words / number of sentences
average_sentence_length = number_words / number_sentences
average_sentence_length_format = "{:.1f}".format(average_sentence_length)

# Print outputs of analysis
print("Paragraph Analysis\n-------------------------")
print(f"Approximate Word Count: {number_words}")
print(f"Approximate Sentence Count: {number_sentences}")
print(f"Average Letter Count: {average_letter_count_format}")
print(f"Average Sentence Length: {average_sentence_length_format}")

# Write outputs of analysis to text file
with open(outputpath, 'w', newline='') as text_file:
    text_file.write("Paragraph Analysis\n-------------------------\n")
    text_file.write(f"Approximate Word Count: {number_words}\n")
    text_file.write(f"Approximate Sentence Count: {number_sentences}\n")
    text_file.write(f"Average Letter Count: {average_letter_count_format}\n")
    text_file.write(f"Average Sentence Length: {average_sentence_length_format}")