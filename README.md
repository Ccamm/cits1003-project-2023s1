# CITS1003 CTF Assignment 2023 Challenge Files

Here will be the location of the challenge files for CITS1003 Semester 1 2023 assignment.

# How to add challenges

*Stolen from DownunderCTF*

**Do not clone this repo directly, and do not make any commits to this repo directly**. We want to make sure that any challenges you put into this repo is committed in correctly (or at least mostly correctly) right from the get go. 

The way we'll ensure this is by requiring you to fork this repo, make your changes, and then create a Pull Request (PR) to get this repo updated. Within the PR, you should put any information about the challenge that you think is important. Someone else will need to review your PR and ensure that it's good to go before approving it, at which point you (or anyone else) can merge it into this repo.

The steps generally go like this:

1. Fork this repo (click the Fork button on the top right hand side of this page, assuming you're on a computer).
2. Clone your own fork (not this repo!) down to your machine. `git clone <your_forked_repo_link_here>`
3. Create a new branch, checkout to it, and make any changes you need to here (add your challenge into the repo during this step). `git checkout -b branch-name-here`
4. Ensure that you stage and commit your changes on this branch, and then push your branch to your forked repo. You'll need to push your branch specifically. For example: `git push origin branch-name-here`.
5. On GitHub, go to the page of your forked repo, switch to your new branch on the repo, and then click the Pull Request button. This will let you create a pull request on this main repo.
6. If you have to make any changes after the last step, you can just make the changes on your forked repo in the new branch. Any time you push your changes to GitHub, the PR will be updated to reflect your changes.

You can also follow [this guide](https://gist.github.com/Chaser324/ce0505fbed06b947d962). It describes how the Fork and PR workflow works. Note that you'll probably not be required to do it exactly as they have (for example, you'll likely not be required to rebase your branch with master as your changes to the repo should be independent from everyone elses).

# Challenge Format

## Folder Structure

Files for a specific challenge need to be stored in a folder with the name of the challenge inside the respective category folder. Inside the challenge folder, you'll need the following structure.

* `README.md`: Contains information about the challenge. Follow the below template for creating this file.
* [Optional] `challenge/`: Files for creating/running the challenge eg. source code. **These files will not be provided to competitors**.
* [Optional] `publish/`: Folder with files that will provided to competitors.
    - `{challenge-name}.zip`: A ZIP file of the files that will be provided to players. Replace `{challenge-name}` with the name of the challenge.
* [Optional] `solution/`: Files for solving the challenge.

## Challenge README.md Template

Use the following template for creating the `README.md` for challenges.

```markdown
# Challenge

**Name:** FILL IN

**Category:** FILL IN

**Difficulty:** FILL IN

**Flag:** FILL IN

---

## Description

FILL IN

---

## Solution

FILL IN

---

## [Optional] How to run

FILL IN
```
## Flag format

The format of *most* flags should be `UWA{w0w_c00l_3xAmP13_fl4G1!}` where the text inside the `{}` is changed.

Not all challenges should be in the `UWA{}` though (especially forensic challenges (insert `grep UWA` meme)).

