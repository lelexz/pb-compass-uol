for i in range(2, 101):
    primo = True
    for x in range(2, i):
        if i % x == 0:
            primo = False
            break
    if primo:
        print(i)