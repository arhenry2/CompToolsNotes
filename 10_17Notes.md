# Class Notes for 10.17.2018
## intro to python
### basic programming concepts, not much about python itself
### basic python interpreter, *not* the notebook
could access python by:
- typing `python`
-- `quit()` to get out of python
- `touch myscript.py` <- create script to put python code only (no output)
-- `nano myscript.py`
--- get Visual Studio Code to get color-coded python style
-- in VS Code, click on square thing in rightside column to get python extensions
- use jupyter notebook `jupyter notebook`
- also use jupyterlab package to have more features
- fun fact: jupyter stands for **Ju**lia **Pyt**hon and **R**

### Installed Visual Studio Code
- had to create (`nano`) a script **w/ `.py` as the extension This is essential!!!**
- opened this in VS Code
- opened *python terminal* in VS Code by `Shift-Command-p` (assumed Shell; lower panel)
- had to type `python` to get terminal to read python
- then could type Shift-Enter to run the python commands (upper panel)

### Software Carpentry Workshop:
#### Using Variables in Python
With python, each command is read on it's own:
- saving a variable
- using with w/ another variable
- changing 1st variable
- 2nd variable stays the same b/c it's value w/ 1st variable wasn't updated

#### Loading Data into Python
`import numpy` <- package to help read csv files (good for "scientific computing with Python")
`numpy.loadtxt(fname='<filename>',delimiter=',')` <- loads file via numpy, delimiter shows it's a csv file
`data=numpy.loadtxt(fname='<filename>',delimiter=',')` <- assigns data to variable `data`
Note: **Array indices: [row,column]**, used: `data[30,20]` for row 30, column 20
- Python starts array w/ row 0 and column 0 (unlike R & Matlab that starts w/ 1 for both)

#### Slicing Data
(TBC)
