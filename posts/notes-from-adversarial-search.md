# Adversarial Search

"Playing chess the way humans play chess"

## Alternatives 
1. Analysis, Strategy & Tactics
2. If-Then Rules
3. Look ahead and evaluate | Look at all the possible moves and evaluate which one of the situations is best?  
4. British Museum Algorithm 
5. Look ahead as far as possible  
Visit [MITOCW Lecture 06](https://www.youtube.com/watch?v=STjW3eH0Cik)

## Options in a basic chess game
- move-generation
- board evaluation
- minimax
- and alpha beta pruning.

__Adversarial search__: when there is an 'opponent' changing the state of the problem at every step in a direction you do not want.
You change state, but then you don't control the next state. 
Examples: Chess, business, trading, war. 


A game can be defined by the 
- __initial state__ (how the board is set up)
- __legal actions__ in each state
- __result__ of each action
- __terminal test__ (which says when the game is over) 
- __utility function__ applies to terminal states.  


# MiniMax 
![MinMax](https://upload.wikimedia.org/wikipedia/commons/6/6f/Minimax.svg)

# Alpha-Beta pruning - Making MiniMax efficient (speed up)
![Alpha-Beta](https://upload.wikimedia.org/wikipedia/commons/9/91/AB_pruning.svg)
