text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = text.split()
new_text = []

for word in words:
    if word.endswith(','):
        updated_word = word[:-1] + 'ing' + ','
        new_text.append(updated_word)
    elif word.endswith('.'):
        updated_word = word[:-1] + 'ing' + '.'
        new_text.append(updated_word)
    else:
        new_text.append(word + 'ing')

print(' '.join(new_text))
