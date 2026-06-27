import pandas as pd

df = pd.read_csv(
    'dataset/train.csv',
    encoding='latin1'
)

print(df.head())
print(df.info())