# Python Debugging Game

A **CLI-based training engine** designed to help beginners practice **debugging Python code** through interactive challenges.

## Features

*  Python debugging challenges
*  Beginner → Intermediate → Advanced levels
*  Level and group based progression
*  Problems stored in JSON for easy expansion
*  Runs entirely in the terminal

## Project Structure

```
python-debugging-game
│
├── main.py              # Entry point
├── engine.py            # Game logic
├── problem_loader.py    # Loads problems from JSON
├── problems.json        # Debugging challenges
├── .gitignore
├── LICENSE
└── README.md
```

## How to Run

Clone the repository:

```
git clone https://github.com/Adarsh_Raj_Sisodiya/Python-Debugging-Game.git
cd Python-Debugging-Game
```

Run the game:

```
python main.py
```

## Example Gameplay

```
=== Python Debugging Training Engine ===

Find the faulty line:

1: def add(a, b):
2:     return a - b
3:
4: print(add(5, 3))

Your answer:
```

## Current Version

**v0.1 – CLI Prototype**

Includes:

* Level-based debugging challenges
* JSON-driven problem system
* Terminal gameplay

## Future Improvements

*  Web version using Flask
*  Score tracking
*  Timed challenges
*  More debugging problems

## License

MIT License
