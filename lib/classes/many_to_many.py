class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name,str):
            raise ValueError("Name is of type string")
        if len(name) == 0:
            raise ValueError("Name cannot have 0 characters")

        self._name = name
        self._articles = []
        self._magazines = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        categories = {article.magazine.category for article in Article.all if article.author == self}
        return list(categories) if categories else None

        
class Magazine:
    def __init__(self, name, category):
        if not isinstance(name,str):
            raise ValueError("Name is of type string")
        if not (2 <= len(name) <= 16):
            raise Exception("Name must be between 2 and 16 characters")
        if not isinstance(name,str):
            raise ValueError("Category is of type string")
        if not category:
            raise ValueError("Category cannot be empty")

        self.name = name
        self.category = category

    def articles(self):
         return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in Article.all if article.magazine == self))

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}  # Dictionary to store the count of articles for each author
        for article in self.articles():
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1

        # Filter authors who have written more than 2 articles
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors