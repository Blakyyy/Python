# Напишите программу, удаляющую из текста все слова содержащие "абв".
text = 'абвезная крутая муть жила в абвешной абвешке и пила только абв'
words = text.split()
new_words = []
delete = 'абв'
for word in words:
    if delete not in word:
        new_words.append(word)
print(new_words)

