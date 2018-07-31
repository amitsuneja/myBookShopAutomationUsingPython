import csv

shelf = {}

class Book:

    def __init__(self, isbn, name, language, origin, authors, price, version):
        self.isbn = isbn
        self.name = name
        self.language = language
        self.origin = origin
        self.authors = authors
        self.price = price
        self.version = version
        self.counter = 1


class Shelf:

    def __init__(self, mycsvfilepath):
        self.mycsvfilepath = mycsvfilepath

    def _add_books_(self):
        with open(self.mycsvfilepath, "rt") as my_csv_file:
            my_csv_reader = csv.reader(my_csv_file)
            for line in my_csv_reader:
                mykeyforshelf = line[2][0:2].upper()
                print("ShelfName ={}".format(mykeyforshelf))
                print("SubShelfName={}".format(line[1]))
                if mykeyforshelf not in shelf.keys():
                    shelf[mykeyforshelf] = {}
                    shelf[mykeyforshelf][line[1]] = Book(line[1], line[2], line[3], line[4], line[5], line[6], line[7])
                    print("Added New Book to new shelf ={} , subshelf= {}, BookName= {}".format(mykeyforshelf,line[1],shelf[mykeyforshelf][line[1]].name))
                    print(shelf)
                    print("\n")
                elif line[1] in shelf[mykeyforshelf].keys():
                    print("this is existing shelf = {} and subshelf={}".format(mykeyforshelf, line[1]))
                    print("existing counter for this book = {}".format(shelf[mykeyforshelf][line[1]].counter))
                    shelf[mykeyforshelf][line[1]].counter = shelf[mykeyforshelf][line[1]].counter + 1
                    print("New counter for this book = {}".format(shelf[mykeyforshelf][line[1]].counter))
                    print(shelf)
                    print("\n")
                else:
                    print("I am existing shelf = {} , But new Sub Shelf ={}".format(mykeyforshelf, line[1]))
                    shelf[mykeyforshelf][line[1]] = Book(line[1], line[2], line[3], line[4], line[5], line[6], line[7])
                    print(shelf)
                    print("\n")

    def _list_all_books(self):
        for key in shelf.keys():
            for subshelfkey in shelf[key].keys():
                self._print_book_details(key,subshelfkey)


    def _search_by_isbn(self, constant_var_for_isbn_search, isbntosearch):
        self.isbntosearch = isbntosearch
        self.constant_var_for_isbn_search = constant_var_for_isbn_search
        self.myshelfnumber = self._find_shelfname_of_isbn(self.isbntosearch, self.constant_var_for_isbn_search)
        print("\n")
        print("Please wait .......")
        print("Your isbn number = {}".format(self.isbntosearch))
        print("Your Shelf number = {}".format(self.myshelfnumber))
        if self.myshelfnumber == "dummykey":
            print("Sorry we are unable to locate the isbn number you have given")
        else:
            self._print_book_details(self.myshelfnumber,self.isbntosearch)


    def _find_shelfname_of_isbn(self, isbn_number_to_find_shelf_name,constant_var):
        self.isbn_number_to_find_shelf_name = isbn_number_to_find_shelf_name
        self.constant_var = constant_var
        myshelfkey = "dummykey"
        for key in shelf.keys():
            for subshelfkey in shelf[key].keys():
                if shelf[key][subshelfkey].isbn == self.isbn_number_to_find_shelf_name:
                    myshelfkey = key.upper()
        if myshelfkey == "dummykey":
            return("KeyNotFound")
        else:
            return(myshelfkey)


    def _print_book_details(self, majorshelfname, minorshelfname):
        self.majorshelfname = majorshelfname
        self.minorshelfname = minorshelfname
        print("Name of Book = {}".format(shelf[self.majorshelfname][self.minorshelfname].name))
        print("ShelfName = {}".format(self.majorshelfname))
        print("ISBN/Subshelf = {}".format(self.minorshelfname))
        print("Language Book = {}".format(shelf[self.majorshelfname][self.minorshelfname].language))
        print("Country of Origin = {}".format(shelf[self.majorshelfname][self.minorshelfname].origin))
        print("Authors of Book = {}".format(shelf[self.majorshelfname][self.minorshelfname].authors))
        print("price of Book = {}".format(shelf[self.majorshelfname][self.minorshelfname].price))
        print("Number of Copies in stock = {}".format(shelf[self.majorshelfname][self.minorshelfname].counter))
        print()

    def _search_substring(self, substringtosearch):
        self.substringtosearch = substringtosearch
        self.substring_check = 0
        for key in shelf.keys():
            for subkey in shelf[key].keys():
                if self.substringtosearch.upper() in shelf[key][subkey].name.upper():
                    self._print_book_details(key.upper(),shelf[key][subkey].isbn)
                elif self.substringtosearch.upper() in shelf[key][subkey].authors.upper():
                    self._print_book_details(key.upper(),shelf[key][subkey].isbn)
                else:
                    pass

 









































myShelfObj = Shelf("E:\\Ashish\MyCsvFiles\\myCurrentInventory.csv")
myShelfObj._add_books_()
myShelfObj._list_all_books()
myShelfObj._search_by_isbn(0, "A11B12C13D17")
print("\n")
print("\n")
print("\n")
print("\n")
print("I am searching a sub string now..............")
myShelfObj._search_substring("Sumit")
