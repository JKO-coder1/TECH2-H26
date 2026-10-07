
# TECH2: Introduction to Programming, Data, and Information Technology

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Course material for fall 2026 (H26) — Author: Richard Foltyn


## Course outline for part 2

`L` = Lecture, `W` = Workshop


| Week | Day         | L/W | Topic | Notes & Exercises | Solutions |
|------|-------------|-----|-------|----------------------|------------------------------------------|
|  40  | Wed, Sep 30 | `L` | GitHub & NumPy | [Slides](lectures/lecture1/lecture1-slides.pdf), [Notebook](lectures/lecture1/lecture1.ipynb), [PDF](lectures/lecture1/lecture1.pdf) | —  |
|      | Fri, Oct 2 | `W` | GitHub & NumPy | [Notebook](workshops/workshop1/workshop1.ipynb), [PDF](workshops/workshop1/workshop1.pdf) | [Notebook](workshops/workshop1/workshop1-solution.ipynb), [PDF](workshops/workshop1/workshop1-solution.pdf) |
|  41  | Wed, Oct 7  | `L` | Intro to pandas | [Notebook](lectures/lecture2/lecture2.ipynb), [PDF](lectures/lecture2/lecture2.pdf) | —  |
|      | Wed, Oct 9  | `W` | Intro to pandas | [Notebook](workshops/workshop2/workshop2.ipynb), [PDF](workshops/workshop2/workshop2.pdf) | TBA |
|  42  | Wed, Oct 14  | `L` | Plotting | [Notebook](lectures/lecture3/lecture3.ipynb), [PDF](lectures/lecture3/lecture3.pdf) | —  |
|      | Fri, Oct 16 | `W` | Plotting | [Notebook](workshops/workshop3/workshop3.ipynb), [PDF](workshops/workshop3/workshop3.pdf) | TBA |
|  43  | Wed, Oct 21 | `L` | Grouping and aggregation | [Notebook](lectures/lecture4/lecture4.ipynb), [PDF](lectures/lecture4/lecture4.pdf) | —  |
|      | Fri, Oct 23 | `W` | Grouping and aggregation | [Notebook](workshops/workshop4/workshop4.ipynb), [PDF](workshops/workshop4/workshop4.pdf) | TBA |
|  44  | Wed, Oct 28 | `L` | Concatenating and merging | [Notebook](lectures/lecture5/lecture5.ipynb), [PDF](lectures/lecture5/lecture5.pdf) | —  |
|      | Fri, Oct 30 | `W` | Concatenating and merging | [Notebook](workshops/workshop5/workshop5.ipynb), [PDF](workshops/workshop5/workshop5.pdf) | TBA |
|  45  | Wed, Nov 4 | `L+W` | AI week | TBA | — |
|      | Fri, Nov 6 | `L+W` | AI week | TBA | — |


## Forking & Cloning

### Forking

- Click on the `Fork` icon to fork this repository (create your own personal copy)
- In the future, you need to click on `Sync Fork` to get new commits made to this repository into your forked version.

### Cloning

1. Click on the green `Code` icon to clone the repository to your computer
2. Select HTTPS or SSH depending on your authentication method (SSH keys will only work if you have configured them) and copy the URL.
3. You can clone the repository directly in Visual Studio Code, or use the command line:

    _Using HTTPS (no SSH key configured):_
    ```bash
    git clone https://github.com/richardfoltyn/TECH2-H26.git
    ```
    _Using SSH keys:_
    ```bash
    git clone git@github.com:richardfoltyn/TECH2-H26.git
    ```


## Creating a Conda environment

Using the Anaconda Prompt (Windows) or Terminal (macOS), you can use
the environment definition file ([environment.yml](environment.yml)) provided in this repository to create
a conda environment called `TECH2`:
```bash
conda env create -f environment.yml
```
Note that you first need to change to the directory where `environment.yml` is located for this to work.

If you don't know how to locate the `environment.yml` file on your system,
you can also download it directly from GitHub and create the environment in one step:
```bash
curl -O https://raw.githubusercontent.com/richardfoltyn/TECH2-H26/main/environment.yml
conda env create -f environment.yml
```


## AI Learning Companion (`tech2` skill)

This repository includes a course skill (`tech2`) that turns compatible AI coding assistants into an interactive tutor and setup assistant for TECH2.

### What it does
- Environment and setup help: Step-by-step assistance for Miniforge/Conda, Git, VS Code, and the `TECH2` Conda environment on Windows, macOS, and Linux.
- Curriculum-aligned tutoring: Provides Socratic hints, explanations, and code examples tailored strictly to the concepts covered up to your current course week.

### CLI tools and agents
The skill is located in `.agents/skills/tech2/` (and `.claude/skills/tech2/`) and is automatically discovered when launched inside this repository. It should work with most AI coding assistants, including:
- [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) (`claude`)
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli) (`codex`)
- [Antigravity CLI](https://antigravity.google/product/antigravity-cli) (`agy`)
- [OpenCode](https://opencode.ai) (`opencode`)
- [Pi](https://pi.dev/) (`pi`)

### Usage
Launch your CLI assistant from the root of your cloned course repository:
```bash
claude
# or: codex, agy, opencode, pi
```
Then ask questions about installation or course materials, for example:
- "I'm having trouble creating the TECH2 conda environment on Windows."
- "I'm in Week 8. Can you explain how boolean indexing works in pandas?"


## Additional resources

1. [Think Python](https://allendowney.github.io/ThinkPython/index.html) by Allen B. Downey:
   general intro to Python, chapters are available as Jupyter notebooks.
2. [Python for Everybody](https://www.py4e.com/book) by Charles R. Severance:
   general intro to Python with a focus on data analysis, available as PDF.
3. [QuantEcon](https://quantecon.org/lectures/): Python programming for economics & finance
    (beginners & advanced)
3. [Introduction to Programming and Numerical Analysis](https://sites.google.com/view/numeconcph-introprog/home):
    Python for macroeconomics, taught at the University of Copenhagen

## License

This material is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/),
except for the data files contained in the `data/` folder, which
fall under the terms imposed by the original content creators.
