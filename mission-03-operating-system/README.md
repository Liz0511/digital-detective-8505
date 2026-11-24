# Mission 3 - Understand the operating system

## 1. Task / objective
This mission is about understanding the operating system, running processes, storage, file paths and permissions.

## 2. Work completed

### Task 3.1 - System information

I will use these commands to check my Mac:

| Information | Command | What it shows |
|---|---|---|
| macOS version | `sw_vers` | Shows the macOS version |
| Current account | `whoami` | Shows the logged-in account |
| Storage | `df -h` | Shows used and available storage |
| System activity | `top -l 1` | Shows a snapshot of running processes |

**My observations:** [Run the commands and write a short summary. Do not publish your username or private details.]

### Task 3.2 - Processes

A process is a program that is currently running. For example, when I open a browser, it runs as a process.

PID means Process ID. It is a number used by the operating system to identify a running process.

Two examples I may find are:
- Browser process
- Text editor process

**My actual examples:** [Check your process list and add two that you can see.]

### Task 3.3 - Paths and permissions

An absolute path gives the full location of a file. A relative path gives the location based on the folder I am currently in.

Example relative path: `mission-03-operating-system/README.md`

My absolute path: [Get it using `pwd`, but remove your personal username before adding it here.]

| Permission | Meaning |
|---|---|
| `r` | Read the file |
| `w` | Make changes to the file |
| `x` | Execute a file or access a directory |

I can use `ls -l` to view file permissions.

### Task 3.4 - Operating system responsibilities

| Responsibility | What it means | Example |
|---|---|---|
| Process management | Manages running programs | Running browser and VS Code together |
| Memory management | Manages RAM used by programs | Giving memory to an application |
| Device management | Helps software communicate with hardware | Connecting a printer |
| File management | Organises files and folders | Saving a document |
| User interface / shell | Lets us interact with the computer | Desktop and Terminal |
| Security and permissions | Controls who can access files | File access permissions |

## 3. Commands / tools used
- `sw_vers` - checks macOS version.
- `whoami` - checks the current account.
- `df -h` - checks storage.
- `top -l 1` - shows system activity.
- `pwd` - shows the current path.
- `ls -l` - shows file details and permissions.

## 4. My understanding
I understood that the operating system manages the computer and helps applications work properly. It handles memory, files, devices and running programs. A process is simply a program that is running at that time.

## 5. Difficulties faced
[Write what you actually found difficult, or write "No major difficulties".]

## 6. How I resolved them
[Write how you solved it, or write "Not applicable".]

## 7. Evidence / files
- System information notes in this README.
- [Add a screenshot after hiding personal information.]

## 8. Commit details
Commit message: `Document operating system and file management`

Commit and push status: [Update after doing it.]
