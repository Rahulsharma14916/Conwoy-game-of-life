# 🧬 Cellular Automaton — Conway's Game of Life

A Python implementation of **Conway's Game of Life**, a classic example of a **cellular automaton** where simple local rules generate complex and emergent behavior.

The simulation runs on a **1000 × 1000 grid** and uses NumPy for efficient computation and Pygame for visualization.

## 🌌 About the Project

Conway's Game of Life is a zero-player simulation created by mathematician **John Horton Conway**.

Each cell in the grid can exist in one of two states:

- 🟩 **Alive**
- ⬛ **Dead**

The state of each cell in the next generation depends only on the states of its eight neighboring cells.

Despite having extremely simple rules, the system can produce surprisingly complex patterns, including moving structures, oscillators, and self-sustaining configurations.

This project explores the concept of **emergence** — how complex global behavior can arise from simple local interactions.

## 📜 Rules

For every cell:

### Living Cell

A living cell:

- **Dies from underpopulation** if it has fewer than 2 neighbors.
- **Survives** if it has 2 or 3 neighbors.
- **Dies from overpopulation** if it has more than 3 neighbors.

### Dead Cell

A dead cell:

- **Becomes alive** if it has exactly 3 living neighbors.

In short:

```text
Alive + 2 or 3 neighbors → Alive
Alive + <2 or >3 neighbors → Dead
Dead  + 3 neighbors       → Alive
```

## 🛠️ Technologies Used

- **Python**
- **NumPy** — efficient manipulation of the 1000 × 1000 grid
- **Pygame** — real-time visualization

## 📁 Project Structure

```text
cellular-automaton/
│
├── game_of_life.py
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd cellular-automaton
```

### 2. Install dependencies

```bash
pip install numpy pygame
```

Or:

```bash
pip install -r requirements.txt
```

### 3. Run the simulation

```bash
python game_of_life.py
```

## 🧮 Grid

The simulation uses a:

```text
1000 × 1000
```

grid containing:

```text
1,000,000 cells
```

Each cell is represented by a binary state:

```text
0 → Dead
1 → Alive
```

NumPy allows the neighboring-cell calculations to be performed efficiently without relying entirely on Python-level loops.

## 🖥️ Visualization

The 1000 × 1000 simulation is scaled to fit inside the Pygame window.

The simulation continuously:

```text
Current Grid
     ↓
Count Neighbors
     ↓
Apply Rules
     ↓
Generate Next Grid
     ↓
Render
     ↓
Repeat
```

## 🔬 Concepts Explored

This project is a starting point for exploring several interesting concepts:

- Cellular Automata
- Emergent Behavior
- Local vs. Global Behavior
- Computational Simulation
- Discrete-Time Systems
- Artificial Life
- Complex Systems
- Parallel/Vectorized Computation

## 🧠 Why Is This Interesting?

The fascinating part of the Game of Life is that **there is no central intelligence controlling the system**.

Every cell follows the same simple rules.

Yet, when millions of cells interact, complex structures can emerge.

This demonstrates a fundamental idea in complex systems:

> **Simple rules can produce unexpectedly complex behavior.**

## 🔮 Future Improvements

Possible extensions to the project include:

- [ ] Interactive cell placement using the mouse
- [ ] Pause / Resume simulation
- [ ] Adjustable simulation speed
- [ ] Zoom and pan
- [ ] Generation counter
- [ ] Population counter
- [ ] Save and load patterns
- [ ] Predefined patterns such as Gliders and Gosper Glider Guns
- [ ] Different cellular automaton rules
- [ ] Multiple cell species
- [ ] Energy-based organisms
- [ ] Mutation and reproduction
- [ ] Evolutionary behavior

The long-term goal is to extend the project from a simple **cellular automaton** toward a small **Artificial Life simulation**, where digital organisms can interact, reproduce, compete, and evolve.

## 📚 References

- Conway's Game of Life
- Cellular Automata
- Artificial Life
- Complex Systems
- Emergence

## 👨‍💻 Author

**Rahul Sharma**

Built as an exploration of cellular automata, emergent behavior, and artificial life.
