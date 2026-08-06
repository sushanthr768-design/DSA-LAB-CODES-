def print_countdown(n):
        if n < 0:
            return
        print(n)
        print_countdown(n-1)

print_countdown(10)
print("LAUNCH")
