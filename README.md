# PacMusic
Implicit coordination for music generation

A PacMan-like world, where walking generates music.

# Requirements
- Python 2.7

# Usage
## Generating data
First, clone or download the project into a directory of your choice. Then go to that directory via the command line.

run: `./main.py -w input -n trials --max-steps steps -o output_dir [additional parameters]`, where the parameters are:
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

## Analysing data
PacMusic (or other implicit coordination environments) generate files with sequences of coordinates and musical notes played, on a format like:
```
5, 5, C
4, 4, E
3, 4, G
2, 4, B
1, 5, D
```
This kind of file can be analysed with: 
`python analysis.py file1 file2 ...`

Then, it outputs statistics about the file. For the example given, the output is:
```
File: arpeggios.log
Sequence of notes: 
['C', 'E', 'G', 'B', 'D']

Number of moves: 4
 
Arpeggios: 
        CEG Occurrences:  1
        EGB Occurrences:  1
        GBD Occurrences:  1
Total arpeggios: 3

Total power chords: 0
----------------------
Done
```

(in that case, the file was `named arpeggios.log`)
