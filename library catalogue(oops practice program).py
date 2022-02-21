import json
import csv
from catalog import Catalog
from book import Book
import warnings
warnings.filterwarnings("ignore")  # To ignore warnings


def csv_to_json(csv_file, json_file):
    jsonArray = []

    # read csv file
    with open(csv_file) as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


catalog = Catalog()
want_to_add_books = input("You need to add books to the table, Press Y to add, press N to exit. Y/N \n")


# This function will add any number of books in the catalog table that user wants and convert it to csv format.
def addbooks():
    if want_to_add_books == 'N' or want_to_add_books == 'n':
        print('No books will be added.')
        exit(None)
    if want_to_add_books == 'Y' or want_to_add_books == 'y':
        print('how many more books to add?')
        book_count = 1
        number_of_books = int(input())
        for _ in range(number_of_books):
            print("Enter details of book number", book_count)
            print('author name:')
            name = input()
            print('ISBN number:')
            isbn = int(input())
            print('Book Title')
            title = input()
            print('Book Subject:')
            subject = input()
            print("DDS number:")
            dds = int(input())
            book_count += 1
            book = Book(name, isbn, title, subject, dds)
            catalog.add_book(book)


addbooks()
# Converting the csv file that got converted in addbooks() function to json format
csvFilePath = r'Catalog.csv'
jsonFilePath = r'Catalog.json'
csv_to_json(csvFilePath, jsonFilePath)

# Script to display the catalog table
want_to_display_table = input("Want to display table? Y/N \n")
if want_to_display_table == 'N' or want_to_display_table == 'n':
    print('Table will not be displayed')
    exit(None)
if want_to_display_table == 'Y' or want_to_display_table == 'y':
    catalog.display_catalog()
    # Asking user whether new record needs to be added or not.
    want_to_add_more_books = input("To add books to the table, Press Y to add, press N to exit. Y/N \n")
    if want_to_add_more_books == 'Y' or want_to_add_more_books == 'y':
        addbooks()
        print('Final Table :')
        catalog.display_catalog()
        # If new record is added than the csv and json files gets updated automatically.
        csvFilePath = r'Catalog.csv'
        jsonFilePath = r'Catalog.json'
        csv_to_json(csvFilePath, jsonFilePath)
    elif want_to_add_more_books == 'N' or want_to_add_more_books == 'n':
        print('No more book is added')

# Script to delete record from catalog table as well as from csv file and json file
want_to_delete_record = input("Want to delete any record? Y/N \n")
if want_to_delete_record == 'Y' or want_to_delete_record == 'y':
    catalog.remove_book()
    csvFilePath = r'Catalog.csv'
    jsonFilePath = r'Catalog.json'
    csv_to_json(csvFilePath, jsonFilePath)
    catalog.display_catalog()
if want_to_delete_record == 'N' or want_to_delete_record == 'n':
    print('No record deleted. Your final catalog:')

# Script to search book from table either via Book Title or via Book Subject.
want_to_search_book = input("Want to search book? Y/N \n")
if want_to_search_book == 'Y' or want_to_search_book == 'y':
    search_book_using_title_sub = input("Want to search book using book title or subject? title/subject \n")
    if search_book_using_title_sub == 'title':
        print('Enter title of the book to be searched :')
        catalog.search_book_title()
    elif search_book_using_title_sub == 'subject':
        print('Enter subject of the book to be searched :')
        catalog.search_book_subject()
    else:
        pass
if want_to_search_book == 'N' or want_to_search_book == 'n':
    print('No Book was searched.')
    exit(None)
