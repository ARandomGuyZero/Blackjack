"""
Blackjack Game

Author: Alan
Date: August 2024

This program simulates a simple game of Blackjack between the user and the computer.
"""

import random
import art

def deal_card():
    """
    Returns a random card from the deck.
    The deck includes numbers 2-10, and the face cards (Jack, Queen, King) all count as 10.
    The Ace can count as either 11 or 1, depending on the player's hand.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(player_cards):
    """
    Calculates the score of the player's hand.
    
    Returns 0 if the player has a Blackjack (Ace and 10).
    Converts the Ace (11) to 1 if the score exceeds 21.
    """
    score = sum(player_cards)
    if score == 21 and len(player_cards) == 2:
        return 0  # Represents a Blackjack
    
    if 11 in player_cards and score > 21:
        player_cards.remove(11)
        player_cards.append(1)
        score = sum(player_cards)
    
    return score

def compare_score(u_score, c_score):
    """
    Compares the user's score with the computer's score.
    
    Returns the result of the game as a string.
    """
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_blackjack():
    """
    Starts a game of Blackjack.
    
    The user and computer each get two cards to start. The user can choose to draw additional cards.
    The computer draws until its score is 17 or higher.
    The game ends when either the user or computer has a Blackjack, exceeds 21, or the user decides to stop drawing cards.
    """
    print(art.logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Initial dealing of two cards for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(player_cards=user_cards)
        computer_score = calculate_score(player_cards=computer_cards)

        print(f"Your hand: {user_cards}. Total score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("Do you want to draw another card? (y/n)\n").lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn to draw cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(player_cards=computer_cards)

    # Show final hands and determine the winner
    print(f"Your final hand: {user_cards}. Final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}. Final score: {computer_score}")
    print(compare_score(u_score=user_score, c_score=computer_score))

# Game loop to allow replay
while input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower() == "y":
    print("\n" * 20)
    play_blackjack()
