# Notes for 9.26.2018
# Git to track and share versions
## Using Git to work with others
Cecile --git push--> GitHub
Claudia <--git pull or git clone-- GitHub
Use git merge to merge changes (if happened ~same time w/ Cecile & Claudia)

Created CompToolsCourseNotes repository on GitHub
added repository to CourseNotes

### Vocab:
[git clone] <- clone smth on github when have nothing on local
[git pull] <- already have version on local, want to pull & merge updates w/ gi$
[git remote add] <- already have git repository, add it to github repo
fetch = gets new updates & stores them in temp staged place to see if dif b/w c$

### Fun fact:
_When collaborating, pull often b/c changes made often_
- [git pull origin master] <- pulls updates from github repo & merges to local
- commit changes before pulling or else git will stop pull update

### Resolving conflicts and merge commits
Cecile and volunteer change zmays file at same time
Cecile made new commit w/out pulling to see if changes
Cecile tries to push & gets error b/c "remote (git) contains work you don't hav$
Cecile tries to git pull & gets error b/c git can't merge two files worked on a$
git status says she has "unmerged paths" and to "[git pull] to merge the remote$
Cecile merges the readme files herself
[git add]
[git commit]
^like normal

[git pull origin master] *origin master added for comfort b/c could be on other$
- though origin master is default

Then Cecile checks that push w/ [git log --abbrev-commit --pretty=oneline --gra$
- shows graph of how commits happened & who did the commits
Lastly Cecile [git push] to put merged file to github

I did [git pull origin master], then [git log --graph]
- updated my local repo and saw graph of commits made

[git merge --abort] <- cancels a merge (if overwhelmed)
