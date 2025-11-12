# Noah's helpers

This is the simulator for [COMS 4444, F25 project 4](https://www.cs.columbia.edu/~kar/4444f25/node21.html)

### CLI Arguments

The simulation can be configured using a variety of command-line arguments.

#### General Options

| Argument     | Default       | Description                                                                                                                                     |
| :----------- | :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| `--gui`      | `False`       | Launches the graphical user interface to visualize the simulation. If omitted, the simulation runs in the command line and outputs a JSON blob. |
| `-T`         | `Noe default` | Sets the total number of turns to run the simulation for.                                                                                       |
| `--map_path` | `No default`  | Specify num_helpers, animal populations and Ark position in a json file. Must be under `maps/`.                                                 |
| `--player`   | `r`           | Specify the player to run, either `r` for random or `1-10` for a group.                                                                         |
| `--ark`      | `No default`  | Specify the ark position as two numbers in the form of `X Y`.                                                                                   |
| `--seed`     | `No default`  | Provides a seed for the random number generator to ensure reproducible simulations.                                                             |
