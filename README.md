# AI 680 — Study Materials & Interactive Visualizations

Course notes, interactive diagrams, and reference materials for **AI 680 / CS 666: Artificial Intelligence — Present and Future** at Long Island University.

Based on Russell & Norvig's *Artificial Intelligence: A Modern Approach* (4th Edition).

---

## 📁 Repository Structure

```
/
├── Chapters 1–3
│   ├── index.html                               — Interactive concept explorer
│   ├── learning_agent_diagram.html              — Learning agent architecture diagram
│   ├── lifo_fifo_search.html                    — DFS vs BFS / LIFO vs FIFO visualizer
│   ├── AI_Concepts_Visual_Organizers.pptx       — 10-slide presentation
│   └── AI_Modern_Approach_Ch1-3_Annotations.md — Study annotations & key terms
│
├── Chapters 4–5
│   ├── chapter4_visual_guide.html               — Local search, optimization & partial observability
│   └── ch5_adversarial_search.html              — Minimax, alpha–beta, MCTS & stochastic games
│
├── Chapter 6
│   └── ch6_csp.html                             — Constraint satisfaction: AC-3, backtracking & graph structure
│
├── Homework
│   ├── maze_a-star_explained.ipynb              — HW 3.1: BFS vs UCS on a weighted graph
│   └── maze_bfs_explained.ipynb                 — HW 3.2: A* search on a 10×10 grid
│
└── (more chapters added as course progresses)
```

---

## 📚 Chapters Covered

### Chapters 1–3 — Introduction, Intelligent Agents, Search
| File | Type | Description |
|------|------|-------------|
| `index.html` | Interactive | Concept explorer with hierarchy view, relationships map, learning path timeline, and algorithm comparisons |
| `learning_agent_diagram.html` | Interactive | Four-component learning agent architecture (Performance Element, Learning Element, Critic, Problem Generator) with real-world examples and tabbed views |
| `lifo_fifo_search.html` | Interactive | Step-by-step visualizer showing how LIFO stacks produce DFS and FIFO queues produce BFS — includes animated frontier tracking and step log |
| `AI_Concepts_Visual_Organizers.pptx` | Slides | 10 professionally designed slides covering agent architecture, search strategies, A*, environment properties, and bounded rationality |
| `AI_Modern_Approach_Ch1-3_Annotations.md` | Reference | 100+ key terms with definitions, historical context, real-world examples, and reflection space — organized by chapter |

### Chapters 4–5 — Local Search, Informed Search, Game Playing
| File | Type | Description |
|------|------|-------------|
| `chapter4_visual_guide.html` | Interactive | Local search algorithms, optimization landscapes, partial observability, and online search — includes animated hill climbing and simulated annealing |
| `ch5_adversarial_search.html` | Interactive | Minimax, alpha–beta pruning, heuristic evaluation, MCTS, stochastic games, and imperfect information — step-through trees with live α/β tracker |

### Chapter 6 — Constraint Satisfaction Problems
| File | Type | Description |
|------|------|-------------|
| `ch6_csp.html` | Interactive | CSP formal definition, constraint types, AC-3 with animated Australia map coloring, backtracking with conflict-directed backjumping, MRV/LCV heuristics, and graph structure decomposition |

---

## 📓 Homework Notebooks

Annotated Jupyter notebooks explaining the reasoning behind each implementation, not just the code. Designed to run in Google Colab.

| File | HW | Description |
|------|-----|-------------|
| `maze_a-star_explained.ipynb` | HW 3.1 | BFS vs UCS on a weighted directed graph (A→G). Covers FIFO vs min-heap frontier structures, adjacency list construction, lazy deletion in UCS, and side-by-side path visualization |
| `maze_bfs_explained.ipynb` | HW 3.2 | A* search on a 10×10 obstacle grid. Covers Manhattan distance admissibility, the g/h/f cost breakdown, closed set logic, coordinate flip for matplotlib, and a bonus A* vs UCS node-expansion comparison |

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

---

## 🚀 Quick Start

**HTML visualizations** — fully standalone, no installation required:
1. Click any `.html` file in the repository
2. Open via GitHub Pages, or clone/download and open locally in any modern browser
3. Works on desktop and tablet (Chrome/Safari recommended)

**Jupyter notebooks** — open directly in Google Colab:
1. Navigate to the `.ipynb` file on GitHub
2. Replace `github.com` in the URL with `githubtocolab.com`, or use File → Open in Colab

---

## 🗺️ Roadmap — Upcoming Chapters

| Week | Chapter(s) | Topic | Status |
|------|-----------|-------|--------|
| 1–3 | Ch. 1–3 | Introduction, Agents, Search | ✅ Complete |
| 4 | Ch. 4–5 | Informed Search, Game Playing | ✅ Complete |
| * | Ch. 6 | Constraint Satisfaction Problems | ✅ Complete |
| 5 | Ch. 7–8 | Logical Agents, First-Order Logic | 🔲 Planned |
| 6 | Ch. 9–10 | Inference, Knowledge Representation | 🔲 Planned |
| 7 | Ch. 12–13 | Probabilistic Reasoning | 🔲 Planned |
| 8 | Ch. 13–14 | Bayesian Networks, MDPs | 🔲 Planned |
| 9 | Ch. 19–20 | Machine Learning | 🔲 Planned |
| 10 | Ch. 21 | Deep Learning | 🔲 Planned |
| 11 | Ch. 22, 25 | Reinforcement Learning, Computer Vision | 🔲 Planned |
| 12 | Ch. 23–24 | NLP, Large Language Models | 🔲 Planned |
| 13–14 | Ch. 26–27 | Robotics, AI Ethics | 🔲 Planned |

---

## 🎓 Course Information

- **Course**: AI 680 / CS 666 — Artificial Intelligence: Present and Future
- **Institution**: Long Island University — Palmer School
- **Instructor**: Dr. Kewei "Isaac" Li
- **Term**: Spring 2026
- **Textbook**: Russell & Norvig, *AI: A Modern Approach*, 4th Edition

---

## 🆘 Troubleshooting

**Page doesn't load on tablet** — Use Chrome or Safari with JavaScript enabled. Try clearing cache if needed.

**GitHub Pages shows 404** — Wait 2–3 minutes after enabling Pages. Confirm `index.html` is in the root directory and Pages is enabled under Settings → Pages.

---

## 📄 License

Provided for academic use. Content is based on publicly available AI concepts from Russell & Norvig's textbook.

## 🙏 Acknowledgments

- Stuart Russell and Peter Norvig — *AI: A Modern Approach*
- Dr. Kewei "Isaac" Li — Course Instructor, LIU
- Claude AI (Anthropic)

## 📧 Contact

**Kyle Allen Sherman** · kyle.allen.sherman@pm.me · AI 680, Spring 2026
