import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Welcome to Data-Camp 2025

    We use marimo notebooks, which allow you to explore data interactively using the tools that the [Python](https://python.org) ecosystem has to offer! 🧑‍🔬📊

    ## What is a notebook?

    - A notebook contains cells that either contain [markdown](https://en.wikipedia.org/wiki/Markdown) or Python code. This is a markdown cell.
    - Every cell has a little "play" symbol ▶︎ that will run the cell, i.e. execute the commands within. 
    - You can also click into a cell and press `shift + enter` on your keyboard to run the cell and continue to the next one.

    Follow this link to find a more detailed introduction to [marimo key concepts](https://docs.marimo.io/getting_started/key_concepts/).
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
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Marimo has a special trick: it keeps track of how cells depend on each other and updates them to always keep the notebook up-to-date."""
    )
    return


@app.cell
def _(x):
    # change the line starting with "x = " in the cell above and this cell will change as well!
    x + 3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Let's cover some Python basics. 

    We cannot do a full python course in the data camp but if you have ever done any programming (and even if you haven't) you should get into it quite quickly as we go.

    You already saw integers above. Python also has floating point numbers:
    """
    )
    return


@app.cell
def _():
    # define two floats
    pi = 3.14
    a = 3 / 4

    # return them from this cell.
    pi, a
    return a, pi


@app.cell
def _(mo):
    mo.md(
        r"""You can check the type of a variable by calling `type`. Try it out by modifying the cell below to check some variables we defined."""
    )
    return


@app.cell
def _(x):
    type(x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""`Numeric` types like ints and floats can be used for math operations and comparisons:"""
    )
    return


@app.cell
def _(a, pi):
    5 * a > pi
    return


@app.cell
def _(mo):
    mo.md(
        r"""There are a lot of other useful [built-in types](https://docs.python.org/3/library/stdtypes.html) in Python:"""
    )
    return


@app.cell
def _():
    # strings can hold test:
    i_am_a_string = "Hello!"

    # strings can also span multiple lines:
    description = """
    This is a rather lengthy text
    spanning multiple lines.
    """
    return description, i_am_a_string


@app.cell
def _(description, i_am_a_string):
    # We can combine strings:
    print(i_am_a_string + " " + description)
    return


@app.cell
def _(description):
    # And we can "slice" them
    # Here we take only the first 10 elements in the string
    print(description[0:10])
    return


@app.cell
def _(mo):
    mo.md(
        r"""So we see that that a string is really a sort of ordered collection of characters. There are also other types of collections."""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Lists

    List can contrain arbitrary objects, have an ordering, and are mutible. That is, we can modify them after creating them.
    """
    )
    return


@app.cell
def _(i_am_a_string, pi):
    my_list = [i_am_a_string, pi]

    print(my_list)

    my_list.append(27)

    print(my_list)

    my_list[1] = pi / 2

    print(my_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Tuples

    Tuples are similar to lists, but they are immutible. That is, we cannot modify them after we created them. 
    """
    )
    return


@app.cell
def _():
    my_tuple = (1, 2, 5)

    # my_tuple[1] = 2 # uncomment this line and you will get an error!
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""💡 The round braces around a tuple are optional. When we returned ```pi, a``` from one of the cells above, we also created a tuple!"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Modifying objects that are used in multiple different places can have unintended side effects. Therefore it is sometimes preferable to just not do that 😀

    >💡 Generally it is quite safe to modify an object inside the cell where it is created but it is discouraged to modify an object in a different cell than the one where it was created. If you do it anyway then your result may depend on the order in which you execute cells. That can get really confusing 😵‍💫
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Dictionaries

    Dictionaries allow us to map a value to a key. The are not ordered but allow for easy access using e.g. an id.

    We use curly brackets to cerate a dict and square brackets to access elements.
    """
    )
    return


@app.cell
def _():
    user_info = {"Username": "RabotUser", "Consumption": 123}
    user_info
    return (user_info,)


@app.cell
def _(user_info):
    user_info["Username"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Functions

    Functions allow us to structure and reuse our code better. 

    - They start with the keyword `def` and have
    - a name,
    - a tuple of parameters,
    - a colon,
    - an optional `docstring` describing the function,
    - a block of code that is indented. Usually people use 1 tab = 4 spaces.
    """
    )
    return


@app.function
def say_hello(name):
    """Print personal greetings

    Parameters
        name: whom to greet.
    """

    print("Hello, " + name + "!")


@app.cell
def _():
    say_hello("World")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""You can find out more about a function by calling `help`. """)
    return


@app.cell
def _():
    help(say_hello)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In marimo you can also just

    - hover your cursor over a function or
    - click on the "view live docs" tool from the panel on on the left side of this page.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## There is much more

    - There is a lot more to Python please check out e.g. the [official beginners guide](https://docs.python.org/3/tutorial/index.html), in particular the [introduction section](https://docs.python.org/3/tutorial/introduction.html).
    - We often use frameworks beyond the standard library. We'll look at a first example in the next notebook: `1_churn_rates.py`


    """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
