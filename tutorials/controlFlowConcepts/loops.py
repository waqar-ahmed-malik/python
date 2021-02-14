# ------------- break out of the loop -------------------------

nums = [1, 2, 3, 4]
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

'''prints 
1
2
Found
'''


# ---------------------------------------------------------------------------------------------------------------------

# ------------------------------ skips an iteration --------------------------

nums = [1, 2, 3, 4]
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)
'''prints 
1
2
Found
4
5
'''
# --------------------------------------------------------------------------------------------------------------------


# -------------------------- For Loop and  range function ---------------------------------------
for i in range(10):
    print(i)    # prints 0 to 9

for i in range(1, 11):
    print(i)    # prints 1 to 10

# ------------------------------------------------------------------------------------------------


# -------------------- While Loop ----------------------------------------
i=0
while i<10:
    print(i)
    i += 1          # prints 0 to 9

while i<=10:
    print(i)
    break           # prints 1 then breaks so only "1" is printed.
    i += 1
