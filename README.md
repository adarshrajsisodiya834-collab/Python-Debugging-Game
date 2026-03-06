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

Planned features and ideas for upcoming versions of the project.

### Gameplay Improvements

* ⏱ **Time-Bound Challenges**
  Add a timer for each debugging problem to simulate real coding pressure.

* 🎯 **Multiple Game Modes**

  * **Practice Mode** – unlimited time, focus on learning
  * **Challenge Mode** – timed debugging rounds
  * **Survival Mode** – continue until a mistake is made

* 📈 **Level Progression System**
  Automatically increase difficulty as the player solves more problems.

* 🏆 **Level-Up Rewards**

  * Unlock harder debugging challenges
  * Bonus points for streaks
  * Achievement badges for milestones

### Learning Features

* 💡 **Hints System**
  Players can request hints that guide them toward the bug without revealing the answer.

* 📚 **Detailed Explanations**
  Show why the bug occurred and how to fix it properly.

* 🧠 **Bug Type Categories**

  * Syntax errors
  * Logic errors
  * Runtime errors
  * Common beginner mistakes

### Content Expansion

* 📦 **Large Problem Library**
  Expand the problem database to 100+ debugging challenges.

* 🔄 **Randomized Challenge Selection**
  Prevent repeating the same debugging problems frequently.

* 📊 **Performance Tracking**
  Track solved problems, accuracy, and improvement over time.

### Interface Improvements

* 🌐 **Web Version (Flask)**
  Convert the CLI game into a browser-based debugging trainer.

* 🎨 **Improved CLI Interface**

  * Colored output
  * Clearer prompts
  * Better feedback messages

* 🏁 **Leaderboard System**
  Track top scores and fastest debugging times.

### Developer Improvements

* 🧩 **Modular Game Engine**
  Separate gameplay logic, UI, and problem database for easier expansion.

* 🧪 **Unit Tests**
  Add automated tests for the engine and problem loader.

* 📜 **Better Documentation**
  Provide contributor guidelines and developer documentation.


## License

MIT License
