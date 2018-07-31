# myBookShopAutomationUsingPython
This is OOPS driven project where we planned to automate the bookshop

Below is Data Structure we will be using in this project



myshelf = {}
myshelf["PY"] ={}
myshelf["PY"]["WWW"] = {"Name": "Book1", "Class": "5th"}
myshelf["PY"]["XXX"] = {"Name": "Book2", "Class": "6th"}

myshelf["EE"] ={}
myshelf["EE"]["YYY"] = {"Name": "Book3", "Class": "7th"}
myshelf["EE"]["ZZZ"] = {"Name": "Book4", "Class": "8th"}

print(myshelf)
for shelfkey in myshelf.keys():
    for subshelf in myshelf[shelfkey].keys():
        print(myshelf[shelfkey][subshelf])
