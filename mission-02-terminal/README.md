# Mission 2 – Become Comfortable with the Terminal

## 1. Task Completed

In this mission, I practised using Terminal and learned how to work with files and folders using commands.

## 2. Work Completed

### Task 2.1 – Basic Commands

I practised some basic Terminal commands.

| Operation | Command | What it does |
|---|---|---|
| Show current location | `pwd` | Shows the current folder |
| List files | `ls` | Shows files and folders |
| Detailed list | `ls -l` | Shows file details |
| Go back one folder | `cd ..` | Moves to the parent folder |
| Create folder | `mkdir practice` | Creates a new folder |
| Create file | `touch notes.txt` | Creates an empty file |
| Copy file | `cp notes.txt copy.txt` | Creates a copy |
| Rename file | `mv copy.txt new-copy.txt` | Changes the file name |
| View file | `cat notes.txt` | Shows the file content |

### Task 2.2 – File Practice

I used the following commands to practise creating and copying files.

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

After running these commands, I could create a folder, add text to a file, view its content, copy it and rename the copied file.

I also learned that `>` replaces the existing content, while `>>` adds new content at the end.

### Task 2.3 – Flags and Pipes

I tried these commands:

```bash
ls
ls -lah
ls -lah | head
```

I learned that flags give extra information when using commands. For example, `-l` shows details, `-a` shows hidden files and `-h` makes file sizes easier to understand.

The pipe symbol `|` sends the output of one command to another. In this example, `head` shows the first few lines.

### Task 2.4 – Package Managers

I learned about Homebrew, which is a package manager for macOS.

I used these commands to check it:

```bash
brew --version
brew list
```

A package manager helps us install and manage software on a computer.

## 3. Commands / Tools Used

I used Terminal and practised these commands:

`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `echo`, `head` and Homebrew commands.

##4. Difficulty Faced

At first, I was confused about the difference between copying and renaming a file. After practising the cp and mv commands, I understood how they work.
