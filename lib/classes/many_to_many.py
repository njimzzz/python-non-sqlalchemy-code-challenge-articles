class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title  # Use the private attribute to allow setting the title initially
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot set attribute 'title'")

    

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must have more than 0 characters")
        
        self._name = name
        self._articles = []
        self._magazines = []
        
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        raise ValueError("Cannot change authors name")


    def articles(self):
        return [article for article in Article.all if article.author == self]
        

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
       categories = {article.magazine.category for article in Article.all if article.author == self}
       return list(categories) if categories else None
    
from collections import defaultdict

class Magazine:
    def __init__(self, name: str, category: str):
        self._validate_name_and_category(name, category)
        self.name = name
        self.category = category

    def _validate_name_and_category(self, name: str, category: str):
        if not isinstance(name, str) or not isinstance(category, str):
            raise ValueError("Name and category must be strings")
        if not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters long")
        if not category:
            raise ValueError("Category cannot be empty")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in Article.all if article.magazine == self))

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else []

    def contributing_authors(self):
        author_article_count = defaultdict(int)
        for article in self.articles():
            author_article_count[article.author.name] += 1
        return [author for author in set(article.author for article in self.articles()) 
                if author_article_count[author.name] > 2]


author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")
Article(author_1, magazine_1, "How to wear a tutu with style")
Article(author_1, magazine_1, "How to be single and happy")
Article(author_1, magazine_1, "Dating life in NYC")
Article(author_1, magazine_2, "Carrara Marble is so 2020")
Article(author_2, magazine_2, "2023 Eccentric Design Trends")