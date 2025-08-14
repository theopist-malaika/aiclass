class Library:
    def __init__(self,books):
        self.books=books
    def borrowbook(self,title):
        for i in self.books:
            if title.lower() == i.lower():
                return"available"
books=["biology","english","chichewa"]
documents=Library(books)
print(documents.borrowbook("maths"))

