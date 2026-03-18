# AI: A Modern Approach - Chapters 1-3 Organized Annotations

---

## Chapter 1: Introduction

### Key Terms
Rational agent, bounded rationality, satisficing, agent function, agent program, percept, percept sequence, performance measure, autonomy, consequentialism, PEAS description, task environment, fully observable, partially observable, deterministic, nondeterministic, episodic, sequential, static, dynamic, discrete, continuous, single-agent, multiagent, simple reflex agents, model-based reflex agents, goal-based agents, utility-based agents, learning agents, atomic representation, factored representation, structured representation, distributed representation

---

### Chapter 1 Detailed Annotations

| Concept/Definition | Example | Personal Reflection |
|-------------------|---------|---------------------|
| **Natural language processing** - enables AI to communicate successfully in human language | Chatbots, translation systems, voice assistants |  |
| **Knowledge representation** - storing what the AI knows or hears | Databases, semantic networks, ontologies |  |
| **Automated reasoning** - answering questions and drawing new conclusions | Expert systems, theorem provers |  |
| **Machine learning** - adapting to new circumstances and detecting patterns | Recommendation systems, fraud detection |  |
| **Computer vision** - perceiving the world visually | Facial recognition, autonomous vehicle navigation |  |
| **Robotics** - manipulating objects and moving about | Manufacturing robots, warehouse automation |  |
| **Rational agent** - selects actions expected to maximize performance measure given percept sequence and built-in knowledge | Chess-playing program that evaluates moves based on win probability |  |
| **Bounded rationality** - decision-makers face information processing and temporal constraints on deliberation | Educational administrators with limited time to review student data |  |
| **Satisficing** - making decisions that are "good enough" rather than optimal (Herbert Simon, 1978 Nobel Prize) | Choosing a restaurant that meets basic criteria rather than exhaustively comparing all options |  |
| **Perfect rationality** - always taking the exactly optimal action; not feasible in complex environments | Theoretical ideal that cannot be achieved in practice due to computational limits |  |
| **Value alignment problem** - ensuring AI systems pursue goals aligned with human values | King Midas problem: getting exactly what you asked for with unintended consequences |  |
| **Agent** - anything that perceives its environment through sensors and acts through actuators | Thermostat, self-driving car, software bot |  |
| **Percept** - content an agent's sensors are perceiving at a given moment | Camera image, temperature reading, stock price |  |
| **Percept sequence** - complete history of everything the agent has ever perceived | All sensor readings from initial state to current time |  |
| **Agent function** - mapping from percept sequences to actions | Function that determines what action to take given sensory input |  |
| **Agent program** - implementation of the agent function | Actual code running on physical architecture |  |
| **Agent = architecture + program** - AI agent consists of hardware/software platform plus decision-making code | Robot = physical body/sensors + control software |  |
| **Consequentialism** - evaluating agent behavior by its consequences | Judging a medical AI by patient outcomes, not by its decision process |  |
| **Performance measure** - evaluates any given sequence of environment states to capture desirability | Points scored in a game, customer satisfaction ratings |  |
| **Rationality depends on four things**: performance measure, prior knowledge, available actions, percept sequence to date | Taxi driver deciding route based on traffic knowledge, GPS data, and time constraints |  |
| **Omniscience vs. rationality** - omniscient agent knows actual outcomes; rational agent maximizes expected performance | You can make a rational decision to carry an umbrella even if it doesn't rain |  |
| **Autonomy** - relying on own percepts and learning rather than designer's prior knowledge | Self-driving car learning from experience vs. following pre-programmed rules |  |
| **PEAS description** - Performance, Environment, Actuators, Sensors framework for task environments | Automated taxi: Performance=safety/speed, Environment=roads/traffic, Actuators=steering/brakes, Sensors=cameras/GPS |  |
| **Fully observable** - sensors give access to complete environment state at each point in time | Chess game where both players see the entire board |  |
| **Partially observable** - sensors don't detect all relevant aspects | Poker game where you can't see opponent's cards |  |
| **Single-agent** - agent solving a problem by itself | Solving a crossword puzzle alone |  |
| **Multiagent** - multiple entities must be viewed as agents | Chess game (competitive), autonomous vehicles sharing road (cooperative/competitive) |  |
| **Deterministic** - next state completely determined by current state and action | Solving 8-puzzle where moves have predictable effects |  |
| **Nondeterministic** - next state not completely determined; may list possibilities without probabilities | Weather affecting taxi journey: "there's a chance of rain tomorrow" |  |
| **Stochastic** - explicitly deals with probabilities for nondeterministic outcomes | "There's a 25% chance of rain tomorrow" |  |
| **Episodic** - agent's experience divided into atomic episodes; next episode doesn't depend on previous actions | Image classification tasks where each image is independent |  |
| **Sequential** - current decisions affect future choices | Chess, medical diagnosis where each step affects later options |  |
| **Static** - environment doesn't change while agent deliberates | Crossword puzzle remains unchanged while you think |  |
| **Dynamic** - environment changes during deliberation; not deciding counts as deciding to do nothing | Real-time strategy game, stock trading |  |
| **Discrete** - finite number of distinct states, percepts, and actions | Chess with finite board positions and legal moves |  |
| **Continuous** - values sweep through continuous ranges smoothly over time | Taxi driving with continuous speed and position values |  |
| **Known environment** - agent knows the "laws of physics" governing the environment | Playing a video game where you know all the rules |  |
| **Unknown environment** - agent doesn't know how the environment works | New video game where you don't know what buttons do until you try them |  |
| **Simple reflex agents** - select actions based on current percept, ignoring history | Thermostat turning on heat when temperature drops below threshold |  |
| **Model-based reflex agents** - maintain internal state tracking unobserved aspects of world | Self-driving car tracking positions of other vehicles even when temporarily out of view |  |
| **Transition model** - knowledge about how the world changes over time (effects of actions and independent changes) | Physics simulation predicting object movement |  |
| **Goal-based agents** - use goal information describing desirable situations to guide action selection | GPS navigation system finding route to destination |  |
| **Utility-based agents** - use utility function to measure desirability of states and maximize expected utility | Investment algorithm balancing risk and return |  |
| **Utility function** - internalization of the performance measure; ranks states by desirability | Happiness scale, monetary value calculation |  |
| **Expected utility** - utility the agent expects to derive on average given probabilities and utilities of outcomes | Choosing medical treatment based on probability of success × quality of outcome |  |
| **Model-free agent** - learns what action is best without learning how actions change environment | Reinforcement learning agent that learns "go left works well here" without understanding why |  |
| **Learning agent components**: learning element (makes improvements), performance element (selects actions), critic (feedback on performance), problem generator (suggests exploratory actions) | AlphaGo: performance element plays moves, learning element updates strategy, critic evaluates positions, problem generator tries new opening strategies |  |
| **Atomic representation** - each state is indivisible with no internal structure | Search problems where states are just labels (A, B, C) |  |
| **Factored representation** - state split into fixed set of variables/attributes with values | Planning with variables like location=home, time=morning, weather=sunny |  |
| **Structured representation** - world has things/objects related to each other | Relational databases, first-order logic describing relationships between entities |  |
| **Distributed representation** - concepts mapped across multiple memory locations | Neural networks where information is spread across many neurons |  |

