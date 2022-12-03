from auxiliary_functions import read_csv_data
from enum import Enum


# Add points for chosen shape: 1 for Rock, 2 for Paper, and 3 for Scissors
class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# Calculate outcome and add respective points: 0 if you lost, 3 if the round was a draw, and 6 if you won
class Outcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


def solve_part_1(path: str):
    data = read_csv_data(path)
    
    total_score = 0
    for row in data:
        opponent = row[0]
        me = row[1]

        ## Calculate the outcome of the round
        # Opponent plays: A for Rock, B for Paper, and C for Scissors
        # You play:       X for Rock, Y for Paper, and Z for Scissor
        outcome_of_round = 0
        match me:
            case 'X':
                outcome_of_round += Shape.ROCK.value

                match opponent:
                    case 'A':
                        outcome_of_round += Outcome.DRAW.value # RR = Draw
                    case 'B':
                        outcome_of_round += Outcome.LOSS.value # RP = Lose
                    case 'C':
                        outcome_of_round += Outcome.WIN.value # RS = Win
            case 'Y':
                outcome_of_round += Shape.PAPER.value

                match opponent:
                    case 'A':
                        outcome_of_round += Outcome.WIN.value # PR = Win
                    case 'B':
                        outcome_of_round += Outcome.DRAW.value # PP = Draw --> There was a bug
                    case 'C':
                        outcome_of_round += Outcome.LOSS.value # PS = Lose
            case 'Z':
                outcome_of_round += Shape.SCISSORS.value

                match opponent:
                    case 'A':
                        outcome_of_round += Outcome.LOSS.value
                    case 'B':
                        outcome_of_round += Outcome.WIN.value
                    case 'C':
                        outcome_of_round += Outcome.DRAW.value
        total_score += outcome_of_round

    print(f'Solution of part 1 = {total_score}')


def solve_part_2(path: str):
    data = read_csv_data(path)
    
    total_score = 0
    for row in data:
        opponent = row[0]
        me = row[1]

        ## Calculate the outcome of the round
        # Opponent plays: A for Rock, B for Paper, and C for Scissors
        # You will play:  X for lose, Y for draw , and Z for win
        outcome_of_round = 0
        match me:
            case 'X':
                # I will lose
                outcome_of_round += Outcome.LOSS.value

                match opponent:
                    case 'A':
                        # Opponent plays Rock --> Scissors to lose
                        outcome_of_round += Shape.SCISSORS.value
                    case 'B':
                        # Opponent plays Paper --> Rock to lose
                        outcome_of_round += Shape.ROCK.value
                    case 'C':
                        # Opponent plays Scissors --> Paper to lose
                        outcome_of_round += Shape.PAPER.value
            case 'Y':
                # I will draw
                outcome_of_round += Outcome.DRAW.value

                match opponent:
                    case 'A':
                        outcome_of_round += Shape.ROCK.value
                    case 'B':
                        outcome_of_round += Shape.PAPER.value
                    case 'C':
                        outcome_of_round += Shape.SCISSORS.value
            case 'Z':
                # I will win
                outcome_of_round += Outcome.WIN.value

                match opponent:
                    case 'A':
                        outcome_of_round += Shape.PAPER.value
                    case 'B':
                        outcome_of_round += Shape.SCISSORS.value
                    case 'C':
                        outcome_of_round += Shape.ROCK.value
        total_score += outcome_of_round

    print(f'Solution of part 2 = {total_score}')


def solve():
    path = 'day_02/input.txt'
    solve_part_1(path)
    solve_part_2(path)
