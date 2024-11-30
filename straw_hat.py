'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
from treasure import Treasure
from heap import comparator1

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        self._crewmate_strength=m 
        crewmate = [CrewMate() for i in range(m)]
        self._crewmates = Heap(comparator1, crewmate)
        self._treasures = []

    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        a = self._crewmates.extract()
        a.add_treasure(treasure)
        self._crewmates.insert(a)
        self._treasures.append(treasure)
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        m = len(self._crewmates)
        # Write your code here
        list = []
        if m>=len(self._treasures):
            for i in range(len(self._treasures)):
                self._treasures[i].reinitiate()
                self._treasures[i].completion_time = self._treasures[i].size + self._treasures[i].arrival_time
                list = self._treasures
        if m<len(self._treasures):
            for i in range(len(self._treasures)):
                self._treasures[i].reinitiate()
            for i in self._crewmates._heap:
                a = i.process()
                list.extend(a)
        list.sort(key = lambda x: x.id )
        return list
                
                
            
        
    
    # You can add more methods if required