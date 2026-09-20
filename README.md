# Maze Solver (BFS)

A command-driven maze solver built from scratch in Python, using a self-implemented
dynamic array (`Vector`) and FIFO queue (`Queue`) — no built-in `list`, `set`,
`collections.deque`, `queue.Queue`, or `heapq` used as the core data structures.

## How to run

`commands.txt` contains one command per line. Comments start with `#`. See
`commands.txt` in this repo for a full working example.

## Commands supported

`LOAD_MAZE <path>`, `PRINT_MAZE`, `SOLVE`, `PRINT_PATH`, `CLEAR`, `QUIT`

Unknown commands print `ERROR: UNKNOWN_COMMAND` and are otherwise skipped.

## Design

**`Vector`** (`vector.py`) — a fixed-size Python list used purely as raw storage
(`[None] * capacity`), with manual index tracking (`_size`, `_capacity`). When full,
`push()` allocates a new buffer at double the capacity and manually copies existing
elements across index by index — no `list.append()` or slicing used for the growth
logic itself.

**`Queue`** (`queue.py`) — a circular-array FIFO built on the same fixed-size
buffer technique as `Vector`. `front`/`rear` pointers wrap around using modulo
(`% capacity`). `enqueue()` raises on a full queue rather than silently overwriting
data; `dequeue()` raises on an empty queue. When used for BFS, capacity is sized as
`rows * cols`, so it never fills up in practice.

**Grid representation** (`maze_reader.py`) — the maze is stored as a `Vector` of
`Vector`s: one inner Vector per row, each holding individual characters. Adjacency
is computed implicitly via `get_neighbors(grid, row, col)`, which returns the up to
4 in-bounds, non-wall neighbors of a cell — no explicit graph object is built.

**BFS** (`solve_maze` in `maze_reader.py`) — standard breadth-first search from `S`,
using the `Queue` above for traversal order (guaranteeing shortest path), a `dict`
for `visited` lookups, and a second `dict` for parent-pointer tracking
(`parent[cell] = came_from`). On dequeuing `G`, the path is reconstructed by walking
`parent` backwards from `G` to `S`, then reversed into a `Vector` in S→G order.
`dict` is used only for lookup/bookkeeping purposes, per the assignment's allowance —
it is never used as the primary traversal structure (that role belongs to `Queue`).

**`CLEAR` policy** — resets both the loaded maze and the last computed path back to
"nothing loaded" (`None`), printing `CLEARED`. Any subsequent `PRINT_MAZE`, `SOLVE`,
or `PRINT_PATH` after `CLEAR` behaves exactly as if no maze had ever been loaded.

## Test files

- `Mazes/maze1.txt` — solvable maze, expected `length=4`
- `Mazes/maze2.txt` — unsolvable maze (walled off), expected `UNSOLVABLE`
- `Mazes/badmaze.txt` — malformed maze file, expected `ERROR: INVALID_MAZE`

## Known limitations

- Command parsing does not currently support quoted-string arguments containing
  spaces (e.g. a maze path with a space in it).
- `queue.py` shares its name with Python's standard-library `queue` module; this
  has not caused conflicts in testing, but a rename (e.g. `my_queue.py`) would be
  safer in a larger project.