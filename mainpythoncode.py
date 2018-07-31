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
        self.counter= 1



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
                    shelf[mykeyforshelf][line[1]] = Book(line[1],line[2],line[3],line[4],line[5],line[6],line[7])
                    print("Added New Book to new shelf ={} , subshelf= {}, BookName= {}".format(mykeyforshelf,line[1],shelf[mykeyforshelf][line[1]].name))
                    print(shelf)
                    print("\n")
                elif line[1] in shelf[mykeyforshelf].keys():
                    print("this is existing shelf = {} and subshelf={}".format(mykeyforshelf,line[1]))
                    print("existing counter for this book = {}".format(shelf[mykeyforshelf][line[1]].counter))
                    shelf[mykeyforshelf][line[1]].counter = shelf[mykeyforshelf][line[1]].counter + 1
                    print("New counter for this book = {}".format(shelf[mykeyforshelf][line[1]].counter))
                    print(shelf)
                    print("\n")
                else:
                    print("I am existing shelf = {} , But new Sub Shelf ={}".format(mykeyforshelf,line[1]))
                    shelf[mykeyforshelf][line[1]] = Book(line[1],line[2],line[3],line[4],line[5],line[6],line[7])
                    print(shelf)
                    print("\n")


myShelfObj = Shelf("E:\\Ashish\MyCsvFiles\\myCurrentInventory.csv")
myShelfObj._add_books_()
print("_____________________________________________________________________________")

for key in shelf.keys():
    for subshelfkey in shelf[key].keys():
        print("Name of Book = {}".format(shelf[key][subshelfkey].name))
        print("ShelfName = {}".format(key))
        print("ISBN/Subshelf = {}".format(subshelfkey))
        print("Language Book = {}".format(shelf[key][subshelfkey].language))
        print("Country of Origin = {}".format(shelf[key][subshelfkey].origin))
        print("Authors of Book = {}".format(shelf[key][subshelfkey].authors))
        print("price of Book = {}".format(shelf[key][subshelfkey].price))
        print("Number of Copies in stock = {}".format(shelf[key][subshelfkey].counter))
        print()

