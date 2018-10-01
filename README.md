# Blackjack
This is a console-based, Unix-compatible, simplified version of the popular card game Blackjack.

# Instructions for running
To play, navigate to this directory after cloning/forking and run `python main.py`. 
To run tests, run `python test.py`.

# Rules
For the sake of this exercise, I decided to simplify the rules a little. The changes are listed below:

* A maximum of 4 players (including yourself) are allowed.
* No gambling has been incorporated at all.
* You are only allowed to hit (get an additional card) or stand (stop receiving cards) - there is no option to double or split.
* In a normal game of Blackjack, it is possible to lose to the dealer if you have 21 and the dealer has blackjack (21 with the original 2 cards dealt). This has not been implemented - that case will be treated as a normal tie.

# Design choices
I determined that a card game like Blackjack should be separated into three objects: *card*, *player*, and *game*. The card, the simplest class carries a name and point value. Players can then have a *hand*, which consists of these cards, and methods for showing and checking the hand. The game then controls the overall game state, which includes generating the initial deck and other players as well as dealing cards and determining winners.

One choice I made was to make the dealer a Player. This allowed me to reuse logic from showHand and checkHand on the dealer, since really the dealer is just a special player in the game of Blackjack. I considered making the dealer his own special class, but I concluded that it was not worthwhile and just made the implementation more complicated.

The directory is split up accordingly to these classes (card.py, player.py, game.py, and main.py for the main executable). 

# Tools used
I used Python 2.7 due to its simple syntax and my ability to quickly translate business logic into a terminal-based program with its use. For libraries, I only used Python's built-in modules:
* `random` to shuffle the deck and generate random player AI choices
* `unittest` for testing, since I did not require complicated testing and only needed to test basic functionalities

# Additional notes
* The player AI is not smart at all - it randomly chooses between hitting and standing, no matter what their hands look like or what the game state is. Exploring AI for Blackjack players sounds very interesting, but was outside the scope for this exercise.
* The game is currently designed so that the player always goes first, which puts them at a slight disadvantage since they do not see the updated game board state after the other players go. The code is unfortunately not designed in a way that the player order can be changed easily - in the future, that should be considered when designing a system like this.
* Player input (for name, number of players, decision) are not thoroughly sanitized. Again, in the future, this should be worked on and made more robust.
