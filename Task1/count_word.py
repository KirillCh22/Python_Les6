

def count_word_dict(words: str):

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1          # ищем похожие слова в списке, если находим прибляем 1, если нет, то ставим 0

    return word_count

