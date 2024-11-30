'''
    Python file to implement the class CrewMate
'''
from treasure import Treasure
from heap import Heap
from heap import comparator2
class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self._load = 0
        self.init_array =[]
        
    
    # Add more methods if required
    def add_treasure (self, treasure):
        treasure.initiate()
        self.init_array.append(treasure)
        self._load =max(self._load, treasure.arrival_time) + treasure.size
        
    def process(self):
        treasures = Heap(comparator2, [])
        list = []
        m = len(self.init_array)
        for i in range(m):
            if treasures.is_empty():
                treasures.insert(self.init_array[i])
            else:
                if i==0:
                    t = self.init_array[i].arrival_time
                else:
                    t = self.init_array[i-1].arrival_time
                time = self.init_array[i].arrival_time - t
                while(time>0):
                    top = treasures.top()
                    if top is None:
                        break
                    if(time>=top.remaining):
                        t= t+ top.remaining
                        top.completion_time = t
                        time = time - top.remaining
                        list.append(treasures.extract())
                    else:
                        top.remaining = top.remaining - time
                        time = 0
                        t = self.init_array[i].arrival_time
                treasures.insert(self.init_array[i])
        if not treasures.is_empty():
            time = self.init_array[-1].arrival_time
            while not treasures.is_empty():
                top = treasures.top()
                time = time + top.remaining
                top.completion_time = time
                list.append(treasures.extract())
        return list
                        
        
        
        
        
        
        
        