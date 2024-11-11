sentence = str(input('Enter a sentence: ')).strip().capitalize()
print(f'There are {sentence.lower().count('a')} "a" in {sentence}')
print(f'The first letter "a" appear in the position {sentence.lower().find('a') + 1}')
print(f'The last "a" appear in the position {sentence.lower().rfind('a') + 1}')
