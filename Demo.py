# Demonstration of Lists vs Tuples in Python

# 1. Creation and Basic Operations
my_list = [1, "hello", 3.14]
my_tuple = (1, "hello", 3.14)

print("## Basic Operations ##")
print(f"List: {my_list}")
print(f"Tuple: {my_tuple}")

# 2. Mutability Test
print("\n## Mutability Test ##")
try:
    # Lists are mutable
    my_list[1] = "world"
    print(f"Modified list: {my_list}")
    
    # Tuples are immutable
    my_tuple[1] = "world"
except TypeError as e:
    print(f"Cannot modify tuple: {e}")

# 3. Methods Demonstration
print("\n## Available Methods ##")
list_methods = [1, 2, 2, 3, 4]
tuple_methods = (1, 2, 2, 3, 4)

# List operations
list_methods.append(5)
list_methods.remove(2)
list_methods.sort()

print(f"List after operations: {list_methods}")
print(f"Count of 2 in tuple: {tuple_methods.count(2)}")
print(f"Index of 3 in tuple: {tuple_methods.index(3)}")

# 4. Memory Usage
import sys
print("\n## Memory Usage ##")
print(f"List memory size: {sys.getsizeof(my_list)} bytes")
print(f"Tuple memory size: {sys.getsizeof(my_tuple)} bytes")

# 5. Performance Test
import time

def performance_test():
    print("\n## Performance Test ##")
    # Creating large sequences
    size = 1000000
    
    # List access
    list_time = time.time()
    test_list = list(range(size))
    for i in range(len(test_list)):
        _ = test_list[i]
    list_time = time.time() - list_time
    
    # Tuple access
    tuple_time = time.time()
    test_tuple = tuple(range(size))
    for i in range(len(test_tuple)):
        _ = test_tuple[i]
    tuple_time = time.time() - tuple_time
    
    print(f"List access time: {list_time:.4f} seconds")
    print(f"Tuple access time: {tuple_time:.4f} seconds")

performance_test()