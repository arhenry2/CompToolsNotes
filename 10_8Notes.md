# Notes from 10.8.2018
======================

## git to check old versions, branch & merge parallel versions, sha

### checking out older versions
recover old versions of readme files by:
- `git pull`
`git log --abbrev-commit --pretty=oneline`
`git checkout <commit code (in yellow)> readme.md` <- see past readme file from that commit
`git checkout master` <- gets you back to original readme
*base repository* = repository with only the .git file

### branches
good to switch back & forth b/w dif versions
`git branch readme-changes` <- created branch called readme-changes
`git branch` <- lists existing branches
`git checkout <branch name>` <- changes branch
`git branch -d <branch name>` <- deletes <branch name>
`git push -u origin <branch name>` <- pushes branch & what's on branch onto GitHub
once on one branch, can see changes only made on that branch 
- had wowza.md file I made in quercus, didn't have adapter.fa made in master)

### collaborating on parallel branches & merging branches
`git merge quercus` <- while on master branch, merges quercus branch items to master branch items
- this pops up with nano to say what merges you made (like a commit)
`git log --abbrev-commit --pretty=oneline --graph --branches -n6` <- see that you merged branches
`git push master` <- pushes merged branches to current branch on GitHub
- will merge other branch to the branch you're on!!!
*Find out: dif b/w `git fetch` and `git pull`

### some other git subcommands
`git revert` <- revert changes (creates new commit)

### SHA checksums
SHA = security hash algorithm; used my GitHub to guard against data corruption

1 byte = 8 bits
1 nibble = 4 bits 
0000 = 0
0001 = 1
0010 = 2
...
1111 = 15
4*4=16 options if a nibble

`echo "this sentence is super cool" | shasum
> 93aff6c8139fff6855797afc8ea7a7513ffabb6f  -
echo "this sentence is duper cool" | shasum
> 97c250becdaa49c62721478c7f82d116e1039e0e`

^ A ###### small dif in the sentence is a HUGE dif in sum of the file (shasum)

