def detect_content_domain(df):
    def get_domain(row):
        bio = str(row.get('channel_info', '')).lower()
        if 'fitness' in bio:
            return 'Fitness'
        elif 'beauty' in bio or 'makeup' in bio:
            return 'Beauty'
        elif 'fashion' in bio:
            return 'Fashion'
        elif 'tech' in bio:
            return 'Tech'
        return 'General'

    df['content_domain'] = df.apply(get_domain, axis=1)
    return df
