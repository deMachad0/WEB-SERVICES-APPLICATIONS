# book dao skeleton

class BookDAO:
    #get all
    def getAll(self):
        return [{"id":1,"Title":"Blah","author":"someone","price":999}]
    #find by id
    def findById(self, id):
        return [{"id":1,"Title":"Blah","author":"someone","price":999}]
    #create a book
    def create(self, book):
        return [{"id":1,"Title":"Blah","author":"someone","price":999}]
    #update a book
    def update(self, id, book):
        return [{"id":1,"Title":"Blah","author":"someone","price":999}]
    def delete(self, id):
        return True
    
    bookDAO = BookDAO()

    if __name__ == "__main__":
        book = {"id":1,"Title":"Blah","author":"someone","price":999}
        print("test getall")
        print(f"\t{bookDAO.getAll()}")
        print("test find by id(1)")
        print(f"\t{bookDAO.findById(1)}")
        print("test create a book")
        print(f"\t{bookDAO.create(book)}")
        print("test update a book")
        print(f"\t{bookDAO.update(1, book)}")
        print("delete a book")
        print(f"\t{bookDAO.delete(1)}")

    