import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def _(pd):
    def get_sales_report(file_path, filter_relocation_and_dunning=True):
        """Load & return the sales report csv"""
        sales_report = pd.read_csv(
            file_path,
            parse_dates=["delivery_start", "cancellation_event_received_at"],
        )

        if filter_relocation_and_dunning:
            sales_report = sales_report.loc[
                ~sales_report["cancellation_reason"].isin(
                    ["CustomerRelocationRetained", "Dunning"]
                )
            ]

        sales_report["has_churned"] = (
            sales_report.cancellation_event_received_at
            > sales_report.delivery_start
        )
        return sales_report


    sales_report = get_sales_report("../sales_report_subset.csv.zip")
    sales_report
    return (sales_report,)


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
    sales_report.has_churned.sem()
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


@app.cell
def _(churn_by_attribution):
    churn_by_attribution["size"].sort_values(ascending=False).plot.bar()
    return


@app.cell
def _(churn_by_attribution):
    _plot_df = churn_by_attribution.sort_values("mean", ascending=False)
    _plot_df["mean"].plot.bar(yerr=2 * _plot_df["sem"])
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
    run_button  # just to retrigger

    _plot_df = (
        sales_report.sample(sample_size_slider.value)
        .groupby("attributed_channel_group", dropna=False)
        .has_churned.agg(["size", "mean", "sem"])
        .sort_values("mean", ascending=False)
    )
    _plot_df["mean"].plot.bar(yerr=2 * _plot_df["sem"])
    return


if __name__ == "__main__":
    app.run()
