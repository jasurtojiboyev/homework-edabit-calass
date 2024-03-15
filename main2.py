class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return "Title: " + self.title

    def get_author(self):
        return "Author: " + self.author

# Yangi kitoblar yaratish
book1 = Book("Mag'rurlik va xurofot", "Jeyn Osten (PP)")
book2 = Book("Gamlet", "Uilyam Shekspir (H)")
book3 = Book("Urush va tinchlik", "Lev Tolstoy (WP)")

# Kitoblar haqida ma'lumot olish
print(book1.get_title())
print(book1.get_author())

print(book2.get_title())
print(book2.get_author())

print(book3.get_title())
print(book3.get_author())