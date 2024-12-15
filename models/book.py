from dao.database import ORM_DATABASE as db

# опис бази даних ""
class BookDBModel(db.Model):
    __tablename__ = "Books"

    # опис полів бази даних "книга"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author: str = db.Column(db.String(200))
    title: str = db.Column(db.String(200))
    publisher: str = db.Column(db.String(200))
    genre: str = db.Column(db.String(200))
    published: int = db.Column(db.Integer)

    def __init__(
        self,

        title: str,
        author: str,
        publisher: str,
        genre: str,
        published: int
    ) -> None:
        self.author = str(author)
        self.title = str(title)
        self.publisher = str(publisher)
        self.genre = str(genre)
        self.published = int(published)