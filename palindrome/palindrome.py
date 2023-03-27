def word_checker(word):
    return word == word[::-1]

if __name__ == '__main__':
    print(word_checker(input('Enter word: ')))