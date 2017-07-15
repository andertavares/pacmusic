# PacMusic
Implicit coordination for music generation

A PacMan-like world, where walking generates music.

# Requirements
- Python 2.7

# Usage
First, clone or download the project into a directory of your choice. Then go to that directory via the command line.

run: `main.py -w input -n trials --max-steps steps -o output_dir [additional parameters]`, where the parameters are:
- input: path to the input file which contains the basic block with the musical notes
- trials: the number of trials (repetitions) of an experiment (default=100)
- steps: the number of steps (moves) per trial (default=120)
- output_dir: a directory to generate the output files (default: data)

Additional parameters are:
- -m {astar,random,randombiased}, --method {astar,random,randombiased}: Method used by PacMan to move (default = AStar)
- -r TARGET_RADIUS, --target-radius TARGET_RADIUS:  Maximum distance from player (in each axis) that a new target appears (default=7)
- -t MAX_TARGETS, --max-targets MAX_TARGETS: Maximum number of simultaneous targets (default=3)
- -h, --help: show a help message and exit

After running, you'll see a bunch of .log files in the directory specified as output. Each has a line with the form:
`row, col, note`

Where `row` and `col` are the visited coordinates and `note` is the musical note that the agent stepped in. 

