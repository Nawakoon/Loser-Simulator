from core import you

print(
    """
                let's play a game
    """
)
you.help()


while you.winning_status != True:
    answer = input("what you'll do : ")
    if answer == "pet":
        you.pet()
    elif answer == "feed":
        you.money = you.feed()
    elif answer == "work":
        you.money = you.work()
    elif answer == "date":
        you.money, you.date_count = you.date()
    elif answer == "relationship":
        you.winning_status = you.relationship()
        if you.winning_status == True:
            break
    else:
        you.help()
