l =['smartphone','laptop','airpods','shoes']
for i in l:
    if i == "laptop":
        break
    print(i.center(20,'_'))

else:
    print("End of the items")

bullets = 10
while bullets > 0:
    if bullets == 5:
        print("Dead")
        break
    print(f"{bullets} are left - You can shoot()")
    bullets -= 1

else:
    print("Game over")