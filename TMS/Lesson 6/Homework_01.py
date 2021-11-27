import collections

"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
"""


def main(t):
    text_on_words = text.split()  # разбивает текст на каждое слово(объект) по отдельности
    counter_text = collections.Counter(
        text_on_words)  # вид словаря,позволяет нам считать количество неизменяемых объектов
    most_common, how_many = counter_text.most_common()[
        0]  # возвращает наиболее часто встречающиеся элемент и как часто

    longest_word = max(text_on_words,
                       key=len)  # key подразумевает первоначальную задачу для выполнения max,то есть найти
    # максимум по длине и потом только в объекте text_on_words
    d = f"наиболее часто встречающееся слово:{most_common}" \
        f"самое длинное слово:{longest_word}"
    return d


if __name__ == "__main__":
    text = 'why this text is so hard u know or not know but u know wow knowledge'
    print(main(text))

# если не через функцию,то


text = 'why this text is so hard u know or not know but u know wow knowledge'
text_on_words = text.split()  # разбивает текст на каждое слово(объект) по отдельности
counter_text = collections.Counter(text_on_words)  # вид словаря,позволяет нам считать количество неизменяемых объектов
most_common, how_many = counter_text.most_common()[0]  # возвращает наиболее часто встречающиеся элемент и как часто

longest = max(text_on_words, key=len)  # key подразумевает первоначальную задачу для выполнения max,то есть найти
# максимум по длине и потом только в объекте text_on_words

print(f"наиболее часто встречающееся слово:{most_common}"
      f"самое длинное слово: {longest}")
