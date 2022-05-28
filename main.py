# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

y=open("story.txt")
file=y.read()
word_count=file.split(" ")

x={}
for word in word_count:
    x[word]=y.get(word, 0)+1

print(x)

