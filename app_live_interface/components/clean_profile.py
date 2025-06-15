def clean_columns(df):
    df['followers'] = (
        df['followers'].astype(str)
        .str.replace(',', '', regex=False)
        .str.extract(r'(\d+)', expand=False)
        .astype(float)
    )
    return df
