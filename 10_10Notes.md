# Notes for 10.10.2018 Class

### [ Comments made before class }
### grade 2 other students' Hw1.3
- If have question about grades, talk to Cecile
- If script grading is from Linux, install GNU tools (already done this?),
-- then replace `grep` by `ggrep` and `sed` by `gsed`
- Run script, grade what the rubric says to
*Fun fact*: get visual studio code (Cecile uses it in class, mixes code and commandline)

## continuation from Cecile's last GitHub notes
### some other git subcommands
`git stash` <- saves changes w/out commiting them & not on Git history
`git checkout -b <mybranch>` <- creates new branch & switch to it
`git stash pop` <- gets changes back onto new branch you're on ^

## awk, parameter expansion, wget, & curl

## quick test processing: `awk`
- *language* for quick text-processing tasks on tablular data
`bioawk` for biological formats
`awk pattern { action } <filename>
- pattern is like `grep` and `sed` patterns
- `/pattern/` ex. `/^chr\d/`
`~` <- match
`!~` <- no match
`&&` <- "and"
`||` <- "or"
`|` <- "or" also, but used when the `|` is within anotehr line
- ex. `awk '/chr2|chr3/' [etc.]` versus `awk 'chr2 || chr3' [etc.]`
variables defined in `awk` ex. `$0`=whole line, `$1`=first field, etc. (-F creates field (like -d for `cut`))
can introduce new variables & don't use `$` to call the variable
- to use shell variables, such as:
--threshold=18
--echo $threshold
--`awk '$3 - $2 > $threshold <filename> (doesn't work)
-- awk -v t=$threshold '$3 - $2 > t' <filename> (works)
--- works b/c only awk touching the t=threshold (not the shell)
--if the `awk statement` is *true*, print the match found
--if the `awk statement` is *false*, prints the line

`awk 'BEGIN{ s = 0 }; { s += ($3-$2) }; END{ print "mean: " s/NR };'`
- calculates 3rd field - 2nd field, add that to variable `s`
- echos "mean: and the average of s/total # of lines read" (gives mean)
- `NR` would only include all lines that were read (so whole file, not just the matches)
- thus, gives average of column3 - column1

`awk 'NR >= 3 && NR <= 5' example.bed`
- current # of records, `NR`, is greater than/equal to 3
- current # of records, `NR`, is less than/equal to 5
- *didn't get this...*

rest of examples show you can pipe commands w/ `awk`
& that big commands should be split up w/ `;` and hard returns

`awk '/Lypla1/ { feature[$3] += 1 };
    END { for (k in feature)
    print k "\t" feature[k] }' Mus_musculus.GRCm38.75_chr1.gtf  | column -t`
- `feature[$3]` <- `feature`=variable w/ array that is a list of values,
-- can get to 1st value with `[#1]`, above ex grabs 3rd value in that variable
- gives 3rd column in `feature` "list"
- the array goes through elements in the 3rd column & counts how many times comes across that element
- ex.) gene was found 3 times; thus `feature[3]`=3 for "gene", etc.
- `k in feature` will loop over the keys (k could be any letter, just k here)

There are functions w/in `awk` language:
-- listed in Cecile's GitHub notes
*we'll have to use `awk` in a hw assignment*

## parameter expansion:
`${variable_name extra stuff}`
- can take substrings (ex. below)
`echo "substrings of parameter values: ${i:1} and ${var:4:5}" # :offset:length`
`%` <- will strip the shortest occurence
`%%` <- strips the longest occurence
`#` <- strips shortest occurence from beginning
`##` <- strips longest occurence from beginning

`echo "substitute: ${var/cool/hot}"`
- substitutes coolname for hotname
> substitute: hotname.txt.pdf.md

`echo "delete:     ${var/cool}"`
deletes cool in coolname
> delete: var=coolname.txt.pdf.md
^these are useful, too

## getting data from the web: wget and curl
`wget` <- not avail default on Mac, get using Homebrew (did this)

ex.) get files from web (instead of downloading each all 15 files, use `wget`
mkdir lizard; cd lizard
- Made dir for lizard data ('>')~ "ssss"
wget http://datadryad.org/resource/doi:10.5061/dryad.mm11q # gives link to data files
- go to that link & download everything from there (this is dangerous!!!)
ls # new file: dryad.mm11q
- check out that new downloaded info, bro
grep "fasta" dryad.mm11q
- look for fasta files within downloaded data (mm11q format)
grep ".txt" dryad.mm11q
-- look for .txt files within downloaded data (mm11q format)
grep "fasta" dryad.mm11q | wc # 6 fasta files
- found 6 fasta files 
- output was: >        6      24     622
wget -r -l 1 -nd --accept-regex '\.fasta|\.txt' http://datadryad.org/resource/doi:10.5061/dryad.mm11q
- only accept files that match that regular expression
-- in ex: find files that match .fasta and .txt files
- output was (once opened dir w/ `ls`):
cten_16s.fasta?sequence=1           cten_nd2.fasta?sequence=1
cten_BACH1.fasta?sequence=1         females_all_meristic.txt?sequence=1
cten_GAPD.fasta?sequence=1          females_all_morph.txt?sequence=1
cten_NTF3.fasta?sequence=1          male_all_meristic.txt?sequence=1
cten_PRLR.fasta?sequence=1          male_all_morph.txt?sequence=1 
(used rm to get rid of `dryad.mm11q`, `dryad.mm11q.1`, & `robots.txt`)

can add options to `wget`:
- `--limit-rate=50k` (limits rate at which you download)
- `-w 1` (waits 1sec b/w file downloads)

`curl`
- writes to std output
