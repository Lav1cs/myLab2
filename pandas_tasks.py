"""Задачи первой части лабораторной: Pandas и Titanic."""
from __future__ import annotations

import pandas as pd

from grader_contracts.pandas_tasks import TitanicInput, TitanicSummary


def analyze_titanic(data: TitanicInput) -> TitanicSummary:
    """Выполните загрузку и анализ датасета Titanic.

    Нужно: посчитать пропуски, число пассажиров старше 30 лет, средний возраст
    и долю выживших по классам, а также пять наибольших тарифов по убыванию.
    """

    df = pd.read_csv(data.csv_path)


    row_count = len(df)

    missing_by_column= df.isna().sum().to_dict()

    adults_over_30_count = int((df["Age"].dropna() > 30).sum())

    mean_age_by_pclass = df.groupby("Pclass")["Age"].mean()


    survival_rate_by_pclass = df.groupby("Pclass")["Survived"].mean()


    highest_fares = list(df["Fare"].sort_values(ascending=False).head(5))
    



    raise NotImplementedError




input_data = TitanicInput(csv_path="titanic.csv")

result = analyze_titanic(input_data)
print(result)