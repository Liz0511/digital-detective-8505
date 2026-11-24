# Mission 2 - Become comfortable with the Terminal

## 1. Task / objective
The aim of this mission was to practise basic Terminal commands and learn how to create, copy, rename and view files.

## 2. Work completed

### Task 2.1 - Basic commands

| Operation | Command | What it does |
|---|---|---|
| Show current folder | `pwd` | Shows where I am currently working |
| List files | `ls` | Shows files and folders |
| Detailed list | `ls -l` | Shows more details about files |
| Go to parent folder | `cd ..` | Moves one folder back |
| Create folder | `mkdir practice` | Creates a folder |
| Create file | `touch notes.txt` | Creates an empty file |
| Copy file | `cp notes.txt copy.txt` | Makes another copy |
| Rename file | `mv copy.txt new-copy.txt` | Changes the file name |
| View file | `cat notes.txt` | Displays the file content |

**What I observed:** [Run these commands in your repository and write what happened.]

### Task 2.2 - File practice

These are the commands to practise inside the repository:

```bash
mkdir terminal-practice
cd terminal-practice
echo "This is my first line." > notes.txt
echo "This is my second line." >> notes.txt
cat notes.txt
cp notes.txt backup.txt
mv backup.txt renamed-backup.txt
ls -l
```

The `>` symbol writes content into a file. The `>>` symbol adds content at the end. Copying makes another file, but moving or renaming changes the location or name of the original file.

### Task 2.3 - Flags and pipes

```bash
ls
ls -lah
ls -lah | head
```

I learned that flags change how a command works. For example, `-l` shows detailed information, `-a` includes hidden files and `-h` makes file sizes easier to read.

The pipe symbol `|` sends the output of one command to another command. Here, `head` displays only the first few lines.

### Task 2.4 - Package managers

Homebrew is a package manager used on macOS. If it is already installed, I can check it using:

```bash
brew --version
brew list
```

A package manager helps us install and update software. It also helps manage the other files or tools that a program needs. I did not install or remove anything for this task.

## 3. Commands / tools used
`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `echo`, `head` and, if installed, `brew`.

## 4. My understanding
Earlier I mostly used folders through the file manager. Now I understand that we can do the same kind of work using Terminal commands. The current folder is important because commands work based on where we are.

## 5. Difficulties faced
[Write the actual command or step that confused you. If none, write "No major difficulties".]

## 6. How I resolved them
[Write what helped you solve it, or write "Not applicable".]

## 7. Evidence / files
- `terminal-practice/notes.txt`
- `terminal-practice/renamed-backup.txt`
- [Add a safe screenshot if available.]

## 8. Commit details
Commit message: `Complete Terminal and file management mission`

Commit and push status: [Update after doing it.]
