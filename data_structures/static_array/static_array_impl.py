from StaticArray.StaticArray import StaticArray
import array


if __name__ == '__main__':
    size = 10
    
    # Using StaticArray class
    my_static_array = StaticArray(size)
    for i in range(size):
        my_static_array[i] = i
    
    print("My Static Array:")
    print(my_static_array)

    # Using the array module from Python standard library
    static_array = array.array('i', list(range(size)))
    
    print("\nLibrary Static Array (array module):")
    print(static_array)