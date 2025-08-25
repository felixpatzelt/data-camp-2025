import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Welcome to Data-Camp 2025

    We use marimo notebooks, which allow you to explore data interactively using the tools that the [Python](https://python.org) ecosystem has to offer! 🧑‍🔬📊

    - A notebook contains cells that either contain [markdown](https://en.wikipedia.org/wiki/Markdown) or Python code. 
    - Every cell has a little "play" symbol ▶︎ that will run the cell, i.e. execute the commands within. 
    - You can also click into a cell and press `shift + enter` on your keyboard to run the cell and continue to the next one.
    """
    )
    return


@app.cell
def _():
    # This is a python cell!
    # Comments start with the hash symbol
    # We import dependencies using the keyword import.
    # Here we import the marimo package to get access to all the nice notebook features
    import marimo as mo
    return (mo,)


@app.cell
def _():
    # Run this cell and see what happens!
    print("Hello, World!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Of course you can do calculations. The last result of a cell is always added to its output automatically"""
    )
    return


@app.cell
def _():
    1 + 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""You can also define variables like this:""")
    return


@app.cell
def _():
    x = 21
    x * 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    We cannot do a full python course in the data camp but if you have ever done any programming (and even if you haven't) you should get into it quite quickly as we go.

    To learn more..
    """
    )
    return


if __name__ == "__main__":
    app.run()
