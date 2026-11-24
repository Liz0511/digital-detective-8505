# Mission 6 - Git and GitHub

## 1. Task / objective
This mission is about learning how Git works, making commits, creating a branch and opening a Pull Request on GitHub.

## 2. Work completed

### Task 6.1 - Basic Git commands

| Operation | Command | What it does |
|---|---|---|
| Check status | `git status` | Shows which files have changes |
| Stage changes | `git add README.md` | Selects a file for the next commit |
| Commit | `git commit -m "message"` | Saves the staged changes in Git history |
| View history | `git log --oneline` | Shows previous commits |

Staging means selecting the changes that I want to save. Committing means saving those selected changes in the Git history.

### Task 6.2 - Create a branch

The branch name required in the assignment is `update-about`.

```bash
git switch -c update-about
```

After creating the branch, I need to add a section called **My Learning** to the main README. I can write two or three things I have learned so far.

Then I can save and push the branch:

```bash
git status
git add README.md
git commit -m "Add my learning section"
git push -u origin update-about
```

**Branch link:** [Add after pushing.]

### Task 6.3 - Pull Request

After pushing the branch, I need to open GitHub and create a Pull Request from `update-about` into `main`.

A branch is a separate place to work on changes without directly changing the main branch. A Pull Request is used to ask for those changes to be reviewed and merged.

- Pull Request link: [Add after creating it.]
- Status: [Open / Merged]
- Merge: [Only if your instructor asks you to.]

### Task 6.4 - Git command glossary

| Command | Meaning |
|---|---|
| `git init` | Starts a Git repository |
| `git status` | Checks the current changes |
| `git add` | Stages files |
| `git commit` | Saves staged changes |
| `git log` | Shows commit history |
| `git branch` | Lists or creates branches |
| `git switch` | Changes the current branch |
| `git push` | Sends commits to GitHub |
| `git pull` | Gets the latest remote changes |

## 3. Commands / tools used
`git status`, `git add`, `git commit`, `git log`, `git branch`, `git switch`, `git push` and `git pull`.

## 4. My understanding
Git helps us keep track of changes in a project. GitHub lets us store the repository online. Branches and Pull Requests are useful when working on changes because we can review them before adding them to the main project.

## 5. Difficulties faced
I initially found Git branches and Pull Requests confusing, but I understood them after practising.

