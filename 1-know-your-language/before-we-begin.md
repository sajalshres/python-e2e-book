# Before We Begin

Before we begin, lets address some of the skills that all developers need regardless of their specialization.

- Version Control - Git or SVN
- Basic Terminal
- How the Web works

## Version Control - Git

Version control is a system that keeps track of changes to a file or group of files over time. When you have a history of these changes, it lets you find specific versions later, compare changes between versions, recover files you may have deleted, or revert files to previous versions.

Git and SVN both are feasible for various workflows and version control systems, But since Git is more popular, it seems like a no-brainer for us.

### Three sections of a Git Project

A conventional Git project will have three main sections:

1. #### Git directory

   Located in project-path/.git/ is where Git stores everything to tack in-and-outs of project including metadata, object databases, versions of project files.

2. #### Working directory (or tree)

   It is the place where a user makes local changes to project. This directory pulls the project files from Git directory's object database and place them on the working directory.

3. #### Staging area

   Sometimes also called as index, stage, or cache, this is a file that stores information about what will go into your upcoming commit. A commit tells Git to save the stage changes.

   Git will take a snapshot of the files and permanently tore them in the Git directory.

Each file in a Git project will maintain following states:

1. Committed
2. Modified
3. Staged

### Configure your Git Environment

git config command will allow us to customize your Git environment. Configuration is stored at three levels:

1. System
2. User
3. Project

### Initialize Repositories

`$ git clone` : Make existing directory into a Git project

`$ git clone [URL or SSH]` : Clone or download a repository that already existing in a remote location.

### Branches

Any commits you make will be made on the branch you’re currently “checked out” to.

`$ git status` : Check status of your local changes and branch

`$ git branch [branch-name]` : Create new branch `branch-name`

`$ git checkout [branch-name]` : Switch to a `branch-name` and update working directory.

`$ git merge [branch-name]` : Combine `branch-name` history into current branch. This is usually done in pull requests.

`$ git branch -d [branch-name]` : Delete the `branch-name` branch

### Making Changes

`$ git add [file..s]` : Stage (Snapshots) the changed files.

`$ git commit -m "[message]"` : Take a snapshot of staged files.

`$ git log` : Lists version history for the current branch

`$ git log --follow [file]` : Lists version history for a file, including renames

`$ git diff [source-branch] [target-branch]` : Shows content differences between two branches

`$ git show [commit]` : Outputs metadata and content changes of the specified commit

### Synchronize your Changes

`$ git fetch` : Get history from the remote branches

`$ git merge` : Combines remote tracking branches into current local branch

`$ git push` : Uploads all local branch commits to remote repository

`$ git pull` :  Updates your current local working branch with all new commits from the corresponding remote branch. (Combination of `git fetch` and `git merge`)

### Mistakes - That's Nice

`$ git reset [commit]` : Undoes all commits after `[commit]`, preserving changes locally

`$ git reset --hard [commit]` : Discards all history and changes back to the specified commit

> *Warning:* Changing history can have have hazardous effect.

### Authenticate with SSH

1. #### Check for existing SSH Key

   1. Check that there are no `rsa` files here before continuing

      `$ ls -al ~/.ssh`

   2. Create `.ssh` directory if it doesn't exists

      `$ mkdir $HOME/.ssh`

2. #### Generate a new SSH Key

   `$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`

3. #### Add SSH Key to `ssh-agent`

   `$ eval $(ssh-agent -s)`

   `$ ssh-add ~/.ssh/id_rsa`

4. #### Add RSA Key to remote system

   1. Copy the RSA Key to clipboard
   2. Paste it to remote system

## Basic Terminal

## How the Web works

