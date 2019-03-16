#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class HumanPlayer(Player):
    def move(self):
        my_move = input("rock, paper or scissors?")
        if my_move == "rock":
            return "rock"
        elif my_move == "paper":
            return "paper"
        elif my_move == "scissors":
            return "scissors"
        else:
            print("Try Again")

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class ReflectPlayer():
    def move(self):
        if self.thier_move == None:
            return random.choice(moves)
        else:
            return self.their_move

class CyclePlayer(Player):
    def move(self):
        my_move = random.choice(moves)
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0
        self.ties = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            self.p1.score += 1
        elif beats(move2, move1) is True:
            self.p1.score += 1
        else:
            self.ties

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print(f" Player 1 score: {self.p1.score}, Player 2 score: {self.p2.score}")
            if self.p1.score > self.p2.score:
                print("You Win!")
            elif self.p1.score < self.p2.score:
                print("You Lose")
            else:
                print("Tie")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()