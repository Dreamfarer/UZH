# Variables can either be defined and directly used...
SOME_VAR="Hello World!"
echo $SOME_VAR
# or provided during script invocation like in this task. You
# can use the REPO_URL variable that points to a repository.

# Add your terminal commands here. Make sure to first run them
# locally on your machine to have more detailed error output.
git clone $REPO_URL repo
cd repo
git branch feature_x
git checkout feature_x
printf 'print("Hello World!")' > hello.py
git add hello.py
git commit -m 'Add "Hello World" example'
git push origin feature_x
git checkout master
printf '# good bye' > bye.py
git add bye.py
git commit -m 'Add "Good Bye" comment'
git merge feature_x -m 'Merge "feature_x"'
git push origin master
