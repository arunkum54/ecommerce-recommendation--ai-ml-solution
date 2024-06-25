import pandas as pd
from scipy.stats import ttest_ind

# Loading data
df = pd.read_csv('data/ab_test_interactions.csv')

# Separating into groups (assuming Group A and Group B)
group_A = df[df['group'] == 'A']
group_B = df[df['group'] == 'B']

# Calculating metrics (e.g., conversion rate)
conversion_rate_A = group_A[group_A['interaction'] == 'purchase'].shape[0] / group_A.shape[0]
conversion_rate_B = group_B[group_B['interaction'] == 'purchase'].shape[0] / group_B.shape[0]

# Performing t-test for conversion rate
t_stat, p_value = ttest_ind(group_A[group_A['interaction'] == 'purchase']['product_id'],
                            group_B[group_B['interaction'] == 'purchase']['product_id'])

# Printing results
print(f"Conversion Rate Group A: {conversion_rate_A:.2%}")
print(f"Conversion Rate Group B: {conversion_rate_B:.2%}")
print(f"T-statistic: {t_stat:.2f}, p-value: {p_value:.4f}")

# Example to interpreting results (adjust for your specific metrics and context)
if p_value < 0.05:
    print("Statistically significant difference found between groups.")
    if conversion_rate_B > conversion_rate_A:
        print("Group B performs better.")
    else:
        print("Group A performs better.")
else:
    print("No statistically significant difference found between groups.")
