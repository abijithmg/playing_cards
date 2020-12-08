import random
import gc

class PlayingCards():
    def __init__(self):
        self.suits = ["Clubs", "Hearts", "Spades", "Diamond"]
        self.card_names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.initial_deck = []
        for suit in self.suits:
            for card_name in self.card_names:
                self.initial_deck.append(card_name + " of " + suit)
        # Shuffle the cards before game starts
        random.shuffle(self.initial_deck)
        # Create a shallow copy of deck in order restore deck once restart is selected
        self.playing_deck = self.initial_deck.copy()

    def display_deck(self):
        print(f"Remaining cards on deck :::: {len(self.playing_deck)}")

    def play_card(self):
        # using pop function to remove the card at the top of the deck stack
        print(f"\nYou picked card: {self.playing_deck.pop()}\n")
        self.display_deck()

    def shuffle_deck(self):
        random.shuffle(self.playing_deck)
        print("\nShuffled the deck!!\n")
        self.display_deck()

    def restart_game(self):
        restart_input = input("Are you sure you want to restart game? (Y/N) : ")
        if restart_input.upper() == "Y":
            self.playing_deck = self.initial_deck.copy()
            print("\nStarted new game!!")
            self.display_deck()
        else:
            return

if __name__=="__main__":
    print("\n############################\nWelcome to Simple Card Game:\n############################\n")
    print("Rules: Subject to market risk, please read email shared by HR carefully :)!")
    
    pc = PlayingCards()
    # infinite loop until user exits
    while(True):
        try:
            print("\nGame Menu:\n1 : Play a Card\n2 : Shuffle\n3 : Restart \n4 : Quit\n")
            primary_input = int(input("Please enter your choice: "))
            if primary_input == 1:
                pc.play_card()
            elif primary_input == 2:
                pc.shuffle_deck()
            elif primary_input == 3:
                pc.restart_game()
            elif primary_input == 4:
                quit_inp = input("Are you sure want to quit game? (Y/N) : ")
                # using upper function to suit our needs, in case user enters lower case
                if quit_inp.upper() == "Y":
                    print("Until next time!! BYE")
                    # explicity free memory before exit
                    gc.collect()
                    exit()
                else:
                    continue
            else:
                print("ERROR: Please enter a VALID choice!!")
        except ValueError as e:
            print("ValueError: Please enter a number from 1 to 4 !!")