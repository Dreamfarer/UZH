## 💾 UZH Computer Science

### About this project

This repository is a collaboration between various computer science students currently completing the assessment year at the [University of Zurich](https://www.oec.uzh.ch/en/studies/bachelor/it.html). Its main goal is to provide documented, functioning and divers sample solutions for fellow students seeking help in computer science.

> To date, this project only includes tasks from the lecture _Informatics I_ which are being distributed over the ACCESS platform. In the future, it is planned to incorporate a handful of assignments, guides and information for other lectures.

> :warning: **Disclaimer** :warning:<br>This repository is meant as a guideline and helping hand if you get stuck on a task. It is not the idea that you just copy and paste the answers blindly. Use the solution as inspiration on what's missing in your own code. This also counts for the provided tests: It can be boring to form them yourself, but it helps you understand the task better, and obviously, you don't have tests provided when working on real coding problems.


## 📝 Contributing
There is nothing worse than being forced into a certain coding style. Having only one solution provided promotes exactly that. Read through the following guide and share your solution today to contribute to a diverse range of styles and approaches. This is the only way we can make sure other students find a satisfactory answer to their questions.

> To make contributing as much painless and fun as possible, we have created the following manual supporting contributions via **Git-SCM** (command-line), **Visual Studio Code** and **PyCharm**. Chose what suits you best! You'll encounter a drop-down menu whenever some action is specific to one particular method. However, the main parts, like creating a new branch or submitting a pull request (PR) do not differ whatsoever.

### Step 0: Get collaborator rights

If this is your first time around, please stick around for the following explanation. However, if you already are a collaborator GitHub-wise, jump right to the next step. We rely on branch-based contributions; in order for you to follow this guide along and be able to create branches yourselves, you absolutely need to get the collaborator role. Don't be hesitant, create a simple issue over [here](https://github.com/Perytron/UZH/issues) and ask to receive your special rights! :)

> If you only want to do a one time contribution, consider helping via the forking method explained further down.

### Step 1: Create a new branch
Head over to [here](https://github.com/Perytron/UZH/branches) and hit the green button labeled "**New branch**". Enter a new branch name with the following convention: **MODULE-EXERCISE-TASK-USERNAME-DESCRIPTION**. However, please use lowercase letters only, except for your username, and separate every task explicitly, e.g. **info1-009-01-02-03-04-Perytron-solution** if you were to upload solution one to four of the 9th exercise set. Afterwards, tap the green button labeled "**Create branch**" to confirm.

### Step 2: Clone the repository

> This step only needs to be performed once in the beginning. For future contributions you'll want to fetch the repository first as described in [step 3](https://github.com/Perytron/UZH/edit/28-update-readme/README.md#step-3-switch-to-your-newly-created-branch) before proceeding. This will update your local copy of this repository to the current version found here on Github.

<details><summary>Git-SCM</summary>

Open your git-enabled terminal of choice in whatever local directory you want the repository to be stored. Execute the following command:
```
git clone https://github.com/Perytron/UZH.git
git cd UZH
```

</details>

<details><summary>Visual Studio Code</summary>

Open up Visual Studio Code and either hit **Ctrl+Shift+G** or navigate to the left-most toolbar and click onto the icon that looks like a branch _(third icon underneath the Visual Studio Code logo)_. Click onto the button labeled "**Clone Repository**". Copy the following line and paste it into the search bar that has just popped up in Visual Studio Code.
```
https://github.com/Perytron/UZH.git
```
Chose whatever local directory you want the repository to be stored. Visual Studio Code will ask you whether you want to open the repository, confirm by clicking onto "**Open**".

</details>

<details><summary>PyCharm/CLion</summary>

After launching PyCharm/CLion perform the following steps:
```
1. Tap on “Get from VCS” in the top right corner.
2. Paste the following URL into the input field: “https://github.com/Perytron/UZH.git”
3. Select the target destination you want the project folder to be in.
4. Make sure the chosen Version Control System is “Git”.
```
> Alternatively you can also log into GitHub, then your able to select the project on the left side of the window.

</details>

### Step 3: Switch to your newly created branch
<details><summary>Git-SCM</summary>

Copy the following statements by tapping the copy button on the right-hand side of the code box and paste them into your git-enabled terminal of choice. Be sure to change **BRANCH_NAME** to your name defined in step 1, for example **git checkout 009-1-Perytron-Fix**. You can safely paste the whole code block into the terminal, it will only execute the first two statements automatically.
> Please make sure to execute the commands inside the locally cloned repository folder. If you have followed the previous steps of this manual, you are good to go.
```
git checkout main
git fetch --all
git fetch --prune
git checkout BRANCH_NAME
```

</details>
<details><summary>Visual Studio Code</summary>

The following step is very important because if you do not perform it, you would commit your local changes to the **main** branch directly. Like you have done in step two, navigate to the **Source Control** tab again within Visual Studio Code.

Firstly, inside the **Source Control** tab, click onto the menu labeled "**...**" and choose "**Fetch**" to let Visual Studio Code discover your freshly created branch. Next off, again opening the menu labeled "**...**", choose "**Checkout to...**". The search bar will pop up; click onto the branch you have created in step one. It will appear in the form of "**origin/BRANCH_NAME**", in our example this would be: "**origin/009-1-Perytron-Fix**".

</details>
<details><summary>PyCharm/CLion</summary>

Inside your PyCharm/CLion you have to perform the following actions:
```
1. Open your cloned repository folder
2. Tap on Git on the bottom left. A window should appear with branches to the left, commit history in the middle and commit details to the right.
3. After move to the top bar and select "Git" > "fetch"
4. After fetching successfully you should be up-to-date.
5. Your newly on GitHub created branch should be visible under "Remote" > "origin"
6. Right-click on your branch and select checkout.
7. Now your head is on the right branch.
```

</details>

### Step 4: Do your magic, be creative
Now it is the time to implement all your changes. Please make sure that your code works and yields the maximum amount of points possible. If this is not the case, please clearly label them as such. Remember to move all the files you are willing to upload into a folder following the convention of **USERNAME Solution**, e.g. **Perytron Solution**, before committing. Note that if your username originally starts with a lower-case letter, be sure to capitalize the first letter, e.g. change **perytron** to **Perytron**.

> :warning: Verify that your solution is correct by testing your code with different inputs before opening a pull request.

> :warning: Only include source-files holding your code, no compiled files (.exe files for example).

> As for test cases: There is one file where every contributor adds their individual test cases, so that all are collected in one file. Just add yours at the bottom of the file. Please append your test function names with your username or abbreviation, e.g. def test_invalid_input_PER.

### Step 5: Just send it (Commit & Push)
> When writing your commit message, follow a similar convention as in the naming of the branch by starting the sentence with a capital letter and writing in present tense **MODULE-EXERCISE-TASK: DESCRIPTION**, e.g **Info1-009-01: Add solution** 
<details><summary>Git-SCM</summary>

To track, stage and commit your changes, you will have to copy and paste the following commands into your git-enabled terminal of choice. Please change **COMMIT_MESSAGE** and **ADDITIONAL_DESCRIPTION** to something meaningful, e.g. **git commit -m "E10 T1 fix" -m "Fix typo in main function"**. Don't forget to include the quotation marks (").
```
git add .
git commit -m "COMMIT_MESSAGE" -m "ADDITIONAL_DESCRIPTION"
```
Like in step 2, change the **BRANCH_NAME** to your name defined in step 1.
```
git push origin BRANCH_NAME
```

</details>
<details><summary>Visual Studio Code</summary>

Open the **Source Control** panel again like you have previously done in step two and three. However, this time, you will not be using the menu labeled "**...**". Instead, above the button labeled "**Commit**", enter a short but meaningful summary; tell us what you have changed. If you need over 50 characters, Visual Studio Code tells you that the message will be cut off on GitHub: Consider shortening it or adding a line break, which will appear as an additional description on GitHub.

If you are satisfied with your commit message, tap onto the downwards pointing arrow on the right-hand side of the button labeled "**Commit**". Chose "**Commit & Push**" to upload your changes to GitHub.

</details>
<details><summary>PyCharm/CLion</summary>

After you coded your solution inside PyCharm/CLion or manually copied your solution files to your local repository folder, PyCharm/CLion should automatically recognise your changes.

> Please follow the correct folder structure laid out in our guidelines on GitHub otherwise your PR might get rejected.

In order to upload your changes you have to do the following steps:

```
1. On the left of your screen select "Commit"
2. If you see your solution files under the "Unversioned Files" tab, you have to right click on them and select "Add to VCS" (Version Control System)
 !!! Be sure to only add the actual solution files, not for example .gitignore or xml files. !!! 
 To make future commits easier you can select all those files -> right click -> add to .gitignore -> exclude
3. If your files are under the "Changes" tab, checkbox them.
4. Beneight write a logical commit message like, "Add 10.2 solution"
5. Click "Commit and Push" and "Push" again in the popup.
```

If the push was successful you should see your commit on GitHub but remember look under your branch.
 

</details>

### Step 6: Create a pull request (PR)
Head over to [here](https://github.com/Perytron/UZH/compare/) and click on the button labeled "**compare: main**". From the list, chose the branch you have just changed. Name the pull request accordingly by starting the sentence with a capital letter and writing in present tense with the following convention: **MODULE-EXERCISE-TASK: DESCRIPTION**, e.g **Info1-002-04: Add solution** Inside the pull request, add [Perytron (Gianluca)](https://github.com/Perytron) as a reviewer and yourself as an assignee. Please also tag your pull request (PR) with the appropriate labels. For example, if you were to upload solutions, chose the yellowish label called "**solution**". 

Your changes are now awaiting supervision, however, the code itself will not be tested. The only check involves oversighting that nothing gets unintentionally changed or deleted.

> After the pull request (PR) has been accepted, the branch you have created previously in step one gets closed, as your changes have now been added to the main branch. This is done automatically to keep the repository clean of unused branches. If you want to add something to your already closed branch (e.g. you forgot to add your test files), reopen the branch [here](https://github.com/Perytron/UZH/pulls?q=is%3Apr+is%3Aclosed) by selecting your already closed pull request, scrolling to the bottom and clicking the button labeled "**Restore Branch**". Start at [step 3](https://github.com/Perytron/UZH/edit/28-update-readme/README.md#step-3-switch-to-your-newly-created-branch) of this manual. Please be aware that you need to update the branch first because it is now behind the main branch. Instead of using **git fetch**, use **git pull** when in your local branch to actually get the newest version with all its files (**git pull** is the equivalent of **git fetch & git merge**).

### Alternative: Contribution via fork
> Don't worry if you have never contributed to a GitHub repository. Read through [this](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) official tutorial, which teaches you how to fork your own copy of this project and how to create a pull request. As a supplement to the guide, the download link for **git** can be found [here](https://git-scm.com/downloads). Additionally, read the [these](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) official GitHub instructions on how to sync your fork with its original repository.

## ❓ Frequently Asked Questions
<details><summary>Q: I've made changes to the wrong local branch, what should I do?</summary>

A: I would definitely be lying if I say this has never happened to me, quite the contrary, actually. But don't worry, everything is alright! For this method to work, however, you need to be able to access **git** via the command-line. Copy the following line and paste it into your git-enabled terminal of choice. It will copy your changes.
```
git stash
```
Before copying and pasting the following commands, change **BRANCH_NAME** to the name of the branch you want your changes to be applied to. **git** will now carry over any changes made to the wrong branch over to your branch of choice.
```
git switch BRANCH_NAME
git stash apply
```

</details>
<details><summary>Q: How do I clean up my local repository?</summary>

A: **git** does not automatically delete unused branches, both remote and local ones, which could lead to a great mess in the long run. It is important to clean up your repository periodically. First of all, we'll switch to the main branch and check which branches there are by copying and pasting the following lines into your git-enabled terminal of choice.
```
git switch main
git branch -v -a
```
This command will yield us a result like this, where **white** and **green** entries signify that this branch exists locally. Furthermore, **green** tells you that you are currently on this very branch. **Red** entries mean that these branches exist or have existed at one point in time.
```diff
  28-update-readme                                   
+ * main                                             
- remotes/origin/010-01-02-03-04-Perytron-solution   
- remotes/origin/011-01-02-03-04-Perytron-solution   
- remotes/origin/28-update-readme                    
- remotes/origin/HEAD                                
- remotes/origin/main                                
```
Therein lies the problem: **git** does not automatically delete the remote branches (the **red** ones), even if they might not exist on GitHub anymore. You'll want to use the following command to delete your local remote branches, that were already deleted on GitHub.
```
git fetch -p
```
However, prune (the above command) will not delete local branches (the **white** ones). If you wanted to delete the white **28-update-readme** branch, you would use the following command:
```
git branch -d 28-update-readme
```

Deleting remote branches is very easy too, head over [here](https://github.com/Perytron/UZH/branches) and delete your desired branch using the 🗑️- icon. Please make sure you have selected the correct branch, else you might accidentally delete a branch actively used by a colleague.

If you find yourself in the situation where nothing works anymore, you've completely messed up, there is still hope: You can always store the changed files in whatever folder that does not belong to this repository and completely delete the local copy of the repository. Afterwards, clone it again using [step 2](https://github.com/Perytron/UZH#step-2-clone-the-repository) of this documentation and instead of implementing everything again from scratch in [step 4](https://github.com/Perytron/UZH#step-4-do-your-magic-be-creative), you'll just copy over the changed files which you have temporarily stored before. 

</details>

## 🆘 Help
If you encounter any issue or would like to contribute to a specific problem without going through the process of creating a pull request, create an [issue](https://github.com/Perytron/UZH/issues) and we will aid you as soon as possible. For the non-GitHub users among you, write us directly in the WhatsApp chat "Informatik Jahrgang 22".
