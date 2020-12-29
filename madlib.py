from random-word import RandomWords
import random

def loveLetterML(inputFile, outputFile):
    """
    This function either fills an empty MadLib text file with words a user inputs, and writes the completed MadLib to a new
    text file, or generates a completely random madlib.
    """
    yes = 'yes'
    no = 'no'
    question = input('Do you want to make your own MadLib, or do you want to generate a random one? Type "yes" to make your own, or type "no" to generate a random one.').low
    elif question != no and != yes:
        while question != and != yes:
            question = input('Please type either "yes" or "no" to continue')
    if question == 'yes':
        inF = open(inputFile)
        outF = open(outputFile, 'w')
        content = inF.read()
        replaced = "~"
        words = []
        word1 = str(input("Who are you writing this to? ")).capitalize()
        words.append(word1)
        word2 = str(input("Enter an adjective. ")).lower()
        words.append(word2)
        word3 = str(input("Enter a verb. ")).lower()
        words.append(word3)
        word4 = str(input("Enter a body part. ")).lower()
        words.append(word4)
        word5 = input("Enter a number. ").lower()
        if word5.islower():
            while word5.islower():
                word5 = str(input("Try entering a number in numerical form. "))
                words.append(word5)
        else:
            words.append(word5)
        word6 = str(input("Enter a noun. ")).lower()
        words.append(word6)
        word7 = str(input("Enter an adverb. ")).lower()
        words.append(word7)
        word8 = str(input("Enter a verb. ")).lower()
        words.append(word8)
        word9 = str(input("Enter a plural noun. ")).lower()
        words.append(word9)
        word10 = str(input("What is your name? ")).capitalize()
        words.append(word10)
        count = 0
        for word in content:
            if replaced not in word:
                outF.write(word)
            elif replaced in word:
                word = word.replace(replaced, words[count], 1)
                outF.write(word)
                count += 1
        outF.close()
    elif question == 'no':
        r = RandomWords
        inF = open(inputFile)
        outF = open(outputFile, 'w')
        content = inF.read()
        replaced = "~"
        words = []
        count = 0
        word1 = str(input("Who are you writing this to? ")).capitalize()
        words.append(word1)
        word2 = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="adjective").lower()
        words.append(word2)
        word3 = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="verb").lower()
        words.append(word3)
        #word4 needs to be a body part
        word5 = str(random.randint(0, 1000))
        words.append(word5)
        word6 = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun").lower()
        words.append(word6)
        word7 = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="adverb").lower()
        words.append(word7)
        word8 = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="verb").lower()
        words.append(word8)
        word9 = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun").lower()
        word10 = str(input("What is your name? ")).capitalize()
        words.append(word10)
        for word in content:
            if replaced not in word:
                outF.write(word)
            elif replaced in word:
                word = word.replace(replaced, words[count] 1)
                count += 1
                outF.write(word)
        outF.close()

loveLetterML("madlib.txt", "newmadlib.txt")
