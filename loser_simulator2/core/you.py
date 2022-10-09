# import scripts
from random import randint
from core import scripts


money = randint(0, 3)
date_count = 0
winning_status = False
date_amount_to_win = randint(3, 5)


def show_money(_currentMoney):
    return "you have $ " + str(_currentMoney) + " left"


def pet():
    return print(scripts.petting)


def feed():
    current_money = money
    feed_cost = 1
    if current_money < feed_cost:
        print(scripts.feeding_no_money)
    else:
        current_money -= feed_cost
        print(scripts.feeding)
    print(show_money(current_money))
    return current_money


def work():
    work_income = 6
    current_money = money
    current_money += work_income
    print(scripts.working)
    print(show_money(current_money))
    return current_money


def date():
    current_money = money
    dated = date_count
    date_cost = 10
    if current_money >= date_cost:
        current_money -= date_cost
        dated += 1
        print(scripts.dating)
    else:
        print(scripts.dating_no_money)
    print(show_money(current_money))
    return current_money, dated


def relationship():
    current_money = money
    current_winning_status = winning_status
    if current_money >= 20 and date_count >= date_amount_to_win:
        print(scripts.relationship_win)
        current_winning_status = True
    elif current_money <= 20 and date_count >= date_amount_to_win:
        print(scripts.relationship_no_money)
        print(show_money(current_money))
    elif current_money >= 20 and date_count <= date_amount_to_win:
        print(scripts.relationship_no_date)
    else:
        print(scripts.relationship_nothing)

    return current_winning_status


def help():
    return print(
        """
                please type these to play
                
                pet           | pet a dog
                feed          | feed a dog ($1)
                work          | make $4
                date          | date with some cute girl ($10)
                relationship  | if she OK, you win
        """
    )
