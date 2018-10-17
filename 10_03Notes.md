# more shell with 'if', script arguments, arithmetic

## script arguments
write bash if running a script, but if forget have your script say #!/bin/bash

## safe script options, file permissions
always start script with:
- #!/bin/bash
- `set -e` # script terminates if any command exits with non-zero status
- `set -u` # terminates if any variable is unset
- `set -o pipefail` # terminates if command within a pipes exits unsuccessfully

could always write `bash <scriptname> <filename>`
- instead of always writing bash, could write `!/bin/bash`

Tried to run: `./headtail.sh`
Output: `-bash: ./headtail.sh: Permission denied`
- to give yourself *permission* to run `./headtail.sh`:
- `ls -l`
- `chmod u+x headtail.sh`
- then can use script in current directory
- `./headtail.sh <filename> | column -t

### Fun facts:
* u, g, o: user, group, other; a for all
* + or - to add or remove permissions
* r, w, x: read, write, execute

## ~/bin directory
put programs here b/c easy to call the programs from anywhere
*tried to add headtail.sh to my path and that failed...*
*can't call it from anywhere with this issue*

## arithmetic expansion
shell isn't used for complicated math (use R or python for that)
`((i+=1))` <- incremented i by 1; same as `((i++1))
`echo $((i++))`
`echo $i` <- i++ executes the command and increments i after
`echo $((++i))`
`echo $i` <  ++i increments i first, then executes the command
^ these could be useful in for loops

## if statements and checks
need something that returns true or false
`-lt` <- "is less than"
ex.)

`if [ $i -lt 800 ] # the spaces after `[` and before `]` are REQUIRED
then
  echo "i is less than 800"
else
  echo "i is not less than 800"
fi`

### notation:
`$#` <- "number of arguments"
`-o` <- "or"
`-a` <- "and" (creates a circuit, if have $1 -a $2, if $1 is false, then $2 is automatically false)
`!` <- "is not"
`-f` <- "file"
`$1` <- "first argument"
`-r` <- "readable"
`-lt` <- "less than"
`-le` <- "less than or equal to"
`-gt` <- "greater than
more notations on Cecile's git notes
exit code: 0 if successful, 1 if unsuccessful (for the shell, 0=true, 1=false!!)
*order is important!*
