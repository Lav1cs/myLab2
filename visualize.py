from __future__ import annotations

from correlation_tasks import analyze_brain_correlations
from grader_contracts.correlation_tasks import BrainCorrelationSummary, BrainDataInput
from matplotlib import pyplot as plt

import pandas as pd
import seaborn as sns


df = pd.read_csv('brainsize.txt', sep='\t', na_values=['NA', 'N/A', ''])

plt.figure(figsize = (8, 6))
sns.heatmap(df[['FSIQ', 'VIQ', 'PIQ', 'Weight', 'Height', 'MRI_Count']].corr(),
            annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

input_data = BrainDataInput('brainsize.txt')
strongest_mri_feature = analyze_brain_correlations(input_data).strongest_mri_feature


sns.scatterplot(data=df, x=strongest_mri_feature, y='MRI_Count', hue='Gender')  # замените VIQ на strongest_mri_feature
plt.show()