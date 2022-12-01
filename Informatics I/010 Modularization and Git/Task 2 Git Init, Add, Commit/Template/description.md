In this task, you will go through the required steps for creating a new local Git repository. We will test whether you know how to `init` a repository, `add` files to the index, and `commit` change sets. In contrast to many other tasks, you are not going to write code this time. All you do is to add a set of terminal commands to the `script.sh`. 

Assume that the `script.sh` will be executed in your current working folder. Perform the following steps:

* Initialize a Git repository in the current folder.
* Create a new file `a.txt` with the content `aaa` (You can achieve this on the terminal through `printf "aaa" > a.txt`).
* Create a new file `b.txt` with the content `bbb`.
* Add both files to the Git index.
* Commit the current index and use the commit message `Add files a.txt and b.txt`.
* *Append* the text `b2` in a new line to `b.txt` (You can achieve this through `printf "\nb2" >> b.txt`, please note the `\n` and the `>>`)
* Add and commit your changes using the message `Add second line to b.txt` (normally, this would open an editor, but ACCESS is non-interactive, so use the `-m` parameter).

The grading will only consider the current state of the index and the history of your newly created repository, so feel free to add further `printf` commands to analyze what's happening. However, we strongly recommend you to experiment with the different commands locally and to inspect their effects in a graphical tool.

**Note:** If you do not have a working Git installation on your machine that you can use from the command line, please [install a current version](https://git-scm.com/downloads). As Git internally represents the history in a tree, we also strongly recommend you to use a graphical client like [SourceTree](https://www.sourcetreeapp.com/), [Git Extensions](https://gitextensions.github.io/), or the minimalistic [Gitk](https://git-scm.com/docs/gitk) to inspect the current state of the repository.

**Note:** After executing the script, your index should be clean and there should be no changed files in your working directory.

**Note:** Your scripts cannot access the internet and will timeout if you try.
