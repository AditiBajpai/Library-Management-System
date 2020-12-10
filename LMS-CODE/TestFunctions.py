# -*- coding: utf-8 -*-

from Catalog import Catalog
catalog = Catalog()
from User import Member, Librarian
from Book import Book

#print("########################## Creating Librarian Object ####################### \n")
librarian = Librarian("Raman","Delhi",35,'ASDF35','PYTHLIB101')
print(librarian)
#print("####################Librarian Object Created Successfully! ################ \n")

l1 = librarian.addBook("The Kite Runner","Khaled Hosseini", "2003", 309,catalog)
librarian.addBookItem(l1,'01TKR','R1B2',catalog)
librarian.addBookItem(l1,'01TKR','R1B3',catalog)
librarian.addBookItem(l1,'01TKR','R2B2',catalog)


l2 = librarian.addBook("Shoe Dog","Phil Knight", "2015",312,catalog)
librarian.addBookItem(l2,'03ATSS','R1B2',catalog)
librarian.addBookItem(l2,'03ATSS','R3B3',catalog)
librarian.addBookItem(l2,'03ATSS','R1B2',catalog)


l3 = librarian.addBook("Ikigai", "Hector Gracia", "2016", 195,catalog)
librarian.addBookItem(l3,'07IKIG','R1B1',catalog)
librarian.addBookItem(l3,'07IKIG','R3B2',catalog)
librarian.addBookItem(l3,'07IKIG','R3B2',catalog)

l4 = librarian.addBook("Inferno", "Dan Brown", "2010", 234,catalog)
librarian.addBookItem(l4,'02INF','R1B2',catalog)
librarian.addBookItem(l4,'02INF','R3B3',catalog)
librarian.addBookItem(l4,'02INF','R1B2',catalog)

librarian.viewBooks(catalog)

librarian.removeBookItemFromCatalog("Inferno","02INF", catalog)

librarian.removeBook("Inferno", catalog)

librarian.viewBooks(catalog) #check if catalog updated after removing book


# Librarian will add members##
m1 = librarian.addMember("Vishwas","Bangalore",23,'asljlkj22','std1233')
m2 = librarian.addMember("Prabhat","Delhi",32,'pbht1234','std1234')
m3 = librarian.addMember("Ishita","Kolkata",29,'ishi3456','std1235')
m4 = librarian.addMember("Ruby","Delhi",41,'rub45','std1236')

# Librarian will view all members##
librarian.viewMember()

#Librarian will remove members##
librarian.removeMember("Prabhat")

#Librarian will check updated members list
librarian.viewMember()

#librarian will search the book by name
librarian.searchByName("The Kite Runner", catalog)

##librarian will search the book by name
librarian.searchByName("Inferno", catalog)

##librarian will search the book by name of the author of the book
librarian.searchByAuthor("Khaled Hosseini", catalog)



################ member  ####################

#issuebook
m1.issueBook("The Kite Runner", catalog)
#issue_same_book
m1.issueBook("The Kite Runner", catalog)
#issue_another_book_check_total_updated_issued_books
m1.issueBook("Ikigai", catalog)
#check_for_other_members_of_the_library
m3.issueBook("Ikigai", catalog)
#check_for_unavailable_books
m3.issueBook("The Kite ", catalog)

#returnbook#
m1.returnBook("The Kite Runner", librarian, catalog)

#member can view books
m1.viewBooks(catalog)

#member can search by name of the book
m1.searchByName("Ikigai", catalog)

#member can search by author name
m4.searchByAuthor("Phil Knight", catalog)

######Book#######

#checking printBook function
b1 = Book('Harry Potter ','J.K. Rowling ', '2000',300)
b1.addBookItem('123hp','H1B1')
b1.addBookItem('124hp','H1B3')

b1.printBook()
