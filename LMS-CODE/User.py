# -*- coding: utf-8 -*-
from Catalog import Catalog
from Billing import Billing

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id

    def viewBooks(self,catalog):
        catalog.displayAllBooks()

    def searchByName(self,name,catalog):
        book_search = catalog.searchByName(name)
        if book_search:
            print("Book Found")
            print(book_search)
        else:
            print("Book Not Found")

    def searchByAuthor(self,author_name,catalog):
        book_search = catalog.searchByAuthor(author_name)
        if book_search:
            print("Book by author",author_name,"is present")
            #print(book_search)
        else:
            print("Book by author", author_name,"not found")



class Member(User):
    members_list = []

    @classmethod
    def addMemberList(cls, member):
        cls.members_list.append(member)

    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issued_books = [ ]
        Member.addMemberList(self)

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    #assume name is unique
    def issueBook(self,name,catalog,days=10):
        book_to_issue = catalog.searchByName(name)
        if book_to_issue in self.issued_books:
            print("This book has already been issued to you")

        elif book_to_issue is not None and len(book_to_issue.book_item) > 0:
            isbn = book_to_issue.book_item[0].isbn
            catalog.removeBookItem(name,isbn)
            print("Book Issued Successfully!")
            print("Inventory Updated!")

            self.issued_books.append(book_to_issue)
            self.issuedBookRecords()
        else:
            print("This book does not exist")



    def issuedBookRecords(self):
        total_issued_books = len(self.issued_books)
        if total_issued_books>0:
            print("The total number of books issued by the member {} are:".format(self.name), total_issued_books)
            print("The details of the books are:")
            for book in self.issued_books:
                print(book)



    #assume name is unique
    def returnBook(self,name,lib,catalog):
        result = self.check_book_in_issued_list(name)
        if result is not None:

            lib.returnIssuedBook(name,catalog,result)
            self.updatedBookRecords(name)
        else:
            print("This book has not been issued to you")



    def check_book_in_issued_list(self,name):
        for book in self.issued_books:
            if name==book.name:
                for i in book.book_item:
                    isbn = i.isbn
                    rack = i.rack
                    return [book,isbn,rack]
        return None

    def updatedBookRecords(self,name):
        for book in self.issued_books:
            if name in book.name:
                self.issued_books.remove(book)
                total_issued_books = len(self.issued_books)
                print("The list has been updated")
                print("The total number of books issued by the member {} are:".format(self.name), total_issued_books)
                break




class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id

    def __repr__(self):
        return (self.name +" " + self.location  + " "+  self.emp_id)

    def addBook(self,name,author,publish_date,pages,catalog):
        new_book = catalog.addBook(name,author,publish_date,pages)
        print("Book Added Successfully!")
        return new_book

    def addBookItem(self,name,isbn,rack,catalog):
        catalog.addBookItem(name,isbn,rack)

    def removeBook(self,name,catalog):
        catalog.removeBook(name)

    def removeBookItemFromCatalog(self,name,isbn,catalog):
        catalog.removeBookItem(name,isbn)


    def returnIssuedBook(self,name,catalog,result_list):
        book_to_return = result_list[0]
        isbn = result_list[1]
        rack = result_list[2]
        days = int(input("Enter the number of days you had the book:"))
        Billing.calculateBill(days)
        catalog.addBookItem(book_to_return,isbn,rack)
        print("Book returned Successfully!")
        print("Inventory Updated")



    def addMember(self,name, location, age, aadhar_id,student_id):
        m = Member(name, location, age, aadhar_id, student_id)
        print("New Member has been added Successfully")
        return m

    def removeMember(self,name):
        flag = 0
        for member in Member.members_list:
            if member.name == name:
                Member.members_list.remove(member)
                print("The member of {} name has been removed".format(name))
                flag = 1
                break
        if flag==0:
            print("No member exists by this name")

    def viewMember(self):
        for member in Member.members_list:
            print(member)
