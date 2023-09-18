# Instructions :
# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: None): It will contain a list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.

class Pagination() :
    def __init__(self, contentlist, pageSize):
        self.pageSize = 10
        self.pageSize = int(pageSize)
        self.contentlist = contentlist
        self.end_list = list()
        self.list_dict = { }
        self.page_num_cur = 1
        
        
        self.num_of_pages = len(self.contentlist) / self.pageSize
        if float(self.num_of_pages % 1) > 0 :
            self.end_list = self.contentlist[int(self.num_of_pages)*self.pageSize :]
            self.total_pages = int(self.num_of_pages) + 1
            self.list_dict[self.total_pages] = self.end_list 
        else: 
            self.total_pages = self.num_of_pages
        
        
        
        for num in range(1, int(self.num_of_pages) + 1 ) :
            pagelist = list()
            for index in range(self.pageSize * (num - 1), self.pageSize * num) :
                pagelist.append(self.contentlist[index])
                
            self.list_dict[num] = pagelist
        print(self.list_dict)
    
    def getVisibleItems(self) :
        print(self.list_dict[self.page_num_cur])

    
    def nextPage(self) :
        if self.page_num_cur < self.total_pages :
            self.page_num_cur = self.page_num_cur + 1
        else :
            print("This is the last page. No more pages are available.")
    
    def prevPage(self) :
        if self.page_num_cur > 1 :
            self.page_num_cur = self.page_num_cur - 1
        else :
            print("This is the first page. No previous pages are available.")

    def firstPage(self) :
        print(self.list_dict[1])

    def lastPage(self) :
        print(self.list_dict[self.total_pages])

    def goToPage(self, pageNum) :
        self.pageNum = pageNum
        if self.pageNum < 1 :
            print(self.list_dict[1])
        elif self.pageNum > self.total_pages :
            print(self.list_dict[self.total_pages])
        else:
            print(self.list_dict[self.pageNum])

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
page = Pagination(alphabetList, 3)
page.getVisibleItems()  
page.nextPage()
page.firstPage()
page.lastPage()
page.goToPage(4)
page.goToPage(10)
