print("welcome to the tip calculator")
bill=int(input("What was the total bill?"))
percentage=float(input("what percentage tip would uou like to give?10, 12, or 15?"))
split=int(input("how many pedople to split the bill?"))
bill_p=bill*(percentage/100)
each=bill/split
print(f"every one pay{each}")
print(f"e{bill_p}")
