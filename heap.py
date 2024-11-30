def comparator1(crewmate1, crewmate2):
    if (crewmate1._load - crewmate2._load)>0: 
        return False
    return True
    
def comparator2(treasure1, treasure2):
    if (treasure1.arrival_time + treasure1.remaining) == (treasure2.arrival_time + treasure2.remaining):
        if (treasure1.id - treasure2.id)>0:
            return False
        return True
    else:
        if ((treasure1.arrival_time + treasure1.remaining) -  (treasure2.arrival_time + treasure2.remaining))>0:
            return False
        return True
        

    

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        self._heap = init_array
        self.comparison_function = comparison_function
        if len(self._heap)>1:
            self.heapify()
        
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        
    def insert(self, value):
        self._heap.append(value)
        self.upheap(len(self._heap) - 1)
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
    
    def extract(self):
        if not self.is_empty():
            self.swap(0, (len(self._heap)-1))
            a=self._heap.pop()
            if len(self._heap) != 0:
                self.downheap(0)
            return a
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here

    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if not self.is_empty():
            a = self._heap[0]
            return a
        return None
    
    def parent(self, integ):
        return ((integ-1)//2)
    
    def left_child(self, integ):
        if self.has_left(integ):
            return (2*integ +1)
    
    def right_child(self, integ):
        if self.has_right(integ):
            return (2*integ + 2)
            
    def has_left(self, integ):
        if (2*integ + 1) < len(self._heap):
            return True
        else:
            return False
            
    def has_right(self, integ):
        if (2*integ +2) < len(self._heap):
            return True
        else:
            return False
    def swap (self, int1, int2):
        self._heap[int1], self._heap[int2] = self._heap[int2], self._heap[int1]
        
    def downheap (self, integ):
        if self.has_left(integ):
            left_child = self.left_child(integ)
            small_child = left_child
            if self.has_right(integ):
                right_child = self.right_child(integ)
                if self.comparison_function(self._heap[right_child],self._heap[left_child]) is True:
                    small_child = right_child
            if self.comparison_function(self._heap[small_child],self._heap[integ]) is True:
                self.swap(small_child, integ)
                self.downheap(small_child)
                
    def upheap (self, integ):
        parent = self.parent(integ)
        if parent >=0 :
            if self.comparison_function(self._heap[parent],self._heap[integ]) is False:
                self.swap(parent, integ)
                self.upheap(parent)
                
    def heapify(self):
        last = len(self._heap) -1
        for i in range(last, -1, -1):
            self.downheap(i)
            
    def __len__(self):
        return len(self._heap)
        
    def is_empty (self):
        return (len(self._heap)==0)
                
    
    # You can add more functions if you want to