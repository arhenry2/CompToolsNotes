# In-Class Notes for 1 Oct 2018
-------------------------------

## Hw 1 Exercise 2 Review:
Comments in scripts:
- head -n2 file | tail -n1 | cut c18
-- # get hmax <- all comment that's needed for this line
- grep "hmax = \d" 
-- # assumes h </= 9
- variables <- have comment that explains short variable names (comment for humans)
- what to document in readme file: 
-- this is explained in first readme file (go to commits on GitHub and click on <> for cecile's first commit of that file

## In-Class Work:
### more shell tools, sed

cut:
`less -S <filename>`
- lets you see all file more organized if lines are long
`cut -f#` takes only the # column from a datafile; `f` = "field" = column of data
`-d` changes the delimiter b/w columns fields (instead of tab)
`-c#` cuts the # character, instead of column, from datafile
Skipped lecture-examples example; do this later for extra practice
- used grep '_' combined.nex | cut -f1 -d ' ' | less
-- used less to check that it works, then change `less` to `> taxa`
-- delimiter changed to a space

sort:
`-k` sorts by specific columns (keys)
- ex.) `-k2,2` sorts by keys in columns 2 to 2
- add `n` to sort 2nd column numerically
- add `r` to sort 2nd column in reverse order
`-c` checks if sorted already
`-t,` to change separator to a comma instead of tab
exercise to extract feature of gene in a file:
`grep "ENSMUSG00000033793" Mus_musculus.GRCm38.75_chr1.gtf | less -S | cut -f 3 | sort | uniq -c`

column:
`column` formats table data to be human readable
`-s"," sets separator to comma instead of tab

basename & dirname:
extract file/folder name and its path from a string
`pwd`
`basename $(pwd)`
`dirname $(pwd)`

stream editor: sed:
*most imp use is to substitute things
`sed s/pattern/replacement/ filename > newfile`
- never send this to a current file!!!
sooo many options on her website
- `s/pattern/replacement/g` replace in all instances
- `s///gi` case-insensitive search *(/// = /pattern/replacement/)*
- `s///p` print to screen if match, don't print to output
- uses similar notations as `grep`

example

echo "chr12:74-431" | sed -E 's/^(chr[^:]+):([0-9]+)-([0-9]+)/\1\t\2\t\3/'
> chr12t74t431

echo "chr12:74-431" | gsed -E 's/^(chr[^:]+):([0-9]+)-([0-9]+)/\1\t\2\t\3/'
> chr12 74      431
*use `gsed` to utilize GNU sed to make more human-readable*

echo "chr12:74-431" | sed -E 's/^(chr[^:]+):([0-9]+)-([0-9]+)/\1\ \2\ \3/'
> chr12 74 431

*without gsed, replace `t` with ` ` (a space); achieve same as `gsed`
