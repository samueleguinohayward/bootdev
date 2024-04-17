def appearance_count(text):
    count_per_word = {}
    for word in list(text):
        
        lowerWord = word.lower()
        if not lowerWord.isalpha():
            continue
        if lowerWord in count_per_word: 
            count_per_word[lowerWord] = count_per_word[lowerWord] + 1
        else:
            count_per_word[lowerWord] = 1
    for (char,count) in sorted(count_per_word.items(), key=lambda item: item[1] ,reverse = True):
        print("The \""+ char+"\" char appears: "+ str(count_per_word[char])+" times")

print("Report of frankenstein.txt")
print("--------------------------")
with open("./text.txt") as book:
    text= book.read()
    words= text.split()
    print("The text contains: "+str(len(words))+" words")
    print("----------------------------------------------")
    appearance_count(text)


