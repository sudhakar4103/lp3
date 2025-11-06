import time

# ---------- Recursive Fibonacci ----------
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# ---------- Non-Recursive Fibonacci ----------
def fib_non_recursive(n):
    n1, n2 = 0, 1
    print(n1, n2, end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1, n2 = n2, n3
    print()

# ---------- Main Function ----------
def main():
    n = int(input("Enter the number of elements: "))

    print("\nFibonacci Sequence (Recursive): ", end="")
    start1 = time.time()
    for i in range(n):
        print(fib_recursive(i), end=" ")
    end1 = time.time()
    time_recursive = (end1 - start1) * 1_000_000  # microseconds

    print("\n\nFibonacci Sequence (Non-Recursive): ", end="")
    start2 = time.time()
    fib_non_recursive(n)
    end2 = time.time()
    time_nonrecursive = (end2 - start2) * 1_000_000  # microseconds

    # ---------- Time & Space Complexity ----------
    print("\n=== Time and Space Complexity Analysis ===")
    print(f"Recursive Time Taken: {time_recursive:.2f} microseconds")
    print("Recursive Time Complexity: O(2^n)")
    print("Recursive Space Complexity: O(n)\n")

    print(f"Non-Recursive Time Taken: {time_nonrecursive:.2f} microseconds")
    print("Non-Recursive Time Complexity: O(n)")
    print("Non-Recursive Space Complexity: O(1)")

if __name__ == "__main__":
    main()
# Theory :
# The recursive function fib_recursive(n) calls itself twice for every step, leading to exponential time complexity (O(2ⁿ)).

# The non-recursive version uses iteration, making it linear (O(n)).

# Space usage:

# Recursive → uses stack frames for each call → O(n)

# Non-recursive → only a few variables → O(1)    
