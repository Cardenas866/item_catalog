from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, BookDB, User

engine = create_engine('sqlite:///BookCatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="cardenas866@gmail.com")
session.add(User1)
session.commit()

# Dummy books data
book1 = BookDB(bookName="Pride and Prejudice",
               authorName="Jane Austen",
               coverUrl="""https://books.google.com.mx/books/content
               ?id=aQM50Iu3CZcC&printsec=frontcover&img=1&zoom=1
               &edge=curl&imgtk=AFLRE73uPSn3jF37T-j9jz6cqJagVhciXypttUK9nss-
               Fd151EmJvB37jy9LoPsAna5VA8cicQqHaZkpBQqSWhd8j5s08CXfOuX0F7
               vqQ0TvLeU4mjezDWPPzzNcB2i8NGrzeGsZDCWC""",
               description="""This sparkling tale of one of literature's
               most famous courtships focuses on a spirited family of sisters
               and their marriage-minded mother's attempts to see
               them well settled.""", category="Romance", user_id=1)

session.add(book1)
session.commit()

book2 = BookDB(bookName="Harry Potter and the Prisoner of Azkaban",
               authorName="JK Rowling",
               coverUrl="""https://books.google.com.mx/books/content
               ?id=BPtbPgAACAAJ&printsec=frontcover&img=1&zoom=1
               &imgtk=AFLRE71BymKe_TBHEjbg5wv7_lipWLKv-YiRLTDnVTNHU79BZdGQ
               l4nT0HHcJxdJeKVlImKFw2-ryO7tjdU3HbHemm2CL_1hxBLoOWqZZgDPnr
               chuQrpklefsS5btdJiOQnhL4l34OlV""",
               description="""Harry Potter, along with his friends, Ron and
               Hermione, are about to start their third year at Hogwarts School
               of Witchcraft and Wizardry.""", category="Fantasy", user_id=1)

session.add(book2)
session.commit()

book3 = BookDB(bookName="1984",
               authorName="George Orwell",
               coverUrl="""https://books.google.com.mx/books/content
               ?id=uyr8BAAAQBAJ&printsec=frontcover&img=1&zoom=1
               &edge=curl&imgtk=AFLRE72kgVlmW0us7R1OTBX43hsBWLiTSfkSUD7A2At2
               INNRTrKeZIrVZvSqcw1s2BBJ38sVJUGjNH6DTW71MOKkBdrbrSwPw8B-uUS
               Qgndu3ZwIVcyUCMJXoTnq4zD_1qOj21XSh0oF""",
               description="""Who controls the past controls the future:
               who controls the present controls the past""",
               category="Fiction", user_id=1)

session.add(book3)
session.commit()

book4 = BookDB(bookName="The Outsider",
               authorName="Stephen King",
               coverUrl="""https://books.google.com.mx/books/content
               ?id=2MhaDwAAQBAJ&printsec=frontcover&img=1&zoom=1
               &edge=curl&imgtk=AFLRE72NaZ50HNUd98RaXC3zyQEC0OgQmYfc-XYpU5
               pHRshuGXFp03pQKzlIFlKMky2FXj6n_zLQ1ugphaeWyjDzZILE6GMKJ5lm-k5
               gDG5_lP5RMXf4VKDgMvc6n5aI11Dot4rBBIRC""",
               description="""The Outsider is a horror novel by American
               author Stephen King, published on May 22, 2018, by Scribner.""",
               category="Mystery", user_id=1)

session.add(book4)
session.commit()

book5 = BookDB(bookName="Redshirts",
               authorName="John Scalzi",
               coverUrl="""https://books.google.com.mx/books/content
               ?id=2myG-uWq5zQC&printsec=frontcover&img=1&zoom=1
               &edge=curl&imgtk=AFLRE73W_onYbLuTNuInCg6IlgqBU6x-le-tGiCoZY6Br
               Fy9YPzxclOMwC3FO_UjI2NlGs99mnJHr9cc0HtYjM7KgvB15Ei_cpqIFF49
               YX5GKpuM2Wcqvg-UX1EGZw0MK086AqMeBUIG""",
               description="""Ensign Andrew Dahl has just been assigned to the
                Universal Union Capital Ship Intrepid, flagship of the
                Universal Union since the year 2456.""",
                category="Fiction", user_id=1)

session.add(book5)
session.commit()


print "Success"