---

## Chapter 2: Intelligent Agents (Extended Concepts)

### Key Terms
Agent, environment, sensor, actuator, percept, action, agent function, agent program, rationality, performance measure, environment type, reflex agent, model-based agent, goal-based agent, utility-based agent, learning agent

---

### Chapter 2 Detailed Annotations

| Concept/Definition | Example | Personal Reflection |
|-------------------|---------|---------------------|
| **Agent analysis tool** - "agent" is a tool for analyzing systems, not an absolute characterization dividing world into agents and non-agents | Same system might be analyzed as single agent or collection of sub-agents depending on purpose |  |
| **King Midas problem** - putting the wrong purpose into a machine; getting exactly what you specified with unintended consequences | Midas asked that everything he touched turn to gold, then regretted it when food, drink, and family turned to gold |  |
| **Four determinants of rationality**: (1) performance measure defining success, (2) agent's prior knowledge, (3) available actions, (4) percept sequence to date | Rational taxi behavior depends on safety metrics, traffic knowledge, steering/braking capabilities, and current sensor data |  |
| **Rationality maximizes expected performance; perfection maximizes actual performance** - can't predict future perfectly, so rationality is about making best decision given available information | Rationally choosing umbrella based on weather forecast even if it doesn't rain |  |
| **Information gathering** - rational agents gather information to improve future decisions | Exploration in unknown environments before exploitation |  |
| **Learning requirement** - rational agents learn from percepts rather than relying solely on prior knowledge | Robot improving navigation through experience |  |
| **Lack of autonomy** - extent to which agent relies on designer's knowledge rather than own learning | Hardcoded chess program vs. self-learning chess AI |  |
| **Task environments** - the "problems" to which rational agents are the "solutions" | Driving task environment includes roads, traffic, weather, other drivers |  |

