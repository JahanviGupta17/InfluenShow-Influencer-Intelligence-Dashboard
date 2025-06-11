import pandas as pd

def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)

    # Clean 60_day_eng_rate (% values to float)
    if "60_day_eng_rate" in df.columns:
        df["60_day_eng_rate"] = df["60_day_eng_rate"].astype(str).str.replace('%', '', regex=False)
        df["60_day_eng_rate"] = pd.to_numeric(df["60_day_eng_rate"], errors='coerce')

    # Clean followers (e.g., "15,000", "2.5k", "1.1m")
    if "followers" in df.columns:
        df["followers"] = df["followers"].astype(str).str.replace(',', '').str.lower()
        df["followers"] = df["followers"].str.replace('k', 'e3').str.replace('m', 'e6')
        df["followers"] = pd.to_numeric(df["followers"], errors='coerce')

    # Clean avg_likes, posts, new_post_avg_like, total_likes
    for col in ["avg_likes", "posts", "new_post_avg_like", "total_likes"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(',', '').str.lower()
            df[col] = df[col].str.replace('k', 'e3').str.replace('m', 'e6')
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df
