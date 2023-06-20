import wikipediaapi


def read_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def get_article(title):
    w_api = wikipediaapi.Wikipedia('en')

    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""


def generate_articles(filename):
    titles_generator = read_titles(filename)
    for title in titles_generator:
        article = get_article(title)
        yield article
        

def average_letter_count(filename):
    total_letters = 0
    article_count = 0

    articles_generator = generate_articles(filename)
    for article in articles_generator:
        total_letters += len(set(article.lower()))
        article_count += 1

    if article_count > 0:
        average_count = total_letters / article_count
        return average_count
    else:
        return 0


average_count = average_letter_count('small.txt')
print("Średnia liczba liter na artykuł:", average_count)
