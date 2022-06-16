import numpy as np
import pandas as pd
import scipy.stats as stats

def mannwhitneyu_for_df(df, class_column, value_column, alpha = 0.05):
    categories = df[class_column].unique()
    df_tmp = pd.DataFrame([], columns=["Categorie_A", "Categorie_B", "p_value"])
    for idx, cat_a in enumerate(categories):
        for cat_b in categories[idx:]:
            _stats, p = stats.mannwhitneyu(df[df[class_column]==cat_a][value_column],
                                          df[df[class_column]==cat_b][value_column])
            df_tmp.loc[len(df_tmp)] = [cat_a, cat_b, p]
    # bonferroni correction
    alpha = alpha / len(df_tmp)
    df_tmp["Significant"] = df_tmp["p_value"] < alpha
    return df_tmp

def effectsize_for_df(df, class_column, value_column):
    df_effect_size = pd.DataFrame([], columns=["Categorie_A", "Categorie_B", "Effect_Size"])
    styles = df[class_column].unique()
    for idx, style_a in enumerate(styles):
        for style_b in styles[idx + 1:]:
            style_a_data = df[df[class_column] == style_a][value_column]
            style_b_data = df[df[class_column] == style_b][value_column]
            effect_size = cohend(style_a_data, style_b_data)
            df_effect_size.loc[len(df_effect_size)] = [style_a, style_b, effect_size]
    return df_effect_size

def cohend(d1, d2) -> float:
    # calculate the size of samples
    n1, n2 = len(d1), len(d2)
    # calculate the variance of the samples
    s1, s2 = np.var(d1, ddof=1), np.var(d2, ddof=1)
    # calculate the pooled standard deviation
    s = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    # calculate the means of the samples
    u1, u2 = np.mean(d1), np.mean(d2)
    # return the effect size
    return (u1 - u2) / s