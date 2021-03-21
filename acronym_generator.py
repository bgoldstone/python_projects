#Generates an acronym from a phrase
def main():
    phrase = input('Enter an input to convert to acronym ')
    phrase_list = phrase.split(' ')
    acronym = ''
    for word in phrase_list:
        acronym += word[0]
    print(f'the acronym is {acronym.upper()}')



if __name__ == '__main__':
    main()