# components/insight_generator.py

import pandas as pd

def convert_social_counts(val):
    try:
        if isinstance(val, str):
            val = val.lower().replace(",", "").strip()
            if val in ['', 'unknown', 'unnown', 'na', 'n/a']:
                return None
            if 'k' in val:
                return float(val.replace('k', '')) * 1_000
            elif 'm' in val:
                return float(val.replace('m', '')) * 1_000_000
            else:
                return float(val)
        return float(val)
    except (ValueError, TypeError):
        return None

def clean_engagement_string(val):
    try:
        if isinstance(val, str):
            val = val.replace('%', '').strip()
            return float(val) if val else None
        return float(val)
    except:
        return None

def generate_derived_features(df):
    df['avg_likes'] = df['avg_likes'].apply(convert_social_counts)
    df['followers'] = df['followers'].apply(convert_social_counts)

    df['avg_likes'] = pd.to_numeric(df['avg_likes'], errors='coerce')
    df['followers'] = pd.to_numeric(df['followers'], errors='coerce')

    if '60_day_eng_rate' in df.columns:
        df['60_day_eng_rate'] = df['60_day_eng_rate'].apply(clean_engagement_string)

    df['engagement_quality'] = df['avg_likes'] / df['followers'].replace(0, pd.NA)
    df['engagement_quality'] = df['engagement_quality'].fillna(0)

    df['influence_score'] = 0.7 * df['avg_likes'].fillna(0) + 0.3 * df['followers'].fillna(0)
    df['fake_follower_score'] = 100 - (df['engagement_quality'] * 100).clip(upper=100)

    return df
