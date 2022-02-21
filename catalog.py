import pandas as pd
import warnings
warnings.filterwarnings("ignore")  # To ignore warnings


class Catalog:

    def __init__(self):
        self.df = pd.DataFrame(columns=['name', 'isbn', 'title', 'subject', 'dds'])
        self.data_to_append = None
        self.data = None

    def add_book(self, obj):
        self.data_to_append = {'name': obj.name, 'isbn': obj.isbn, 'title': obj.title, 'subject': obj.subject,
                               'dds': obj.dds}
        self.df = self.df.append(self.data_to_append, ignore_index=True)
        self.df.to_csv('Catalog.csv', index=False)

    def remove_book(self):
        print('Enter row number of the table to delete that author from the table :')
        print("Note : The table starts from row number 0 not 1.")
        row_input = int(input())
        if row_input >= 0:
            self.df.drop(row_input, 0, inplace=True)
            self.df.to_csv('Catalog.csv', index=False)

    def display_catalog(self):
        print(self.df)

    def search_book_title(self):
        data = self.df.copy()
        user = data['title'] == input()
        data.where(user, inplace=True)
        selected_rows = data[~data[['name', 'isbn', 'title', 'subject', 'dds']].isnull()]
        if len(selected_rows.dropna()) != 0:
            print(selected_rows.dropna())
        else:
            print('-1, The Book title you entered is not present in catalog.')

    def search_book_subject(self):
        data = self.df.copy()
        user = data['subject'] == input()
        data.where(user, inplace=True)
        selected_rows = data[~data[['name', 'isbn', 'title', 'subject', 'dds']].isnull()]
        if len(selected_rows.dropna()) != 0:
            print(selected_rows.dropna())
        else:
            print('-1, The Book title you entered is not present in catalog.')
