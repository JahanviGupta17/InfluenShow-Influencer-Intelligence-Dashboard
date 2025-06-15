def calculate_metrics(df):
    total_influencers = df.shape[0]
    total_reach = df["followers"].sum()
    avg_eng_rate = df["60_day_eng_rate"].mean()
    high_performers = df[df["60_day_eng_rate"] > 4].shape[0]

    return {
        "total_influencers": total_influencers,
        "total_reach": total_reach,
        "avg_eng_rate": avg_eng_rate,
        "high_performers": high_performers
    }
