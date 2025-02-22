import sys
import time
from lobster import Lobster, dynamic_programming_lobster

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("The program needs exactly one file as a command line argument\n")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = "output"

    try:
        with open(input_file, 'r') as input, open(output_file, 'w') as output:
            # Read bag size
            bag_size = int(input.readline().strip())
            
            # Read each lobster's attributes
            lobster_collection = []
            for line in input:
                parts = line.strip().split()
                if len(parts) != 3:
                    continue
                name = parts[0]
                size = int(parts[1])
                value = int(parts[2])
                if size <= bag_size:
                    lobster_collection.append(Lobster(name, size, value))
            
            lobster_number = len(lobster_collection)

            # Measure execution time
            start = time.time()

            # Function call
            dynamic_programming_lobster(lobster_collection, lobster_number, bag_size, output)

            end = time.time()
            output.write(f"\nTime: {end - start} seconds\n")

    except IOError as e:
        sys.stderr.write(f"Failed to open files: {e}\n")
        sys.exit(2)

if __name__ == "__main__":
    main()
