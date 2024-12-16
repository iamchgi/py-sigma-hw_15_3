"""
Модель структури даних "книга" - для представлення:
DTO: Data Transfer Object — один із шаблонів проєктування, який використовують для передачі даних між підсистемами програми.
"""

from dataclasses import dataclass


@dataclass                      # декоратор для додавання даних
class BookDTO:
    """
    Book information
    """
    title: str
    author: str
    publisher: str
    genre: str
    published: int
    id: int = -1
    famous: bool = False
    full_info = ""
    
    def __post_init__(self):   # дандер метод __post_init__ заповнює поля після створення екземпляру класа
        self.famous = self.author != "no name"
        self.full_info = f"{self.title} {self.author} {self.genre}"
