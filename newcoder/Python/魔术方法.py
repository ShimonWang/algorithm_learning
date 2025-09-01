class List:
    def __init__(self):
        self.list = [1,2,3]
    def __len__(self):
        return len(self.list)
lis = List()

print(lis.__len__())
print(len(lis))