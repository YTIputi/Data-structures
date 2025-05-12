from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class StaticArray(Generic[T]):
    '''
    Attempted to recreate a static array data structure with a fixed size.
    This class emulates an array where elements can be accessed, inserted,
    and deleted at specific indices. The array does not automatically resize,
    and the elements are initially set to None (optional) until assigned a value.
    '''
    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        self.size = size
        self.array: list[Optional[T]] = [None] * size

    def __getitem__(self, index: int) -> Optional[T]:
        '''Getter method to retrieve an element at a specific index'''
        self.__validate_index(index)
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        '''Setter method to assign a value at a specific index'''
        self.__validate_index(index)
        self.array[index] = value

    def __len__(self) -> int:
        '''Method to return the size of the array'''
        return self.size

    def __str__(self) -> str:
        '''Method to return a string representation of the array'''
        return "[" + ", ".join(str(el) if el is not None else "_" for el in self.array) + "]"

    def __validate_index(self, index: int) -> None:
        '''Private method to validate if an index is within the valid range'''
        if not 0 <= index < self.size:
            raise IndexError(f"Index {index} out of range [0, {self.size - 1}]")
        
    def insert(self, index: int, value: T) -> None:
        '''Method to insert a value at a specific index, shifting elements if necessary'''
        self.__validate_index(index)
        space_index = None
        for i in range(index, self.size - 1):
            if self.array[i] is None:
                space_index = i
                break
        if space_index is None:
            raise OverflowError("No space to insert at the given index.")
        for i in range(space_index, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value

    
    def delete(self, index: int) -> Optional[T]:
        '''Method to delete an element at a specific index, shifting elements if necessary'''
        self.__validate_index(index)
        removed = self.array[index]
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        return removed

        


    
    