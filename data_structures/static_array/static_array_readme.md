# Static Array

In Python, there are no true static arrays. However, this concept is an important data structure in many programming languages, and similar functionality can be achieved using libraries such as array or numpy, which provide efficient implementations for fixed-size arrays.


---

## Characteristics:

* **Uniform Data Type:** All elements in the array must be of the same type (e.g., integers, strings, floating-point numbers).

* **Fixed Size:** The size of the array is set at creation and remains constant throughout the program's execution.

* **Sequential Memory Layout:** Array elements are stored contiguously in memory, allowing for efficient access.

---

## Memory Management:
To access elements, the following formula is used:
`Element address = Starting address + (Element index × Element size)`.

---

## Indexing:
Indexing starts at 0, and the last element in the array has an index of N−1, where N is the number of elements.

---

## Operations:

| Operation          | Time Complexity   | Description                                                          |
|--------------------|-------------------|----------------------------------------------------------------------|
| **Reading and Writing** | O(1)             | Operations are performed in constant time.                            |
| **Insertion (End)**   | O(1)             | Inserting an element at the end of the array is constant time.       |
| **Insertion (Middle)**| O(N)             | Inserting an element in the middle requires shifting elements.       |
| **Deletion (End)**    | O(1)             | Deleting an element at the end is constant time.                     |
| **Deletion (Middle)** | O(N)             | Deleting an element from the middle requires shifting elements.      |

---

## Advantages:

* Fast access: O(1) for reading and writing.
* Simplicity of implementation.

---

## Disadvantages:

* Fixed size.
* Issues with insertion and deletion (O(N)).
* Inefficient memory usage for large data sets.

---

## When to Use:
Static arrays are suitable when:

* The size of the array is known in advance and will not change.
* Quick access to array elements is needed.
* The array size is relatively small.
