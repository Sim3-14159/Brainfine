<img width="150" height="150" align="left" style="float: left; margin: 0 10px 0 0;" alt="Brainfine logo" src="Images/logo.png"> 

<img alt="Brainfine title" src="Images/title.svg">
<br><br>

Brainfine is a highly human readable programming language with ABC-like syntax, that compiles to Brainf***.
<br><br><br>

> [!NOTE]
> Brainfine is still being built, so these instructions may not work yet.


## Installation

You can go to the [releases](https://github.com/Sim3-14159/Brainfine/releases/latest) page and download a binary for your system. 

If you want to compile from scratch, you need to have have [Unicon](https://github.com/uniconproject/unicon) installed on your system. Clone this repository then run `make` in the project root:
```bash
git clone https://github.com/Sim3-14159/Brainfine && cd Brainfine
make
```

You can optionally also install Brainfine system-wide:
```bash
sudo make install
```

You should then have an executable called *brainfine*.

## Syntax
There are 11 different statements in Brainfine (all case insensitive). "{ }" in the code means some value, "( )" means optional, and "*" means 1 or more times.
| Statement | Action |
|--|--|
| `OUTPUT {x}*` | Outputs the value(s) `x` to the console |
| `INPUT {x} (TYPE {type})` | Reads user input and sets `x` to it, optionally changing `x`s type to `type`
| `SET {x} (TYPE {type}) TO {value}` | Set the variable `x` to `value`, optionally changing `x`s type to `type` |
| `REPLACE {x} WITH {y}` | Anywhere `x` appears in the source file will be replaced with `y`
| `TASK {x} (WITH {y}*) DOES {statements} END` | Define a task named `x` that runs `statements` and optionally has argument(s) `y` |
| `RUN {x} (WITH {y}*)` | Run a task `x`, optionally with arguments `y` |
| `PASTE {filename}` | Replace this line with the contents of the file `filename` |
| `QUIT {s}` | Exit the program with status `s` |
| `FOR {v} IN {a} DO {statements} END` | Run `statements`, setting `v` to the next element in a list `a` every time |
| <code>IF {e} THEN {statements<sub>1</sub>} (OTHERWISE {statements<sub>2</sub>}) END</code> | If the boolean value `e` is true, run <code>statements<sub>1</sub></code>, otherwise run <code>statements<sub>2</sub></code> (if there is an "OTHERWISE" clause) |
| `WHILE {e} DO {statements} END` | While the boolean value `e` is true, run `statements` |

This is a Hello World program in Brainfine:
```js
OUTPUT "Hello, World!"
```

## Usage

Once you have made a Brainfine program with the extention *.bfn*, you can run `brainfine [filename].bfn` or just `brainfine [filename]` to compile it. It will output to the file *[filename].bf* by default, or you can choose an output file like `brainfine [filename] [output]`. 

You can then run the output file with a Brainf*** interpreter like [Beef](https://github.com/andreabolognani/beef).


## License
This project uses an [MIT License](https://opensource.org/license/MIT), so you can use, modify, or share this project however you like!
