# AI 680 / CS 666 — Study Materials

**Course:** Artificial Intelligence: Present and Future  
**Institution:** Long Island University — Palmer School  
**Instructor:** Dr. Kewei "Isaac" Li  
**Textbook:** Russell & Norvig, *AI: A Modern Approach* (4th ed.)  
**Term:** Spring 2026

---

## What's in This Repository

Interactive visualizations, annotations, and reference materials built alongside the course. All HTML files are standalone — open them directly in any browser, no installation required.

---

## Interactive Visualizations

### `learning_agent_diagram.html` — Ch. 2: Learning Agents
Tabbed interactive guide to the four-component learning agent architecture from Russell & Norvig.

- **Overview tab:** Annotated SVG diagram of the full agent loop (environment → percepts → performance element → actions → critic → learning element → problem generator)
- **Component Details tab:** Role, function, and examples for each of the four components
- **Real Examples tab:** Self-driving cars, AlphaGo, spam filters, and a direct connection to the OULAD project
- **Non-Learning vs. Learning tab:** Key distinctions, autonomy, and a direct quote from R&N

---

### `lifo_fifo_search.html` — Ch. 3: DFS & BFS via Data Structures
Step-through visualization demonstrating that the frontier data structure *is* the search strategy.

- Toggle between **DFS (LIFO stack)** and **BFS (FIFO queue)** modes
- Animated step-by-step traversal of a 9-node tree with live frontier state
- Step-by-step log table tracking node expanded, nodes added, and frontier contents
- Summary verdict explaining why you cannot separate strategy from structure

---

### `chapter4_visual_guide.html` — Ch. 4: Local Search & Optimization
Visual guide to local search algorithms, optimization landscapes, and partially observable problems.

- **Landscapes tab:** SVG state-space landscape annotated with local maxima, global maximum, plateaus, ridges, and dead ends
- **Algorithms tab:** Comparison cards for hill climbing, simulated annealing, local beam search, and genetic algorithms with pros/cons and a selection guide
- **Continuous Spaces tab:** Gradient descent, Newton-Raphson, constrained optimization
- **Partial Observability tab:** Sensorless and contingency problems, belief states, AND-OR search
- **Online Search tab:** LRTA*, competitive ratio, real-time agent constraints

---

### `ch5_adversarial_search.html` — Ch. 5: Adversarial Search & Games
Seven-section interactive guide covering the full chapter.

- **Overview:** Formal game definition table (S₀, TO-MOVE, ACTIONS, RESULT, IS-TERMINAL, UTILITY), three game types (deterministic, stochastic, partial), zero-sum clarification
- **Minimax:** Step-through two-ply tree with backed-up value animation; MAX/MIN node roles; multiplayer vector extension
- **Alpha–Beta Pruning:** Live α/β tracker updating each step, pruned node visualization, move ordering impact bars (best vs. random ordering complexity)
- **Heuristic Evaluation:** H-MINIMAX formula, weighted linear evaluation function, quiescence search, horizon effect, forward pruning
- **MCTS:** Four clickable phase cards (Selection → Expansion → Simulation → Back-Propagation); interactive UCT formula where each term expands on click
- **Stochastic & Partial:** Expectiminimax formula with chance nodes, belief states, probabilistic checkmate, equilibrium strategies
- **Algorithm Comparison:** Full complexity table across all algorithms; R&N's four identified limitations

---

## Study Documents

### `AI_Modern_Approach_Ch1-3_Annotations.md`
Structured annotations for Chapters 1–3 with key terms, definitions, real-world examples, and blank reflection space organized in three-column tables.

### `AI_Concepts_Visual_Organizers.pptx`
Ten-slide PowerPoint with visual concept maps for agent architectures, search strategy comparisons, environment properties, and heuristic design — suitable for review or sharing with classmates.

---

## Course Roadmap

| Week | Topic | Chapters | Visualizations |
|------|-------|----------|----------------|
| 1 | Overview & Introduction | Ch. 1 | — |
| 2 | Intelligent Agents, Basic Search | Ch. 2–3 | `learning_agent_diagram.html` · `lifo_fifo_search.html` |
| 3 | Informed Search, Game Playing | Ch. 4–5 | `chapter4_visual_guide.html` · `ch5_adversarial_search.html` |
| 4 | Logical Agents, First Order Logic | Ch. 7–8 | *(planned)* |
| 5 | Inference, Knowledge Representation | Ch. 9–10 | *(planned)* |
| 6 | Probabilistic Reasoning | Ch. 12–13 | *(planned)* |
| 7 | Bayesian Networks, MDPs | Ch. 13–14 | *(planned)* |
| 8 | Linear Programming, CSP | Ch. 4, 6 | *(planned)* |
| 9 | Machine Learning | Ch. 19–20 | *(planned)* |
| 10 | Deep Learning | Ch. 21 | *(planned)* |
| 11 | Computer Vision, Reinforcement Learning | Ch. 25, 22 | *(planned)* |
| 12 | NLP, Large Language Models | Ch. 23–24 | *(planned)* |
| 13–14 | Robotics & AI Ethics | Ch. 26–27 | *(planned)* |

---

## Usage

All HTML files are fully self-contained. To use them:

1. Download the file
2. Open in any modern browser (Chrome, Firefox, Safari, Edge)
3. No server, no dependencies, no installation

To share with classmates, either send the file directly or deploy to GitHub Pages (Settings → Pages → main branch).

---

**Kyle Allen Sherman**  
PhD Program in Information Studies  
kyle.allen.sherman@pm.me
