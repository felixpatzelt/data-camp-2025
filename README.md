# Data-Camp 2025 exercises using Marimo Notebooks

A collection of notebooks to get started with data analysis in Python.

We use the rather new Marimo notebooks (instead of the much older [Jupyter](https://jupyter.org) which serves a similar purpose). 
See [marimo.io](https://marimo.io) for more explanation for this new hot python project!

Note: it is possible to convert between marimo and Jupyter noteboks if you prefer to switch at some point.

## Checking out this repository

To get the data camp code examples, you need to download them to your computer. Ideally we use `git`, which allows pulling later updates easily.

### Using git

Usually you should have [git](https://git-scm.com) already installed if you do any kind of software development. In the command line terminal, navigate to where you want to keep the data-camp files on your computer and check out the repository:

```sh
git clone git@github.com:felixpatzelt/data-camp-2025.git
```

Then change your working directory:

```sh
cd data-camp-2025
```

### Fallback

If by chance you don't have git and want to get going quickly, you can just try out everything by clicking on the big green `<> CODE` button above and then on `Download ZIP`. Extract the ZIP archive to where you keep your Documents and start exploring.

## Installing Python

You can generally install everything using a package manager on *nix systems like macOS and Linux. Under Windows things are a bit different (see below).

### General remarks

We need to get two things onto our computers to get started:
- [Python](https://www.python.org) `3.13` or later
- [uv](https://docs.astral.sh/uv/)

Once we have these two then uv will take care of everything else automatically. uv can also be installed with pip, the default python package manager, if you happen have already installed python on your system.

### mac OS

It is easiest to first install [brew](https://brew.sh) as a system wide package manager. It is the most common tool to install more "technical" open source software on macOS these days. Then use

```brew install uv```

to install the python package manager [uv](https://docs.astral.sh/uv/).


All Python dependencies are taken care of by uv. If you want, you can check out what is configured in the `pyproject.toml` file in the project directory.


### Windows

#### Using WSL
One method is to install [Windows Subsytem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) and then use the same commands as on macOS and Linux. Administrator rights might be required.

#### Without WSL and without admin rights
Another method is to go to [python.org](https://www.python.org) and download the windows installer for python 3.13.7 (or newer) from the downloads section.

Execute the installer on your computer. Make sure to uncheck "Use admin privileges when installing py.exe", and to check "Add python.exe to PATH". Then click "Install now".

Open windows Powershell (search for it using the start menu), type in the following command, and then press enter to run it:

```
pip install uv
```

## Working with the example notebooks

### Find the project directory

First, open a command line terminal (powershell on windows) in the folder that you checked out / downloaded from github (see [above](#checking-out-this-repository).

Using **macOS** and **Linux**, you can type `ls` and hit enter to list the files in the current directory and `pwd` to see where you are. You can change the current directory using the `cd` command. Note for old-school mac users: a directory is the same thing as a folder. 

Using **Windows** Powershell, you can type `dir` and hit enter to list the files in the current directory and `cd` to change the directory.

**Example**: you type `cd Documents/data-camp-2025` if you are now one level above Documents and put the data-camp files inside your Documents directory. 

### Start marimo
From the project directory, run

```uv run marimo edit notebooks```

A browser window will open showing you the main marimo screen. A link to the webpage is also printed out in the terminal.

Go to the [getting started](https://docs.marimo.io/getting_started/) section of the marimo documentation to learn more.


## Slides

As we re-use some existing material, the presentation slides can be found in a different repository on a data-camp branch right now. The files are [here](https://github.com/felixpatzelt/statistics-for-everyone/tree/data-camp) and they can be viewed [here](https://felixpatzelt.com/data-camp-2025/).

## Getting the Data

To keep things simple the project files are public for now. However, this means we cannot check in proprietary data here. We will diistribute further material during the meeting as required.
