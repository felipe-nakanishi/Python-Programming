
#getting the user imput:
text = input("Text:");

#counting how many letters, words and sentences there are in the text:
def counter(text):
    letters = 0
    words = 0
    sentences = 0
    for i in range(len(text)):
        if ((text[i] >= 'a') and (text[i] <= 'z')) or ((text[i] >= 'A') and (text[i] <= 'Z')):
            letters += 1
        if (text[i] == ' '):
                words += 1
        if (text [i] == '.' or text [i] == '!' or text [i] == '?'):
                sentences = sentences + 1
    return [letters, words, sentences]

letters = counter(text)[0]
words = counter(text)[1]
sentences = counter(text)[2]

def coleman_liau_index(letters, words, sentences):
    #Calculating 'L' variable: average n of letters per 100 words:
    L = (letters * 100) / words
    #Calculating 's' variable: average n of sentences per 100 words:
    S = (sentences * 100) / words
    #Calculating the Coleman-Liau index
    index = (0.0588 * L) - (0.296 * S) - 15.8;
    return int(index)

index = coleman_liau_index(letters, words, sentences)

#using the index to mark a grade to the text:
def mark(index):
    if index >= 16:
        print("Grade 16+") 
    elif index < 1:
        print("Grade 1")
    else:
        print("Grade", index)

mark(index)