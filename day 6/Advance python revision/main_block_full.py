"""
__name__ == "__main__"
"""

def main():
    print("Main running")

def helper():
    print("Helper")

if __name__ == "__main__":
    main()

# ------------------ PROBLEM ------------------

# Add another function and call only in main
def test():
    print("Test function")

if __name__ == "__main__":
    test()