---

## Chapter 3: Solving Problems by Searching

### Key Terms
Problem-solving agent, search problem, state space, initial state, goal state, actions, transition model, action cost, optimal solution, path cost, abstraction, search algorithm, search tree, frontier, best-first search, evaluation function, completeness, cost optimality, time complexity, space complexity, breadth-first search, uniform-cost search, depth-first search, depth-limited search, iterative deepening search, bidirectional search, informed search, heuristic function, greedy best-first search, A* search, admissible heuristic, consistent heuristic, weighted A* search, beam search, IDA*, RBFS, SMA*, effective branching factor, relaxed problem, pattern database, landmarks, differential heuristic, metalevel state space

---

### Chapter 3 Detailed Annotations

| Concept/Definition | Example | Personal Reflection |
|-------------------|---------|---------------------|
| **Problem-solving agents** - use atomic representations where states have no internal structure | Route-finding, puzzle-solving where states are treated as indivisible units |  |
| **Planning agents** - use factored or structured representations of states | Robots planning actions considering object locations and relationships |  |
| **Episodic, single agent, fully observable, deterministic, static, discrete, and known environments** - simplest environments for Chapter 3 | 8-puzzle, route-finding on known map |  |
| **Informed vs. uninformed algorithms** - informed can estimate distance to goal; uninformed cannot | A* search (informed using heuristic) vs. breadth-first search (uninformed) |  |
| **Four-phase problem-solving process**: (1) Goal formulation, (2) Problem formulation, (3) Search, (4) Execution | Robot deciding to go to kitchen (goal), planning route (formulation), finding path (search), following path (execution) |  |
| **Open-loop system** - fixed sequence of actions in fully observable, deterministic, known environment | Pre-programmed assembly line robot |  |
| **Closed-loop system** - monitors percepts to handle model errors or nondeterminism | Self-driving car adjusting to unexpected obstacles |  |
| **Search problem formal definition**: state space, initial state, goal states, available actions, transition model, action cost function | 8-puzzle: states are board configurations, initial is starting position, goal is solved position, actions are tile moves, each move costs 1 |  |
| **Optimal solution** - has lowest path cost among all solutions | Shortest route between two cities |  |
| **Abstraction level** - abstract states correspond to sets of detailed world states | "In Arad" abstracts over exact GPS coordinates |  |
| **Standardized problem** - illustrates or exercises problem-solving methods | 8-puzzle, traveling salesperson problem |  |
| **Real-world problem** - solutions people actually use with idiosyncratic formulation | Specific robot navigation with unique sensors |  |
| **Grid world** - agent navigates rectangular grid, perhaps with obstacles | Warehouse robot pathfinding |  |
| **Sokoban puzzle** - pushing boxes to storage locations on grid | Classic planning puzzle requiring look-ahead |  |
| **Knuth's problem** - illustrates infinite state spaces | Using arithmetic operations to reach target number |  |
| **Traveling salesperson problem (TSP)** - visiting every city exactly once with minimum total distance | Delivery route optimization |  |
| **VLSI layout problem** - positioning millions of components and connections on chip | Chip design optimization for area, delay, yield |  |
| **State space** - (possibly infinite) set of states in the world and transitions between them | All possible board configurations in chess |  |
| **Search tree** - describes paths between states, reaching towards goal; may have multiple paths to same state | Tree of possible move sequences exploring game positions |  |
| **Frontier** - separates interior region (expanded states) from exterior region (unreached states) | Nodes waiting to be explored in search |  |
| **Best-first search** - choose node with minimum value of evaluation function f(n) | A* selecting lowest f(n) = g(n) + h(n) |  |
| **Node data structure**: STATE, PARENT, ACTION, PATH-COST (or g(node)) | Search tree node storing state reached, how we got there, and cost so far |  |
| **Queue types**: priority queue (best-first), FIFO queue (breadth-first), LIFO queue/stack (depth-first) | Different search strategies use different frontier organization |  |
| **Reached states** - lookup table (hash table) storing states already encountered | Preventing redundant exploration |  |
| **Cycle** - special case of redundant path where path loops back to earlier state | A→B→C→B creates a cycle |  |
| **Three approaches to redundant paths**: (1) remember all reached states, (2) don't worry about it, (3) check for cycles only | Trade-off between memory usage and efficiency |  |
| **Completeness** - algorithm guaranteed to find solution when one exists and report failure when none exists | Ensures algorithm won't get stuck or give wrong answer |  |
| **Cost optimality** - finds solution with lowest path cost (also called admissibility) | Guaranteed to find best solution, not just any solution |  |
| **Time complexity** - measured by number of states and actions considered or seconds taken | How long algorithm takes to run |  |
| **Space complexity** - memory needed to perform search | Critical for large problems that might exhaust memory |  |
| **Complexity measures**: \|V\| (vertices/nodes), \|E\| (edges/actions), d (depth of optimal solution), m (maximum depth), b (branching factor) | For implicit state spaces, complexity in terms of d, m, b |  |
| **Breadth-first search** - expands shallowest nodes first; complete even on infinite spaces; finds minimum-action solutions | Uses FIFO queue; explores level by level |  |
| **Early goal test** - check if node is solution when generated | Breadth-first can use this; faster than late goal test |  |
| **Late goal test** - check if node is solution when popped from queue | Best-first search typically uses this |  |
| **Exponential complexity problem** - cannot be solved by uninformed search except for smallest instances | Memory requirements grow exponentially with depth |  |
| **Dijkstra's algorithm / Uniform-cost search** - best-first search where f(n) = path cost from root; finds cheapest path | Expands lowest-cost nodes first; optimal for varying action costs |  |
| **Complexity of uniform-cost**: O(b^(1+⌊C*/ε⌋)) where C* is optimal cost, ε is minimum action cost | Can explore many low-cost actions before useful high-cost action |  |
| **Depth-first search** - expands deepest node first; usually implemented as tree-like search without reached table | Uses LIFO/stack; memory-efficient but incomplete in infinite/cyclic spaces |  |
| **Depth-first incompleteness** - can get stuck in infinite path even without cycles | Not systematic in infinite state spaces |  |
| **Backtracking search** - variant of depth-first using even less memory by modifying current state directly | Only stores one state and action path; O(m) memory vs O(bm) |  |
| **Depth-limited search** - depth-first with depth limit l; incomplete if l chosen poorly | Prevents infinite descent but may miss solutions beyond limit |  |
| **Iterative deepening search** - tries depth limits 0, 1, 2,... until solution found | Combines benefits of depth-first and breadth-first; preferred for large unknown-depth spaces |  |
| **Iterative deepening efficiency** - re-generating upper levels doesn't matter when most nodes are at bottom level | O(bd) time complexity when solution exists |  |
| **Bidirectional search** - searches forward from initial state and backward from goal, hoping to meet in middle | O(2 × b^(d/2)) complexity; requires backward reasoning ability |  |
| **Informed search strategy** - uses domain-specific hints about goal location via heuristic function | More efficient than uninformed search when good heuristics available |  |
| **Heuristic function h(n)** - estimated cost of cheapest path from node n to goal state | Straight-line distance for route-finding |  |
| **Greedy best-first search** - expands node with lowest h(n); appears closest to goal | Fast but not optimal; complete in finite spaces |  |
| **A* search** - best-first with f(n) = g(n) + h(n); estimated cost of best path through n | Combines actual cost so far with estimated remaining cost |  |
| **Admissible heuristic** - never overestimates cost to reach goal; h(n) ≤ h*(n) where h* is true cost | Required for A* cost optimality; straight-line distance is admissible |  |
| **Consistent heuristic** - h(n) ≤ c(n,a,n') + h(n') for all nodes and successors; triangle inequality | Stronger than admissibility; ensures f(n) is non-decreasing along paths |  |
| **A* with inadmissible heuristic** - may or may not be cost-optimal; can work if only overestimates slightly | Sometimes acceptable for speed gains |  |
| **Monotonic costs** - path costs always increase (or stay same) as you extend path | g costs are monotonic since action costs are positive |  |
| **Optimal efficiency of A*** - any algorithm using same heuristic must expand all nodes A* surely expands | A* is optimally efficient for tree search with consistent heuristic |  |
| **Pruning** - eliminating possibilities from consideration without examining them | Critical AI concept; A* prunes unnecessary search tree nodes |  |
| **Satisficing solutions** - "good enough" solutions that are suboptimal but faster to find | Accept somewhat worse solution to save time/space |  |
| **Weighted A* search** - uses f(n) = g(n) + W × h(n) where W > 1; inadmissible but faster | Focuses more on heuristic (greedy-like) while considering path cost |  |
| **Bounded suboptimal search** - guarantees solution within constant factor W of optimal | Solution cost ≤ W × C* |  |
| **Bounded-cost search** - finds solution with cost less than constant C | Accept any solution below cost threshold |  |
| **Unbounded-cost search** - accept any cost as long as solution found quickly | Pure speed optimization |  |
| **Speedy search** - unbounded-cost algorithm expanding node minimizing h(n)/(1 + g(n)) | Balances proximity to goal with cost spent |  |
| **Beam search** - limits frontier to k best nodes; incomplete and suboptimal but memory-efficient | Discards all but k best-scoring nodes |  |
| **Iterative-deepening A* (IDA*)** - A* benefits without storing all reached states; visits some states multiple times | Like iterative deepening but uses f-cost limits instead of depth limits |  |
| **Recursive best-first search (RBFS)** - mimics best-first using only linear space | More efficient than IDA* but still regenerates nodes |  |
| **Memory-bounded A* (MA*) and Simplified MA* (SMA*)** - uses all available memory efficiently | Expands best leaf, deletes worst leaf when memory full |  |
| **SMA* subtlety** - expands newest best leaf, deletes oldest worst leaf when all equal f-values | Avoids deleting just-expanded node |  |
| **Memory limitations make problems intractable** - forced to switch among candidate paths when all can't fit | Time complexity suffers from memory constraints |  |
| **Bidirectional heuristic search** - considers pairs of nodes (one from each frontier) that are surely expanded | More complex than unidirectional; uses lb(m,n) < C* criterion |  |
| **f2(n) = max(2g(n), g(n) + h(n))** - evaluation function for bidirectional best-first search | Mimics lower-bound criteria for bidirectional efficiency |  |
| **Front-to-end search** - hF estimates distance to goal; hB estimates distance to start | Traditional bidirectional approach |  |
| **Front-to-front search** - estimates distance to other frontier | Alternative bidirectional strategy |  |
| **8-puzzle**: 9!/2 = 181,400 reachable states; needs good heuristic for efficiency | Manageable size; can keep all in memory |  |
| **15-puzzle**: 16!/2 > 10 trillion states; requires excellent heuristic | Too large for exhaustive search |  |
| **h1 (misplaced tiles)** - counts tiles out of position; admissible heuristic | Each misplaced tile needs ≥1 move |  |
| **h2 (Manhattan distance)** - sum of distances of tiles from goal positions; admissible | Sum of horizontal + vertical distances |  |
| **Effective branching factor b*** - branching factor of uniform tree with N+1 nodes at depth d | Characterizes heuristic quality: closer to 1 is better |  |
| **Korf & Reid reduction**: A* with heuristic h reduces effective depth by constant kh | Search cost O(b^(d-kh)) vs O(bd) for uninformed |  |
| **Dominance**: h2 dominates h1 if h2(n) ≥ h1(n) for all n | h2 always better or equal to h1; never expands more nodes |  |
| **Relaxed problem** - problem with fewer restrictions on actions | Easier to solve; optimal cost is admissible heuristic for original |  |
| **Relaxed problem adds edges** - creates shortcuts in state-space graph | Optimal solution in original is also solution in relaxed |  |
| **Consistency of relaxed heuristic** - derived from exact cost in relaxed problem, obeys triangle inequality | Automatically consistent |  |
| **ABSOLVER** - program generating heuristics automatically from problem definitions | Generated new heuristics for 8-puzzle and Rubik's Cube |  |
| **Subproblem heuristic** - exact solution cost for subset of problem | Pattern database approach |  |
| **Pattern databases** - precomputed exact solution costs for all subproblem instances | Amortized over many searches after one-time precomputation |  |
| **Perfect heuristic via precomputation** - store optimal cost between every vertex pair; O(\|V\|²) space, O(\|E\|³) time | Practical for ~10K vertices, not 10M |  |
| **Landmark points** - chosen vertices for efficient distance estimation | 10-20 landmarks enable fast heuristic calculation |  |
| **Inadmissible landmark heuristic**: hL(n) = min over landmarks of (C*(n,L) + C*(L,goal)) | Efficient but may overestimate |  |
| **Differential heuristic**: hDH(n) = max over landmarks of \|C*(n,L) - C*(goal,L)\| | Admissible and efficient; subtracts landmark-to-goal from node-to-landmark |  |
| **Shortcuts** - artificial edges defining optimal multi-action paths | Speed up route-finding algorithms |  |
| **Greedy landmark selection** - pick random first landmark, then repeatedly add point maximizing distance to nearest landmark | Spreads landmarks out effectively |  |
| **Metalevel state space** - learning how to search better by reasoning about search process itself | AI learning to improve its own search strategies |  |
| **Features for learning** - state properties relevant to predicting heuristic value | Better than raw state description for machine learning |  |
| **Benchmarking** - running algorithms and measuring actual seconds and bytes used | Empirical performance comparison |  |
| **Mathematical algorithm analysis** - abstract complexity analysis independent of implementation | Theoretical performance characterization |  |
| **Input parameter n** - characterizes input size for complexity analysis | Number of items to sort, graph size, etc. |  |
| **Abstract operation count** - reflects running time without compiler/computer specifics | Steps, comparisons, or other implementation-independent measure |  |
| **Worst case Tworst(n)** - maximum time over all inputs of size n | Upper bound on performance |  |
| **Average case Tavg(n)** - expected time over input distribution | More representative of typical performance |  |
| **Big-O notation**: T(n) is O(f(n)) if T(n) ≤ kf(n) for some k, for all n > n0 | Asymptotic upper bound; hides constant factors |  |
| **Asymptotic analysis** - ignoring constant factors and small values of n | Most widely used algorithm analysis tool |  |
| **Complexity analysis** - analyzes problems rather than algorithms | Characterizes inherent problem difficulty |  |
| **P (polynomial problems)** - solvable in time O(nk) for some k | Tractable problems |  |
| **NP (nondeterministic polynomial)** - verifiable in polynomial time with lucky guesses | Can verify solution quickly but finding it may be hard |  |
| **P ≠ NP conjecture** - most believe P ≠ NP but never proven | Central unsolved problem in computer science |  |
| **NP-complete** - hardest problems in NP; if any solved in polynomial time, all NP problems can be | Traveling salesperson, satisfiability |  |
| **NP-hard** - at least as hard as NP-complete; solving one solves all NP problems | May not be in NP themselves |  |
| **co-NP** - complement of NP with yes/no answers reversed | Proving something is NOT a solution |  |
| **co-NP-complete** - hardest problems in co-NP | Likely not in P |  |
| **#P (sharp-P / number-P)** - counting problems corresponding to NP decision problems | Count number of solutions, not just yes/no |  |

