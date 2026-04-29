# 🐧 Ubuntu Terminal & POSIX Workflow Cheat Sheet

**Objective:** A comprehensive reference guide for navigating, managing, and developing within Ubuntu Linux environments, including GitHub Codespaces and local virtual machines.

---

## 📂 1. Navigation & Directory Control
The core commands for moving around the file system.

| Command | Example Usage | Description |
| :--- | :--- | :--- |
| `pwd` | `pwd` | **Print Working Directory:** Outputs your current exact folder path. |
| `ls` | `ls -la` | **List:** Shows files in the current directory. `-l` shows detailed info, `-a` shows hidden files. |
| `cd` | `cd /var/www/` | **Change Directory:** Moves you into the specified folder. |
| `cd ..` | `cd ..` | Moves you exactly one folder level up. |
| `cd ~` | `cd ~` | Moves you directly to your user's home directory. |
| `mkdir` | `mkdir src` | **Make Directory:** Creates a new folder. Use `-p` to create nested folders (`mkdir -p src/main/java`). |
| `rmdir` | `rmdir old_folder` | **Remove Directory:** Deletes a folder (only works if the folder is empty). |

---

## 📄 2. File Management
Commands for creating, moving, and deleting files.

| Command | Example Usage | Description |
| :--- | :--- | :--- |
| `touch` | `touch index.py` | Creates a new, empty file, or updates the timestamp of an existing one. |
| `cp` | `cp file.txt copy.txt` | **Copy:** Duplicates a file. Use `cp -r` to copy an entire directory recursively. |
| `mv` | `mv old.txt new.txt` | **Move/Rename:** Moves a file to a new location or renames it. |
| `rm` | `rm config.json` | **Remove:** Deletes a file permanently. |
| `rm -rf` | `rm -rf ./build/` | **Force Remove:** Deletes a directory and all its contents recursively. *(Use with extreme caution!)* |
| `ln -s` | `ln -s target link` | **Symlink:** Creates a shortcut/symbolic link to another file or directory. |

---

## 🔍 3. File Inspection & Editing
Tools to view and edit file contents without a graphical interface.

| Command | Example Usage | Description |
| :--- | :--- | :--- |
| `cat` | `cat logs.txt` | **Concatenate:** Prints the entire contents of a file to the terminal screen at once. |
| `less` | `less config.yaml` | Opens a file in a scrollable pager. (Press `q` to quit, `/` to search). |
| `head` | `head -n 10 data.csv` | Prints the first 10 lines of a file. |
| `tail` | `tail -f app.log` | Prints the last 10 lines. `-f` "follows" the file, updating live as new logs are written. |
| `nano` | `nano script.sh` | Opens a simple, beginner-friendly terminal text editor. |
| `vim` | `vim script.sh` | Opens an advanced, highly efficient terminal text editor. |

---

## 🔀 4. Search & Text Processing (The UNIX Philosophy)
Advanced tools for filtering and processing data streams.

| Command | Example Usage | Description |
| :--- | :--- | :--- |
| `grep` | `grep "ERROR" app.log` | Searches for a specific word or pattern inside a file. Use `-i` to ignore case, `-r` to search recursively in folders. |
| `find` | `find . -name "*.py"` | Searches the file system for files matching a specific name or condition. |
| `wc` | `wc -l dataset.csv` | **Word Count:** Counts the lines (`-l`), words (`-w`), or characters (`-c`) in a file. |
| `sort` | `sort list.txt` | Sorts lines of text files alphabetically or numerically. |
| `awk` | `awk '{print $1}' log.txt`| Advanced text processing language; commonly used to extract specific columns of data. |
| `>` and `>>`| `echo "hello" > file.txt` | **Redirection:** `>` overwrites a file with new output. `>>` appends to the end of a file. |
| `\|` (Pipe) | `ls -la \| grep ".git"` | **Pipe:** Takes the output of the command on the left and feeds it as input to the command on the right. |

---

## 🔐 5. Permissions & Ownership
Linux is a multi-user environment. These commands manage access control.

| Command | Example Usage | Description |
| :--- | :--- | :--- |
| `chmod` | `chmod +x script.sh` | **Change Mode:** Modifies file permissions. `+x` makes a script executable. `755` sets standard web permissions. |
| `chown` | `chown user:group file` | **Change Owner:** Changes the user and/or group ownership of a file. |
| `sudo` | `sudo apt update` | **Superuser Do:** Executes a command with elevated, administrative (root) privileges. |

---

## ⚙️ 6. Process & Resource Management
Tools for monitoring system performance and stopping runaway programs.

| Command | Example Usage | Description |
| :--- | :--- | :--- |
| `top` / `htop`| `htop` | Opens an interactive task manager showing CPU, RAM, and running processes. |
| `ps` | `ps aux` | **Process Status:** Lists all currently running processes and their Process IDs (PIDs). |
| `kill` | `kill 1234` | Stops a process cleanly using its PID. Use `kill -9 1234` to force-kill a frozen process. |
| `pkill` | `pkill node` | Kills processes by name rather than PID (e.g., kills all running Node.js servers). |

---

## 📦 7. Package Management (Ubuntu/Debian)
Commands to install and update software tools (requires `sudo`).

| Command | Example Usage | Description |
| :--- | :--- | :--- |
| `apt update` | `sudo apt update` | Refreshes the local database of available software packages. *(Always run this first)*. |
| `apt upgrade`| `sudo apt upgrade` | Installs the newest versions of all currently installed packages. |
| `apt install`| `sudo apt install git` | Downloads and installs a specific software package. |
| `apt remove` | `sudo apt remove git` | Uninstalls a software package. |

---

## 🌐 8. Networking
Tools for diagnosing connectivity and downloading files.

| Command | Example Usage | Description |
| :--- | :--- | :--- |
| `ping` | `ping google.com` | Tests connectivity to a server by sending ICMP packets. (Press `Ctrl+C` to stop). |
| `curl` | `curl -O http://url.com` | Transfers data from or to a server. Commonly used to test APIs or download files. |
| `wget` | `wget http://url.com/file`| A robust command-line utility for downloading files from the web. |
| `ip a` | `ip a` | Displays your machine's local IP addresses and network interfaces. |

---

## 🗜️ 9. Archiving & Compression
Commands for zipping and unzipping project folders.

| Command | Example Usage | Description |
| :--- | :--- | :--- |
| `tar -czvf` | `tar -czvf archive.tar.gz ./src` | Compresses a folder into a `.tar.gz` archive. |
| `tar -xzvf` | `tar -xzvf archive.tar.gz` | Extracts a `.tar.gz` archive into the current folder. |
| `zip` | `zip -r proj.zip ./proj` | Compresses a directory into a standard `.zip` file. |
| `unzip` | `unzip proj.zip` | Extracts a standard `.zip` file. |

---

## ⌨️ 10. Essential Keyboard Shortcuts
Mastering these shortcuts significantly speeds up terminal workflow.

* **`Tab`** : Auto-completes file names, folder names, and commands.
* **`Up Arrow` / `Down Arrow`** : Cycles through your previous command history.
* **`Ctrl + C`** : Safely terminates the currently running command or script.
* **`Ctrl + Z`** : Suspends (pauses) the currently running command, sending it to the background.
* **`Ctrl + R`** : Opens a "reverse search" to easily find a long command you typed previously.
* **`Ctrl + L`** : Clears the terminal screen (same as typing `clear`).
* **`Ctrl + A` / `Ctrl + E`** : Moves the cursor to the exact beginning (`A`) or end (`E`) of the current line.
