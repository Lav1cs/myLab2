"""Задачи второй части лабораторной: корреляционный анализ."""
from __future__ import annotations

from grader_contracts.correlation_tasks import BrainCorrelationSummary, BrainDataInput
from matplotlib import pyplot as plt

import pandas as pd
import seaborn as sns

def analyze_brain_correlations(data: BrainDataInput) -> BrainCorrelationSummary:
    """Проанализируйте brainsize.txt.

    Разделите наблюдения по полу и для каждой группы вычислите корреляции
    признаков FSIQ, VIQ, PIQ, Weight, Height с MRI_Count методом Пирсона.
    В strongest_mri_feature верните название признака с наибольшим модулем
    корреляции с MRI_Count среди объединённых результатов двух групп.
    """

    df = pd.read_csv(data.csv_path, sep='\t', na_values=['NA', 'N/A', ''])

    male = df[df['Gender'] == 'Male'].dropna(subset=['MRI_Count'])
    female = df[df['Gender'] == 'Female'].dropna(subset=['MRI_Count'])

    men_count = len(male)
    women_count = len(female)

    features = ['FSIQ', 'VIQ', 'PIQ', 'Weight', 'Height'] # признаки для кор

    men_corr = {}
    women_corr = {}

    for feat in features:
        men_corr[feat] = float(male[feat].corr(male['MRI_Count']))
        women_corr[feat] = float(female[feat].corr(female['MRI_Count']))

    men_women_corr = []

    for feat, corr in men_corr.items():
        men_women_corr.append((abs(corr), feat))
    for (feat, corr) in women_corr.items():
        men_women_corr.append((abs(corr), feat))

    sorted_corr = sorted(men_women_corr, key=lambda x: x[0], reverse=True)

    strongest_mri_feature = sorted_corr[0][1]

    return BrainCorrelationSummary(men_count,
                                   women_count,
                                   women_corr,
                                   men_corr,
                                   strongest_mri_feature
        )


# input_data = BrainDataInput('brainsize.txt')
# result = analyze_brain_correlations(input_data)
#
# print(result)