---

## Historical Notes & Milestones

### Notable Figures & Contributions

| Person/Event | Contribution | Significance |
|-------------|--------------|--------------|
| **Aristotle (384-322 BCE)** | First precise laws governing rational thought | Foundation of logical reasoning |
| **Ramon Llull (c. 1232-1315)** | Ars Magna - mechanical reasoning system using paper wheels | Early attempt at mechanizing thought |
| **René Descartes (1596-1650)** | Clear discussion of mind-matter distinction; dualism | Philosophy of mind foundations |
| **Gottfried Leibniz (1646-1716)** | Built mechanical device for operations on concepts | Early computing device |
| **David Hume (1711-1776)** | Principle of induction | Learning from experience |
| **George Boole** | Formal logic development | Mathematical logic foundation |
| **Gottlob Frege (1848-1925)** | Extended Boolean logic to first-order logic with objects and relations | Modern logic system |
| **Alan Turing** | Built Heath Robinson (1943) for decoding; defined computability | Computing and AI foundations |
| **Konrad Zuse** | Z-3 (1941) - first operational programmable computer | Computing hardware |
| **John von Neumann** | Decision theory, utility theory | Rational decision-making framework |
| **Herbert Simon (1916-2001)** | Satisficing, bounded rationality (1978 Nobel Prize in Economics) | Realistic decision-making models |
| **Warren McCulloch & Walter Pitts (1943)** | First work recognized as AI - neural network models | Neural computation foundations |
| **Marvin Minsky & Dean Edmonds (1950)** | Built first neural network computer | Early AI hardware |
| **John McCarthy (1955)** | Organized Dartmouth conference; created Lisp (1958) | Founded AI field; key programming language |
| **Allen Newell & Herbert Simon** | Logic Theorist (1956), General Problem Solver | Early AI programs, Physical Symbol System Hypothesis |
| **Arthur Samuel** | Checkers program using reinforcement learning (1950s) | Machine learning pioneer |
| **Frank Rosenblatt (1962)** | Perceptrons | Neural network development |
| **Ed Feigenbaum, Bruce Buchanan, Joshua Lederberg** | DENDRAL program - early expert system | Applied AI to scientific problems |
| **Judea Pearl (1988)** | Probabilistic Reasoning in Intelligent Systems (2011 Turing Award) | Uncertainty in AI |
| **Yoshua Bengio, Geoffrey Hinton, Yann LeCun (2019 Turing Award)** | Deep learning development | Modern AI revolution |
| **IBM Watson (2011)** | Won Jeopardy! against human champions | Public AI perception milestone |

### AI Development Phases

| Phase | Characteristics | Key Developments |
|-------|----------------|------------------|
| **Early Enthusiasm (1943-1966)** | High expectations, simple programs | Logic Theorist, GPS, DENDRAL, Lisp |
| **Dose of Reality (1966-1973)** | Recognition of limitations; Lighthill Report; "AI winter" | Combinatorial explosion problems, weak methods |
| **Knowledge-Based Systems (1969-1986)** | Expert systems, domain knowledge | R1, Fifth Generation project, back-propagation rediscovery |
| **Return to Foundations (1987-present)** | Embrace probability, statistics; big data; neural networks | HMMs, deep learning, Watson, probabilistic reasoning |

---

## End of Document

**Note**: The third column ("Personal Reflection") is left blank for you to add your own notes, connections to your coursework, questions, or insights as you study.
