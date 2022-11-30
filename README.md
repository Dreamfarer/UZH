## UZH Computer Science

### About this project

This repository is a collaboration between various computer science students currently completing the assessment year at the [University of Zurich](https://www.oec.uzh.ch/en/studies/bachelor/it.html). Its main goal is to provide documented, functioning and divers sample solutions for fellow students seeking help in computer science.

> To date, this project only includes tasks from the lecture _Informatics I_ which are being distributed over the ACCESS platform. In the future, it is planned to incorporate a handful of assignments, guides and information for other lectures.


## Contributing
There is nothing worse than being forced into a certain coding style. Having only one solution provided promotes exactly that. Read through the following guide and share your solution today to contribute to a diverse range of styles and approaches. This is the only way we can make sure other students find a satisfactory answer to their questions.

> To make contributing as much painless and fun as possible, we have created the following manual supporting contributions via **Git-SCM** (command-line), **Visual Studio Code** and **PyCharm**. Chose what suits you best! You'll encounter a drop-down menu whenever some action is specific to one particular method. However, the main parts, like creating a new branch or submitting a pull request (PR) do not differ whatsoever.

### Step 0: Get collaborator rights

If you are new here and want to contribute to this amazing project, you have certainly found the right place. This section of the manual focuses on contributing as a collaborator. It requires special rights that firstly need to be granted. Please create an issue over [here](https://github.com/Perytron/UZH/issues) and ask to be a collaborator! :)
> If you only want to do a one time contribution, consider helping via the forking method explained further down.

### Step 1: Create a new branch
Head over to [here](https://github.com/Perytron/UZH/branches) and hit the green button labeled "**New branch**". Enter a new branch name with the following convention: **EXERCISE-TASK-USERNAME-DESCRIPTION** E.g. **009-1-Perytron-Fix**. Tap the green button labeled "**Create branch**" to confirm.

### Step 2: Clone the repository
Open your git-enabled terminal of choice in your directory of choice on your local machine. Execute the following command:
```
git clone https://github.com/Perytron/UZH.git
```


### Step 3: Switch to your newly created branch
<details><summary>Git-SCM</summary>

Copy the following statements by tapping the copy button on the right-hand side of the code box and paste them into your git-enabled terminal of choice. Be sure to change **BRANCH_NAME** to your name defined in step 1, for example **git checkout 009-1-Perytron-Fix**. You can safely paste the whole code block into the terminal, it will only execute the first two statements automatically.
> Please make sure to execute the commands inside the locally cloned repository folder
```
git checkout main
git fetch --all
git checkout BRANCH_NAME
```

</details>
<details><summary>Visual Studio Code</summary>

WIP

</details>
<details><summary>PyCharm</summary>

Inside your PyCharm you have to perform the following actions:
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
Now it is the time to implement all your changes. Please make sure that your code works and yields the maximum amount of points possible. If this is not possible, please clearly label them as such. If the solution is more than one file, be sure to add them all within a folder that is named appropriately.

> As for test cases: There is one file where every contributor can add their individual test cases, so that all are collected in one file. Just add yours at the bottom of the file, ending your test names with your username or abbrevation, e.g. ** def test_invalid_input_PER **. 

### Step 5: Just send it (Commit & Push)
<details><summary>Git-SCM</summary>

To track, stage and commit your changes, you will have to copy and paste the following commands into your git-enabled terminal of choice. Please change **COMMIT_MESSAGE** and **ADDITIONAL_DESCRIPTION** to something meaningful, e.g. **git commit -m "E10 T1 fix" -m "Fix typo in main function"**. Be sure to follow the convention of starting the sentence with a capital letter. Don't forget to include the quotation marks (").
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

WIP

</details>
<details><summary>PyCharm</summary>

After you coded your solution inside PyCharm or manually copied your solution files to your local repository folder, PyCharm should automatically recognise your changes.

> Please follow the correct folder structure laid out in our guidelines on GitHub otherwise your PR might get rejected.

In order to upload your changes you have to do the following steps:

```
1. On the left of your screen select "Commit"
2. If you see your solution files under the "Unversioned Files" tab, you have to right click on them and select "Add to VCS" (Version Control System)
3. If your files are under the "Changes" tab, checkbox them.
4. Beneight write a logical commit message like, "Add 10.2 solution"
5. Click "Commit and Push" and "Push" again in the popup.
```

If the push was successful you should see your commit on GitHub but remember look under your branch.
 

</details>

### Step 6: Create a pull request (PR)
Head over to [here](https://github.com/Perytron/UZH/compare/) and click on the button labeled "**compare: main**". From the list, chose the branch you have just changed. Inside the pull request, add [Perytron (Gianluca)](https://github.com/Perytron) as a reviewer and yourself as an assignee. (Please tag your PR as well with the appropriate labels.) Your changes are now awaiting supervision, however, the code itself will not be tested. The only check involves oversighting that nothing gets unintentionally changed or deleted.


### Alternative: Contribution via fork
> Don't worry if you have never contributed to a GitHub repository. Read through [this](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) official tutorial, which teaches you how to fork your own copy of this project and how to create a pull request. As a supplement to the guide, the download link for **git** can be found [here](https://git-scm.com/downloads). Additionally, read the [these](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) official GitHub instructions on how to sync your fork with its original repository.


### Help
If you encounter any issue or would like to contribute to a specific problem without going through the process of creating a pull request, create an [issue](https://github.com/Perytron/UZH/issues) and I will aid you as soon as possible. For the non-GitHub users among you, write us directly in the WhatsApp chat "Informatik Jahrgang 22"
