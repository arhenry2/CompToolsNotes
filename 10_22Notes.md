# In-Class Notes from 10.22.2018 ###

## Intro to Python review:
python is 0-indexed (weird for us unless we're comp peeps)

### Basic Types
`int` = integer, must be a positive whole number
*64 bits: 1(sign) + 63: coded as power of 2, so from 0 to 2^63-1 for positives, from -1 to -2^63 for negatives*
`float` = number that can be decimal
*32 bits: 1 (sign) + 8 (exponent) + 23 (mantissa = fraction)*
*64 bits: 1 (sign) + 11 (exponent) + 52 (mantissa = fraction)*
Note: Your VisualStudioCode uses 64-bit
`bool` = True or False (0=F, 1=T); takes 1 bit (b/c only 0 or 1)
**Important to know for `if` statements**

`1.0/3.0 == 1.0 - 2.0/3.0` <- should be true, but Python returns F b/c of how floats are calculated
-convert to `boolian` by:
bool(1.0/3.0 == -(1.0 - 2.0/3.0)) <- returns 

input: `"%s %s hello %s" % (5,5.8,"5")`
output: `'5 5.8 hello 5'`

`%s` = string
`%` <- take those numbers to put in the string defined by `""`

### How to Store multiple elements
type([10,20]) <- returns `list` (can change lists(mutable))
type((20,30)) <- returns `tuple` (can't change tuples(immutable))
**Note:** A list of lists is not an array

### On SWC Site: Storing Multiple Values in Lists
Create a list with hard brackets
If have a list of names, misspell a name, can select that "object" in the list & only change that
However, this doesn't work on one name, b/c not a list

**Note:**
- modifiable data is **mutable**
- unmodifiable data is **immutable**

#### Making copies and changes, from Cecile's notes on GitHub??
`a = [10,11]`
`b = a`
`print("b[1]=", b[1])` #changes the value b binds to, so changes a too
`b[1] = 22`
`print("b =", b, "\nand a =", a)`
- output: `b= [10,22] and a=[10,22]`
- if you "copy" a into b, then changes made to b and a
- `deepcopy` <- copy everything contained in what's being copied
- if change your deepcopy, will not change what was copied

**This is confusing, go over again**

def add1_scalar(x):
    """adds 1 t scalar input"""
    x += 1
    print("after add1_scalar:",x)


Lots of notes left on Python Notes...
Review GitHub notes from Cecile, was a mess in class
