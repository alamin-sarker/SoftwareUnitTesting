"""Software Unit Testing Report
Scissor Paper Rock game using Test Driven Development"""

import random


class RockPaperScissor():
    '''Rock paper scissor class'''

    choice_list = ["rock", "paper", "scissor"]
    score_limit = 5
    winner = ["user", "computer", "tie"]  # index 0(user), 1(computer), 2(tie)

    def computer_select(self):
        '''computer randomly picks one of the options'''
        return random.choice(self.choice_list)

    @staticmethod
    def user_choice():
        '''player type one of the options of scissor, paper and rock.'''
        user_guess = input(
            "Please enter rock or paper or scissors "
            "for your choice or Q to quit game: ").lower().strip()
        return user_guess

    @staticmethod
    def add_point_to_winner(current_score):
        '''One point is given to the winner'''
        current_score += 1
        return current_score

    def check_winner(self, current_score):
        '''The first to get five points wins the game.'''
        point_reached = False
        if current_score == self.score_limit:
            point_reached = True
        return point_reached

    def determine_winner(self, user_choice, computer_choice):
        '''compare selections and determine who the winner is'''
        new_winner = self.winner[2]

        if computer_choice == "paper" and user_choice == "rock":
            new_winner = self.winner[1]

        elif computer_choice == "rock" and user_choice == "paper":
            new_winner = self.winner[0]

        elif computer_choice == "rock" and user_choice == "scissor":
            new_winner = self.winner[1]

        elif computer_choice == "scissor" and user_choice == "rock":
            new_winner = self.winner[0]

        elif computer_choice == "paper" and user_choice == "scissor":
            new_winner = self.winner[0]

        elif computer_choice == "scissor" and user_choice == "paper":
            new_winner = self.winner[1]
        else:
            new_winner = self.winner[2]

        return new_winner

    def play(self):
        '''playing game with logic and printing results/outputs'''

        user_score = 0
        computer_score = 0
        round_count = 0

        # loop until score limit(5) is reached
        while user_score != self.score_limit or \
                computer_score != self.score_limit:

            user_select = self.user_choice()  # user choice as input

            # checking if user choice is rock, paper or scissor
            if user_select in self.choice_list:

                round_count += 1
                print("Round:", round_count)

                # getting computer's choice
                computer_select = self.computer_select()
                print("Computer chose:", computer_select)
                # determining the winner
                winner = self.determine_winner(user_select, computer_select)

                if winner == "user":
                    # adding score for winner #noqa: E501
                    user_score = self.add_point_to_winner(user_score)
                    print("You win :)")
                    print("Your score is:", user_score)
                    print("Computer's score is:", computer_score)

                elif winner == "computer":
                    computer_score = self.add_point_to_winner(computer_score)
                    print("Computer win :(")
                    print("Computer's score is:", computer_score)
                    print("Your score is:", user_score)

                else:  # if nobody is a winner then its a tie
                    print("Tie!!")

                # checking if anyone reached the score limit
                if self.check_winner(user_score) or \
                        self.check_winner(computer_score):

                    if self.check_winner(user_score):
                        print("\nCongrats you won :)")
                        print("Number of rounds played in total: {}"
                              .format(round_count))
                    else:
                        print("\nComputer won the Game, better luck next time.")  # noqa: E501
                        print("Number of rounds played in total: {}"
                              .format(round_count))
                    break

                print("\n")

            elif user_select == 'q':  # quit the game at any time
                break
            else:  # for invalid user input
                print("Please type rock, paper, scissors or Q as your input.")

    def replay(self):
        '''player can quit or restart the game after winner is determined'''
        exit_game = False

        while not exit_game:  # paly until user quit the game
            self.play()

            game_status = input(
                "\nTo exit the game enter Q or to restart "
                "enter RS: ").lower().strip()

            if game_status == "q":
                exit_game = True
            elif game_status == "rs":
                exit_game = False
            else:
                print("Please enter Q or RS.")


def main():
    '''main method'''
    game = RockPaperScissor()
    game.replay()


if __name__ == "__main__":
    main()
