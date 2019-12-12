# Configure Git
##### Set User Config
`git config --global user.name "username"`\
`git config --global user.email "email"`

##### See User Config
`git config --list`

##### See commands
`git config --help`

# Setting Up for the first time
There can be 3 scenarios
### 1. Clone remote to local
##### Clone to local
`git clone <url or a repo on local> <where to clone>`

##### See Details of Cloned Repo
+ Repo Details
`git remote -v`

+ Branch Details
`git branch -a`

### 2. Clone local to remote
+ First make sure everything is comitted in local repo
+ Switch to your repository's directory\
`cd /path/to/your/repo`

+ Connect to your remote repository\
`git remote add origin https://github.com/waqar-ahmed-malik/gitConcepts.git`

+ Push the local repo to the remote repo\
`git push -u origin master`

### 3. Initialize a local folder as a repo
`git init`

# Work on local repository.
### Monitoring Changes
`git status`\
It will list out the files in the directory which are not being tracked. Before comitting always use this.

### Ignore a file while pushing to the repo.
+ Create a `.gitignore` file using `touch .gitignore`.\
write Readme.txt to skip `Readme.txt`  or we can use wildcards like `*.txt` to skip all text files or we can write `\directory` to skip a directory.
We should always sync .gitignore file to global repo as this makes git to always know which 
file to ignore.
 
### Staging Area
Organise files which have been changed to review.
##### Add all files to staging area.
`git add -A`
##### Add single file to staging area.
`git add filename.extension`
##### Remove all files from staging area.
`git reset`
##### Remove single file from staging area.
`git reset filename.extension`

### commit the changes from staging area to local repo
`git commit -m "message"`

### check logs
See author name who made the commit and the message with it.
`git log`


### Push to the remote repository
##### First Pull the latest one from the remote repository.
`git pull origin master`

##### Push to the remote repository
`git push origin master`


# Common Workflow
1. Create a dev branch
2. Checkout the dev branch
3. Made some changes to the code.
4. Check status of dev branch as it should show the changes made.
5. Add changes to staging area
6. Commit all the changes to dev branch.
7. Associate the local branch to the dev branch(-u syntax will do it after creating a dev branch on remote repo 
   if it doesn'y exist) on remote repo.
8. After running tests on dev remote repo Checkout local master.
9. Pull remote master.
10. Merge local dev to local master.
11. Push to remote master.
**We should not work on the Master Branch. Create a branch for a particular feature and then work on it.**

### Create a new branch
`git branch branch_name`
### list all the available branches.
`git branch`
### to select a branch to work with.
`git checkout branch_name`
### add to staging area.
`git add -A`
### commit to selected branch.
`git commit -m "message"`\
**In the above process local master branch remains unaffected.**

### Push branch to remote repository from this side branch.
`git push -u origin branch_name`\
**It will associate the local side branch to remote side branch so when in in future we do  `git pull` or `git push` then git will know that these local and remote branches are associated with each other. The `-u` flag will create the branch at remote repo if it doesn't exist.**
**This remote side branch will be used for testing before merging to Master branch.**

### After testing with the side branch, merge it with master
##### selects local Master branch
`git checkout master`
##### pull remote master branch and see if someone else has made changes to it.
`git pull origin master`
##### merge side branch to master branch locally as we are in master branch.
`git merge branch_name`
##### list out the branches merged.
`git branch --merged`
##### push from local to remote
`git push origin master`

### Delete the Side branch
##### From Local
`git branch -d branch_name`
##### From Remote
`git push origin --delete branch_name`


# Deinitialize a local repo to stop tracking changes
`rm -rf .git`
