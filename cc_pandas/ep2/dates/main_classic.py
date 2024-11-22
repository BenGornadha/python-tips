import pandas as pd

data = {
    'name': ['John', 'Jane', 'John', 'Jake'],
    'date_of_birth': ['1990-01-01', '1992-02-02', '1990-01-01', '1993-03-03']
}

df = pd.DataFrame(data)

# Conversion des dates
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])

# Suppression des doublons
df = df.drop_duplicates()

print(df)