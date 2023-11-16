#2.2 - print each word on seperate line uppercased

def print_upper_words(words):
    for word in words:
        print(word.upper())


#2.3 - print only words that start with letter 'e'

def print_upper_words_e(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

#2.4 - print only words that start with letters defined in must_start_with

def print_upper_words_3(words, must_start_with):
    
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())