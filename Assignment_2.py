'''1.Unique Sort problem–Implement thisin 5 different ways.Take a string as input that accepts a comma separated
sequence of wordsas inputand prints the unique words in sorted form (alphanumerically).
*Input*: orange, white, red, cyan, green, magenta, cyan, pink, white
*Output*: cyan, green, magenta, orange, pink, red, white'''

def unique(input_str):
    word =input_str.split(",")
    unique_words=sorted(set(word), key=str.lower)
    return ",".join(unique_words)

input_str = input("enter the words : ")
output = unique(input_str)
print(output)

