from random import randint, choice


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


def better_card_handler(player):
    card_chosen = randint(1, 10)
    if card_chosen == 1 and player == user:
        card_chosen = int(input("You got an ace what number do you want the card to be? (1 or 11): "))
    if card_chosen == 1 and player == CPU:
        card_chosen = choice([1, 11])
    return card_chosen


def win_condition21():
    if sum(player_cards) == 21:
        print("You won!")
        print("Your cards: ", sum(player_cards))
        print("Dealers cards: ", sum(dealer_cards))
        return False
    if sum(dealer_cards) == 21:
        print("Dealer won!")
        print("Your cards: ", sum(player_cards))
        print("Dealers cards: ", sum(dealer_cards))
        return False
    return True


def win_condition():
    if sum(dealer_cards) < sum(player_cards):
        if sum(player_cards) > 21:
            print("Dealer won!")
            print("Your cards: ", sum(player_cards))
            print("Dealers cards: ", sum(dealer_cards))
        else:
            print("You won!")
            print("Your cards: ", sum(player_cards))
            print("Dealers cards: ", sum(dealer_cards))
        return False
    if sum(player_cards) < sum(dealer_cards):
        if sum(dealer_cards) > 21:
            print("You won!")
            print("Your cards: ", sum(player_cards))
            print("Dealers cards: ", sum(dealer_cards))
        else:
            print("Dealer won!")
            print("Your cards: ", sum(player_cards))
            print("Dealers cards: ", sum(dealer_cards))
        return False
    return True


def playerdraw():
    player_cards.append(better_card_handler(user))


def dealerdraw():
    dealer_cards.append(better_card_handler(CPU))


CPU = Player("Dealer")
user = Player("Player")
dealer_cards = []
player_cards = []
running = True

print("Lets play blackjack!")

for cards in range(2):
    dealerdraw()
    playerdraw()
print(player_cards)
print("Player has a total at: ", sum(player_cards))

while running:
    running = win_condition21()
    print("Do you want to draw another card? (y/n)")
    draw = input()
    draw = draw.upper()

    if draw == "Y":
        playerdraw()
        running = win_condition21()
        print(user.get_name(), "has a total: ", sum(player_cards))

        if sum(dealer_cards) < 16:
            dealerdraw()
        elif 21 >= sum(dealer_cards) >= 16:
            print("The dealer has stuck.")

    elif draw == "N":
        if sum(player_cards) < 16:
            print("Draw more cards. too low value")
        elif sum(player_cards) > 16 or sum(player_cards) > sum(dealer_cards):
            print("You have stuck, dealer will draw or bust")
            if sum(dealer_cards) < 16:
                dealerdraw()
                running = win_condition()
            else:
                running = win_condition()
