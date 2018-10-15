# 10.15.2018 In-Class Notes
## before class notes:
Hw for W (10.17): Install python (using Python 3!)

-------------------------------------------------
## connecting to remote machines to run long jobs
-------------------------------------------------
## connecting to remote machines: ssh, scp
`ssh` <- Secure SHell
ex.) `ssh loginname@MachineToConnectTo` it'll ask if you're sure if 1st time, type `yes`
best to ask `hostname` to see what you're called on that machine
`ssh` will create directory called .ssh (hidden file b/c of `,`)
.ssh will store info: known_hosts
looks like using your laptop, but actually using other machines
**should not open new window to edit files!!!**
**you're on another comp & it's not safe!!!**
Instead, use `nano -nw <file.md>`
`-nw` <- doesn't open new window

### To avoid typing your password each time: 
Copy the public key from your laptop (in id_rsa.pub)
 to the file ~/.ssh/authorized_keys on the remote server. 
You created a key pair earlier for github,
 and copied your public key to your github profile.

`scp` <- Secure copy, over a network
using scp requires copying from a <pathname> to a dif <pathname>
ex.) `scp -p <username@MachineName>:<pathnameFrom> <pathnameTo>`
Note: need to provide username, machine name & full path on the remote machine.
`-p` <- Preserves timestamp from when files created, not when transferred
`scp` can go from server to remote & vice versa

### Dif b/w `cp` and `scp`
`cp -r log/ target/path/` <- copies content of log/ directory
`cp -r log target/path/` <- copies directory itself *and* its content
*the / is important here!*
`scp` doesn't have this / difference


## long-running jobs: nohup
`tail -f screenlog` <- prints last few outputs on terminal window
`^C` to stop that^
Closing/Stopping the terminal will hangup the server process
-if want server to keep running, to catch & ignore hang-up signal:
`nohup mb mrBayes-run.nex > screenlog &`
`nohup` = catch & ignore hang-up signal
`mb` = run mb program (like bash)
`mrBayes-run.nex` = program in mb
`>` = divert results to...
`<screenlog>` = name of output file
`&` = I'll give you more questions, hang with me
`ps -u <username>` = see what is running on server

## tmux: terminal multiplexer
`tmux` = terminal multiplexer
- sessions can be **detached** and **reattached**: detach, logout,log backin, re-attach
- can have multiple windows in one session
- you have to be organized with tmux if running multiple sessions
`^ad` to detach

### tmux windows and panes
great information here once have example
- without example it's tough to learn
- this notes section includes tmux keys and their respective actions
`^a |` or `^a -` = splits window into panes vertically or horizontally
- these shortcuts depend on configuration of `tmux`
-- notes have site to switch configuration to match notes' configs

### long jobs on stat.wisc.edu machines
*Only for stats servers*
smthn smthn


## running many jobs
Several resources on campus if have big job or tons of small jobs
High performance: big job, requires lots of memory (Use ACI)
High throughput: many small/short jobs (<24hr) (Use CHTC with HTCondor for job scheduling

*Consider if your "high performance" job can be broken down to be a "high throughput" job*
