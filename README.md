# Data-Camp 2025 exercises using Marimo Notebooks

A collection of notebooks to get started with data analysis in Python.

We use the rather new Marimo notebooks (instead of the much older [Jupyter](https://jupyter.org) which serves a similar purpose). 
See [marimo.io](https://marimo.io) for more explanation for this new hot python project!

Note: it is possible to convert between marimo and Jupyter noteboks if you prefer to switch at some point.

## Checking out the repository

In the command line terminal, navigate to where you want to keep the data-camp files on your computer and check out the repository:

```sh
git clone git@github.com:felixpatzelt/data-camp-2025.git
```

Then change your working directory:

```sh
cd data-camp-2025
```

## Install

On mac OS, first install [brew](https://brew.sh) as a system wide package manager. Then use

```brew install uv```

to install the python package manager [uv](https://docs.astral.sh/uv/).

You should be able to install uv using whichever package manager other than brew is available on
your system but this was not tested.

All Python dependencies are taken care of by uv. You can what is configured in the `pyproject.toml` file in the project directory.

## Working in Notebooks

From the project directory, run

```uv run marimo edit notebooks```

A browser window will open showing you the main marimo screen. A link to the webpage is also printed out in the terminal.

Go to the [getting started](https://docs.marimo.io/getting_started/) section of the marimo documentation to learn more.


## Slides

As we re-use some existing material, the presentation slides can be found in a different repository on a data-camp branch right now. The files are [here](https://github.com/felixpatzelt/statistics-for-everyone/tree/data-camp) and they can be viewed [here](https://felixpatzelt.com/data-camp-2025/).

## Getting the Data

To keep things simple the project files are public for now. However, this means we cannot check in proprietary data here. We will distribute further material during the meeting as required.
