# MemoryN.py
#SPace complexity: How much memory an algorithm uses
#List stores every score in memory

n = 4

guess = input("Predict: how many items in the list for n = 4?")
points = list(range(1, n + 1))
print("Your guess:", guess, "List:", points, "items:", len(points))

input("Predict: what happens to list size as n grows? Press Enter")
for size in [4, 10, 100, 1000]:
    print(f"n = {size:<5} List uses {size:<5} items in memory")