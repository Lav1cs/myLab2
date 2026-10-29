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
    # highest_fares1 = (df.sort_values(by="Fare", ascending=False)[["Fare"]].head(5))

    # male_female_count = df.groupby("Sex")["PassengerId"].count()
    #
    # survived = df[df["Survived"] == 1]
    # survival_count = (survived.groupby("Sex")["PassengerId"]).count()
    #
    # kids = df[df['Age'] < 18]
    #
    # groub_dead_kids = kids.groupby('Survived')['Age'].count()
    #
    # found_jack = df.loc[(df['Age'] < 25) & (df['Age'] > 17) & (df['Sex'] == 'male') & (df['Survived'] == 0) & (df['Pclass'] == 3), ['Name', 'Fare']]
    #
    # sex_payment = df.groupby('Sex')['Fare'].mean()
    #
    #
    # female = (df['Sex'] == 'female').sum()
    # male = (df['Sex'] == 'male').sum()
    #
    # sex_classes = (df.groupby(['Sex', 'Pclass'])['Fare'].count() / male) * 100



    raise NotImplementedError

#df.loc - используется для нахождение значения по ключу
# df.loc[df["Age"].notna(), "Name"] - вывод имен у людей, у кого есть age

# df.sort_values(df["Age", "Name"], ascending=[True, False])

# mdf = pd.DataFrame(index=df.index)
# mdf['evenId'] = mdf['PassengerId'].apply(lambda x: x%2 == 0) - создание
# новой колонки с флагом четности


input_data = TitanicInput(csv_path="titanic.csv")

result = analyze_titanic(input_data)
print(result)