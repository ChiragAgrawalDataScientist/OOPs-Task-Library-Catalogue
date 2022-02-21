import warnings
warnings.filterwarnings("ignore")  # To ignore warnings


class Book:

    def __init__(self, name, isbn, title, subject, dds):
        self.name = name
        self.isbn = isbn
        self.title = title
        self.subject = subject
        self.dds = dds
        self.data_to_append = None
