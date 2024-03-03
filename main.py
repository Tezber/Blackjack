from random import randint


class Cards:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class Player:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


'''def card_handler():
    card_chosen = randint(1, 10)
    if card_chosen in ace_chosen:
        print("gets ace")
        return ace.get_value()
    elif card_chosen in two_chosen:
        print("gets 2")
        return two.get_value()
    elif card_chosen in three_chosen:
        print("gets 3")
        return three.get_value()
    elif card_chosen in four_chosen:
        print("gets 4")
        return four.get_value()
    elif card_chosen in five_chosen:
        print("gets 5")
        return five.get_value()
    elif card_chosen in six_chosen:
        print("gets 6")
        return six.get_value()
    elif card_chosen in seven_chosen:
        print("gets 7")
        return seven.get_value()
    elif card_chosen in eight_chosen:
        print("gets 8")
        return eight.get_value()
    elif card_chosen in nine_chosen:
        print("gets 9")
        return nine.get_value()
    elif card_chosen in ten_chosen:
        print("gets 10")
        return ten.get_value()
'''


def better_card_handler(player):
    card_chosen = randint(1, 10)
    if card_chosen == 1 and player == user:
        ace_card = int(input("You got an ace what number do you want the card to be? (1 or 11): "))
        card_chosen = ace_card
    return card_chosen


def win_condition():
    if player_cards[0] > 21:
        print("Dealer won!")
        print("Your cards: ", player_cards)
        print("Dealers cards: ", dealer_cards)
        return False
    elif dealer_cards[0] > 21:
        print("You won!")
        print("Your cards: ", player_cards)
        print("Dealers cards: ", dealer_cards)
        return False
    else:
        return True


CPU = Player("Dealer")
user = Player("You")
dealer_cards = []
player_cards = []
running = True

print("Lets play blackjack!")

for cards in range(2):
    dealer_cards.append(better_card_handler(CPU))
    player_cards.append(better_card_handler(user))
print("You has a total: ", sum(player_cards))
print("Dealer has a total:", sum(dealer_cards))

while running:
    print("Do you want to draw another card? (y/n)")
    draw = input()
    draw = draw.upper()

    if draw == "Y":
        player_cards.append(better_card_handler(user))
        print(user.get_name(), "has a total: ", sum(player_cards))
        running = win_condition()
        if sum(dealer_cards) < 16:
            dealer_cards.append(better_card_handler(CPU))
            print(CPU.get_name(), "has a total: ", sum(dealer_cards))
            running = win_condition()
        else:
            print("The dealer has stuck, cards are as shown in total amounts.")
            print("total:", dealer_cards)

    elif draw == "N":
        if (player_cards > dealer_cards and 21 >= sum(player_cards) > 16) or (
                sum(dealer_cards) > 21 and sum(dealer_cards) > 16):
            print("You won!")
            running = False

        elif (dealer_cards > player_cards and 21 >= sum(dealer_cards) > 16) or (
                sum(player_cards) > 21 and sum(player_cards) > 16):
            print("Dealer won!")
            running = False

        else:
            print("Cards below 16 please draw again.")
