# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*
~~Strikethrough text~~

- Bullet point 1
- Bullet point 2
- Bullet point 3

1. Numbered item 1
2. Numbered item 2
3. Numbered item 3

[Link text](https://www.example.com)
![Image alt text](image.jpg)

> Blockquote

`Inline code`

- `git init`: Initialize a new Git repository
- `git clone <repository>`: Clone a repository from a remote source
- `git add <file>`: Add a file to the staging area
- `git commit -m "<message>"`: Commit the changes in the staging area with a message
- `git status`: Show the status of the working directory and staging area
- `git log`: Show the commit history
- `git branch`: List all branches in the repository
- `git checkout <branch>`: Switch to a different branch
- `git merge <branch>`: Merge changes from a different branch into the current branch
- `git push`: Push local commits to a remote repository
- `git pull`: Fetch and merge changes from a remote repository
- `git remote add <name> <url>`: Add a remote repository
- `git remote -v`: List all remote repositories
- `git diff`: Show the differences between the working directory and the staging area
- `git reset <file>`: Unstage a file from the staging area
- `git revert <commit>`: Create a new commit that undoes the changes made in a previous commit
- `git stash`: Save changes that are not ready to be committed
- `git tag <name>`: Create a new tag for a specific commit

## Python Commands and Statements

Here is an overview of some commonly used Python commands and statements:

- `print()`: Used to display output on the console.
- `input()`: Used to get user input from the console.
- `if` statement: Used for conditional execution of code.
- `elif` statement: Used for additional conditions in an `if` statement.
- `else` statement: Used for code execution when no conditions are met in an `if` statement.
- `for` loop: Used for iterating over a sequence of elements.
- `while` loop: Used for executing a block of code repeatedly as long as a certain condition is true.
- `def` statement: Used to define a function.
- `return` statement: Used to return a value from a function.
- `import` statement: Used to import modules or specific functions from modules.
- `try` and `except` statements: Used for exception handling.
- `with` statement: Used for working with files or resources that need to be cleaned up.
- `class` statement: Used to define a class.
- `self` keyword: Used to refer to the instance of a class within the class definition.
- `super()` function: Used to call a method from the parent class.
- `assert` statement: Used for debugging and testing assumptions in code.
- `pass` statement: Used as a placeholder for empty code blocks.
- `break` statement: Used to exit a loop prematurely.
- `continue` statement: Used to skip the rest of the current iteration of a loop.
- `range()` function: Used to generate a sequence of numbers.
- `len()` function: Used to get the length of a sequence or the number of characters in a string.
- `sorted()` function: Used to sort a sequence.
- `zip()` function: Used to combine multiple sequences into a single sequence of tuples.
- `min()` function: Used to get the minimum value from a sequence.
- `max()` function: Used to get the maximum value from a sequence.
- `sum()` function: Used to get the sum of all elements in a sequence.
- `round()` function: Used to round a number to a specified number of decimal places.
- `abs()` function: Used to get the absolute value of a number.
- `type()` function: Used to get the type of an object.
- `isinstance()` function: Used to check if an object is an instance of a specific class.
- `dir()` function: Used to get a list of attributes and methods of an object.
- `help()` function: Used to get help information about an object or function.

# Common Terminal Commands

## Key Commands & Navigation

Before we look at some common commands, I just want to note a few keyboard commands that are very helpful:

- `Up Arrow`: Will show your last command
- `Down Arrow`: Will show your next command
- `Tab`: Will auto-complete your command
- `Ctrl + L`: Will clear the screen
- `Ctrl + C`: Will cancel a command
- `Ctrl + R`: Will search for a command
- `Ctrl + D`: Will exit the terminal

## Manual Command

On Linux and Mac, the `man` command is used to show the **manual** of any command that you can run in the terminal. So if you wanted to know more about the `ls` command, you could run:

```bash
  man ls
```

Unfortunately, if you are on Windows and using Git Bash, the `man` command is not included, however, you can just type the command that you want to know more about and then `--help` and you will get similar info:

```bash
  ls --help
```

You should be able to use the arrow keys or page up and down. When you are ready to exit, just press `q`.

## The `whoami` Command

The `whoami` command will show you the current user that you are logged in as.

```bash
  whoami
```

## The `date` Command

Another really simple one is the `date` command, which, surprise, will show you the current date and time.

```bash
  date
```

## File System Navigation

Commands to navigate your file system are very important. You will be using them all the time. You won't remember every single command that you use, but these are the ones that you should remember.

| Command                             | Description                                                                       |
| ----------------------------------- | --------------------------------------------------------------------------------- |
| pwd                                 | Lists the path to the working directory                                           |
| ls                                  | List directory contents                                                           |
| ls -a                               | List contents including hidden files (Files that begin with a dot)                |
| ls -l                               | List contents with more info including permissions (long listing)                 |
| ls -r                               | List contents reverse order                                                       |
| cd                                  | Change directory to home                                                          |
| cd [dirname]                        | Change directory to specific directory                                            |
| cd ~                                | Change to home directory                                                          |
| cd ..                               | Change to parent directory                                                        |
| cd -                                | Change to previous directory (which could be different than the parent of course) |
| find [dirtosearch] -name [filename] | Find location of a program                                                        |

Of course, you can group flags together. For example, if I want to see more info and view hidden files, I could do `ls -l -a` and even shorten it to `ls -la`.

## Opening a Folder or File

If you want to open a file or a folder in the GUI from your terminal, the command is different depending on the OS.

Mac - `open [dirname]`
Windows - `start [dirname]`
Linux - `xdg-open [dirname]`

You can open folders, files and even URLs

```bash
  open https://traversymedia.com
```

## Modifying Files & Directories

| Command                     | Description                                         |
| --------------------------- | --------------------------------------------------- |
| mkdir [dirname]             | Make directory                                      |
| touch [filename]            | Create file                                         |
| rm [filename]               | Remove file                                         |
| rm -i [filename]            | Remove directory, but ask before                    |
| rm -r [dirname]             | Remove directory                                    |
| rm -rf [dirname]            | Remove directory with contents                      |
| rm ./\*                     | Remove everything in the current folder             |
| cp [filename] [dirname]     | Copy file                                           |
| mv [filename] [dirname]     | Move file                                           |
| mv [dirname] [dirname]      | Move directory                                      |
| mv [filename] [filename]    | Rename file or folder                               |
| mv [filename] [filename] -v | Rename Verbose - print source/destination directory |

We can also do multiple commands at once with the `&&` operator:

```bash
cd test2 && mkdir test3
```

## Right angle bracket >

This symbol tells the system to output results into whatever you specify next. The target is usually a filename. You can use this symbol by itself to create a new file:

```bash
> [filename]
```

When you are done, hit `ctrl+D`

## The `cat` (concatenate) Command

The cat command is a very common command and allows you to create single or multiple files, view content of a file, concatenate files and redirect output in terminal or files.

The most common thing I use it for is to display the contents of a file:

```bash
  cat [filename]
```

You can also view the contents of multiple files:

```bash
  cat [filename] [filename]
```

You can also create a file using the `cat` command:

```bash
  cat > [filename]
```

This will open up a new file and you can start typing. When you are done, you can press `Ctrl + D` to save and exit.

You can also append to a file:

```bash
  cat >> [filename]
```

This will open up the file and you can start typing. When you are done, you can press `Ctrl + D` to save and exit.

You can use it to show line numbers:

```bash
  cat -n [filename]
```

There are other uses as well, but as you can see, the `cat` command is very powerful.

## The `less` Command

The `less` command is used to view the contents of a file. It is similar to the `cat` command, but it allows you to scroll up and down.

```bash
  less [filename]
```

To exit the `less` command, just press `q`.

## The `echo` Command

The `echo` command is used to display messages, or to create and write to files. It is similar to the `cat` command, but it is used to display a single line of text.

```bash
  echo "Hello World"
```

You can also use it to create a file:

```bash
  echo "Hello World" > [filename]
```

You can also append to a file:

```bash
  echo "Hello World" >> [filename]
```

## The `nano` Command

The `nano` command is a text editor that is installed by default on most Linux distributions, MacOS and you can even use it with Git Bash on Windows. It is very similar to the `vim` editor, but it is much easier to use.

You can open an existing file to edit or create a new file and open it with:

```bash
  nano [filename]
```

When you're ready to exit, just hit `Ctrl + X` and then `Y` to save and `N` to not save.

## The `head` and `tail` Commands

The `head` command is used to output the first part of files. By default, it outputs the first 10 lines of each file. You can also specify the number of lines to output.

```bash
  head [filename]
```

You can also specify the number of lines to output:

```bash
  head -n 5 [filename]
```

The `tail` command is used to output the last part of files. By default, it outputs the last 10 lines of each file. You can also specify the number of lines to output.

```bash
  tail [filename]
```

You can also specify the number of lines to output:

```bash
  tail -n 5 [filename]
```

## The `grep` Command

The `grep` command is used to search for a text pattern in a file. It is very powerful and can be used to search for a string or regular expression in a file or set of files.

```bash
  grep [searchterm] [filename]
```

You can also search for a string in multiple files:

```bash
  grep [searchterm] [filename] [filename]
```

There are a lot more things that you can do with the `grep` command, but it's a but more advanced.

## The `find` command

The `find` command is extremely powerful and is used to find the location of files and directories based on conditions that you specify.

To start off by creating something to work with. Let's create 100 files in the current directory. This is one of those things that I talked about earlier where you can do certain things much faster than you could in the GUI. We already know that the `touch` command will create a file. It can also be used to create multiple files.

```bash
  touch file-{001..100}.txt
```

Now we have 100 .txt files in the current directory. Something that would have taken a lot longer to do in the GUI.

Let's do something very simple and find a specific file. The format looks like this:

```bash
  find [dirname] -name [filename]
```

Let's find the file called `file-001.txt`:

```bash
  find . -name "file-001.txt"
```

This will look in the current directory, which is represented with a dot.

We can look in other directories as well. Let's create a file in our home folder called test.txt

```
  touch ~/test.txt
```

To find that file:

```bash
  find ~/ -name "test.txt"
```

We can look for files that match a certain pattern as well. Let's find all files that start with `file-`:

```bash
  find . -name "file-*"
```

We can search for files that are empty:

```bash
  find . -empty
```

Let's append some text to the file `file-002.txt`. We could use the `cat` command, like I showed you earlier, but we can also use the `echo` command:

```bash
  echo "Hello World" >> file-002.txt
```

Now if we find the empty files again, we will see that `file-002.txt` is no longer empty:

```bash
  find . -empty
```

We can remove all of the files that we created with this command:

```bash
  find . -name "file-*" -delete
  rm -f file-* # This will also work
```

There is so much more that you can do with the `find` command, but it goes beyond the scope of this tutorial.

## Piping
Piping is very powerful. It is a way of redirecting standard output to another destination, such as another file. Let's actually use the find command to find a list of files and then pipe them to a new file.

First, we'll create 10 files:

```bash
touch file-{001..010}.txt
```

Now, let's pipe the result from our find into a new file named `output.txt`

```bash
find . -name "file-0*" > output.txt
```

You can see the results now in the new file:

```bash
cat output.txt
```

## Creating a Symlink

A symlink is a special type of file that points to another file. It is a shortcut to the original file. It is useful when you want to access a file in a different location without having to copy it.

We can use the `ln` command to create a symlink:

```bash
  ln -s [filename] [symlinkname]
```

You can remove a symlink with the `rm` command:

```bash
  rm [symlinkname]
```

If you're on Windows and you are not using something like Git Bash, you can use the `mklink` command:

```bash
  mklink [symlinkname] [filename]
```

## File Compression

`tar` is a program for concatenating multiple files into one big file called a **tarball** and reversing this process by extracting the files from the tarball.

| Command                             | Description                |
| ----------------------------------- | -------------------------- |
| tar czvf [dirname].tar.gz [dirname] | Create tarball             |
| tar tzvf [dirname]                  | See what is in the tarball |
| tar xzvf [dirname].tar.gz           | Extract tarball            |

- -c : Creates Archive 
- -x : Extract the archive 
- -f : creates archive with given filename 
- -t : displays or lists files in archived file 
- -u : archives and adds to an existing archive file 
- -v : Displays Verbose Information 
- -A : Concatenates the archive files 
- -z : zip, tells tar command that creates tar file using gzip 
- -j : filter archive tar file using tbzip 
- -W : Verify a archive file 
- -r : update or add file or directory in already existed .tar file 

## The `history` Command

Used to display the history of commands that you have run.

```bash
  history
```

You can also use the `!` to run a command from the history.

```bash
  !100
```

This will run the command that is in the 100th position in the history.