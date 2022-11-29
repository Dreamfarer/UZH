Git repositories are typically used to synchronize the work between different developers. In this task, we will test, if you know how to `clone` an existing repository and how to `push` your updates. You will again work in the script file `script.sh`.

**Note:** Since we're working with a remote repository, the variable `$REPO_URL` must be used in the script in place of the actual location of the repository on the internet. ACCESS will set this variable to a specific value, because, of course, it must be a repository where ACCESS has read/write permissions. This means:

* You should *not* specify an exact repository in your `script.py`.
* Do *not* set `$REPO_URL` in your script.
* Wherever you would specify the exact repository URL, you must use the variable `$REPO_URL`.
* To test your script locally on your machine with your own repository, you can run your script like this: `REPO_URL="http://some.server.com/yourname/yourrepo" ./script.sh`. This will set the variable `$REPO_URL` to the given value before running the script, so that the script can use it.

For this task, perform the following steps:

* Clone the repository at `$REPO_URL` into the folder `repo`.
* Change the working directory to the new folder (using the command `cd`).
* Create a new file `c.txt` with the content `ccc`.
* Add and commit your changes using the message `Add new file c.txt with some content`.
* Push the new commit to the repository.

**Note:** After executing the script, your index should be clean and there should be no changed files in your working directory.

**Note:** Use `$REPO_URL` in your script and clone to a folder named `repo` or the grading script will fail.

**Note:** Your scripts cannot access the internet and will timeout if you try.
