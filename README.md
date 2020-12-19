# EAI320_Practical1
## Implemented by Lefa Raleting
# EAI 320 - Intelligent Systems, University of Pretoria
## Practical Assignment 1: depth-first search (DFS) and breadth-first search (BFS).
## Compiled by Llewellyn Strydom
## Revised by Michael Teles

# Scenario

**Rock-paper-scissors (RPS)** is a popular game played between two adversaries, where each
adversary simultaneously forms one of three shapes with an outstretched hand [3], or using
some other representation. Throughout this course, the framework provided by [4] will be
used to teach students how different **artificial intelligence (AI)** principles and algorithms can
be applied to the game of RPS.
The RPS terminology that will be used in this course is shown below.

**Object:** One of three hand shapes (viz. rock (R), paper (P), or scissors (S)).
Move: One game where each opponent plays an object, resulting in a win, loss or draw for
each player. The RPS framework used for this practical assignment [4] refers to a move
as a round.

**Match:** A series of moves between two players to decide the overall winner of the game.

**Sequence:** A particular order of objects for one opponent (e.g. rock, rock, scissors).
This assignment will task students with using two common search strategies to find a hidden
sequence that will allow it to exploit an opponent’s weaknesses during a match of RPS.

# Instructions
For this practical assignment, students will investigate the effectiveness of two uninformed
search techniques, namely depth-first search (DFS) and breadth-first search (BFS). The
algorithms will be used to explore different possible sequences in a game of RPS.

The four major goals for this practical are thus
1. Implementing a search tree structure in Python

2. Implementing a DFS and BFS algorithm

3. Implementing a RPS agent that can beat breakable.py

## Task 1
A search tree structure should be created in Python that can be used by any type of search
algorithm. For this task the depth of the search tree must be dynamic and should only be
limited by memory constraints.

Any process or method may be used to create the search tree. The recommended approach
is to use a Python Class to represent nodes in a tree. Each of the nodes are linked and a
recursive function can be used to build the tree.

An example code segment to create a tree class is provided in Listing 1, and a tree can be
constructed using the code in Listing 2, resulting in the node tree shown in Figure 1.
1) Suggestion: A depth parameter may be passed to the constructor of the tree to allow
the tree up to be constructed to the specified depth.

## Task 2
The next task is to write BFS and DFS algorithms that can be used to incrementally search
the tree built in Task 1. Each search algorithm must return a complete list of the sequences
represented by each node, in the order in which they are visited by the algorithm

## Task 3

For this task, the code from Tasks 1 and 2 will be used to determine the objects that
will be played against an agent called breakable.py. This agent is programmed to play
randomly without ever repeating an object, until a certain sequence of objects, called the
break sequence, is played. The break sequence will be unknown and will have a length
between 2 and 5, inclusive. Once the break sequence is played, the agent breakable.py will
repeat its last move an unknown number of times, before it starts playing randomly again.
While the agent is repeating itself, it is possible to exploit it and win every move until the
agent starts playing randomly again. At this stage, the known break sequence is simply played
again to cause the agent to repeat its objects again.
In summary, the tree should be traversed using BFS and DFS respectively, until the break
sequence is found. Once the break sequence is known, it can be used to defeat the agent.

1. Suggestions: The primary goal of this assignment is that the specified search algorithms
should be implemented. As a result, other approaches to solving the problem are not acceptable
(e.g. playing randomly until a repeat is detected). Furthermore, the properties of the various
search algorithms should be compared, so modifications to the search algorithms should not
be implemented as such modifications may obscure the properties of the search algorithms
(e.g. storing the previous five objects played to avoid the need for further search after the
accidental breaks described in the next paragraph).

It is possible to accidentally stumble upon the break sequence before reaching the correct
node in the tree. For example, steps 3 and 4 in Table I could trigger the break sequence
SR, even though the current sequence being tested is RR. If this occurs, the assumed break
sequence will not work consistently, and searching of the tree should be resumed.
The BFS and DFS can be implemented recursively or iteratively, but it is strongly
recommended that your implementation is iterative.
Implementing the entire search process before the first match takes place is not recommended
as some of the aspects of the various search algorithms will be not be clearly seen
by this approach.
If one implements this task successfully, one should expect to win 100% of the games
against the agent breakable.py, but it is possible that this may not occur. Can you explain
why?


### A . Code Instructions 
Each student is required to submit code conforming to the requirements listed below. A
mark of zero will be awarded if the submitted code file does not run, produces errors, or does
not follow the instructions.
* The submission must be a single file.
* Submitted code will be evaluated using the command
    rpsrunner.py <your_filename>.py breakable.py
to ensure that the agent breakable.py is successfully beaten.
* All submissions must be written using Python 3 as a result of the fact that rpsrunner.py
is written in Python 3.
* The code submitted must be the final implementation of Task 3.
* The first line of the code must declare a variable bfs_dfs to select between the BFS
( bfs_dfs = 0) and DFS algorithms ( bfs_dfs = 1).
* Append the output of your program as a comment to the end of your file.
