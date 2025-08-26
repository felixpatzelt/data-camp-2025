import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Data-Camp Analysis 1: Churn Rates from a CSV

    Welcome to our first data analysis. 

    - Below we will load a csv file containing some columns from a sales & churn report.
    - We use the [pandas](https://pandas.pydata.org) library, which specialises in tabular and time-series data 🐼

    It is OK if you don't understand every detail right away. 

    - Try to follow the general ideas in the notebook until the end
    - Experiment with the code to figure out the rest
    - Try to use marimos built-in live docs and tooltips.
    - Refer to the [pandas documentation](https://pandas.pydata.org/docs/) for deeper questions.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Import our dependencies""")
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Optional exercise: find out how to read a csv file on your own.

    Pandas has a read_csv function.
    You can just call pd.read_csv with the path to the csv file you want to read.

    Can you figure this out on your own?

    If not, that is fine as well. The solution is given below
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Loading the CSV file (solution)""")
    return


@app.cell
def _(pd):
    def get_sales_report(file_path, filter_relocation_and_dunning=True):
        """Load & return the sales report csv

        Parameters:
            file_path:
                the file to read
            filter_relocation_and_dunning:
                sometimes a contract is cancelled but the user didn't churn
                this optional keyword arguent deterimnes if we filter out these cases
        """

        # to read the data, only this command is needed
        sales_report = pd.read_csv(
            file_path,
            # here we tell pandas that some columns contain dates and should be read as such
            parse_dates=["delivery_start", "cancellation_event_received_at"],
        )

        # filter special cases
        if filter_relocation_and_dunning:
            # ~ is a negation operator
            # square brackets select a column
            # .isin is a method that pandas provides to test
            # if the element in a cell is contained in a list
            # the result is a mask containint the values True or False
            mask_with_special_cancellation_reasons = ~sales_report[
                "cancellation_reason"
            ].isin(["CustomerRelocationRetained", "Dunning"])

            # pandas has very versitile selection and slicing operators
            # here we use .loc, which can accept the mask created above
            sales_report = sales_report.loc[mask_with_special_cancellation_reasons]

        sales_report["has_churned"] = (
            sales_report.cancellation_event_received_at
            > sales_report.delivery_start
        )
        return sales_report


    sales_report = get_sales_report("data/1_churn_rates_dummy_data.csv")
    sales_report
    return (sales_report,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Print some descriptive statistics""")
    return


@app.cell
def _(sales_report):
    sales_report.has_churned.mean()
    return


@app.cell
def _(sales_report):
    sales_report.has_churned.median()
    return


@app.cell
def _(sales_report):
    sales_report.has_churned.sem()  # sem = Standard Error of the Mean
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## We can group elements in our table and aggregate them

    If you know [SQL](https://en.wikipedia.org/wiki/SQL) This should seem conceptually familiar.
    """
    )
    return


@app.cell
def _(sales_report):
    sales_report.groupby("cancellation_reason", dropna=False).size()
    return


@app.cell
def _(sales_report):
    churn_by_attribution = sales_report.groupby(
        "attributed_channel_group", dropna=False
    ).has_churned.agg(["size", "mean", "sem"])
    return (churn_by_attribution,)


@app.cell
def _(churn_by_attribution):
    churn_by_attribution.round(4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Pandas has built-in visualisation

    Under the hood this uses another Python library called [Matplotlib](https://matplotlib.org) by default, which even allows for more advanced custom plots than we need here.
    """
    )
    return


@app.cell
def _(churn_by_attribution):
    churn_by_attribution["size"].sort_values(ascending=False).plot.bar()
    return


@app.cell
def _(churn_by_attribution):
    _plot_df = churn_by_attribution.sort_values("mean", ascending=False)
    _axis = _plot_df["mean"].plot.bar(yerr=2 * _plot_df["sem"])
    _axis.set_ylabel("Mean Churn Rate ± 2 SEM")
    _axis
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Marimo allows us to make cell outputs interactive

    This allows us to quickly experiment with our results. 

    Here, we can use it to improve our understanding of the effects of statistical uncertainty 🎲
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Simulate repeated experiments with variable sample sizes

    The sample size here is the number of random contracts drawn from the sales report that are used in the plot below.
    """
    )
    return


@app.cell
def _(mo, sales_report):
    sample_size_slider = mo.ui.slider(
        start=10,
        stop=len(sales_report),
        step=1,
        value=len(sales_report) // 3,
        label="Sample Size",
    )
    run_button = mo.ui.run_button(label="Draw another sample")
    mo.hstack([sample_size_slider, run_button])
    return run_button, sample_size_slider


@app.cell
def _(run_button, sales_report, sample_size_slider):
    run_button  # just mention it here to allow retriggering

    _plot_df = (
        sales_report.sample(
            sample_size_slider.value
        )  # this draws a random row from the sales report
        .groupby("attributed_channel_group", dropna=False)
        .has_churned.agg(["size", "mean", "sem"])
        .sort_values("mean", ascending=False)
    )
    _axis = _plot_df["mean"].plot.bar(yerr=2 * _plot_df["sem"])
    _axis.set_ylabel("Mean Churn Rate ± 2 SEM")
    _axis
    return


if __name__ == "__main__":
    app.run()
