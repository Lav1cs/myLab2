"""Задачи первой части лабораторной: Pandas и Titanic."""
from __future__ import annotations

import pandas as pd

from grader_contracts.pandas_tasks import TitanicInput, TitanicSummary


def analyze_titanic(data: TitanicInput) -> TitanicSummary:
    df = pd.read_csv(data.csv_path)

    row_count = len(df)
    missing_by_column = {col: int(n) for col, n in df.isna().sum().items()}
    adults_over_30_count = int((df["Age"] > 30).sum())

    mean_age = df.groupby("Pclass")["Age"].mean()
    mean_age_by_pclass = {int(k): float(v) for k, v in mean_age.items()}

    survival = df.groupby("Pclass")["Survived"].mean()
    survival_rate_by_pclass = {int(k): float(v) for k, v in survival.items()}

    highest_fares = [float(f) for f in df["Fare"].sort_values(ascending=False).head(5)]

    return TitanicSummary(
        row_count=row_count,
        missing_by_column=missing_by_column,
        adults_over_30_count=adults_over_30_count,
        mean_age_by_pclass=mean_age_by_pclass,
        survival_rate_by_pclass=survival_rate_by_pclass,
        highest_fares=highest_fares,
    )


if __name__ == "__main__":
    print(analyze_titanic(TitanicInput(csv_path="titanic.csv")))