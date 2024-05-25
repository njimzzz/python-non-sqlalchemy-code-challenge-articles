class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        author.add_article(self)
        self.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        raise AttributeError("Cannot set attribute 'title'")

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must have more than 0 characters")
        self._name = name
        self._articles = []
        
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        raise ValueError("Cannot change authors name")

    def articles(self):
        return self._articles
 

    def magazines(self):
        return self._magazines

    
    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("Article must be an instance of Article")
        self._articles.append(article) 
        return article


    def topic_areas(self):
        return {magazine.category for magazine in self._magazines}

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass


author = Author("Carry Bradshaw")
magazine = Magazine("Vogue", "Fashion")
article_1 = Article(author, magazine, "How to wear a tutu with style")