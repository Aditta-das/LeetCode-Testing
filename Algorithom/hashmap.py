class MyHashMap(object):

    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    def put(self, key, value):
        self.arr[key] = value
    
    def get(self, key):
        return self.arr[key]
    
    def remove(self, key):
        self.arr[key] = None
