
import pandas as pd
import numpy as np
df1 = pd.DataFrame({"Text1":[1, "Bob", "Teacher", 5, 100], "Text2":[2, 8, "Mary", "Mama", 50], "Text3":[3, "Pen", 24, "Woker", 15]})
print(df1)
def summ(df):
    df_numeric = df.apply(pd.to_numeric, errors="coerce")
    total_sum = df_numeric.sum().sum()
    print(total_sum)

print(summ(df1))