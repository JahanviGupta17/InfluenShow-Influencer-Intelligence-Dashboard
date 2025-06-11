# InfluenShow-Influencer-Intelligence-Dashboard
# 📊 Influencer Intelligence Dashboard

The **Influencer Intelligence Dashboard** is a user-friendly, interactive data visualization tool built with **Streamlit** and **Plotly**. It enables brands, marketers, and researchers to explore, analyze, and segment influencers from public data to support better decision-making for campaign planning and partnerships.

---

## 🚀 Features

### 1. 📈 Metrics Overview
Displays key summary metrics:
- **Total Influencers**: Total number of influencers in the dataset.
- **Total Reach**: Sum of followers across all influencers.
- **Average Engagement Rate**: Mean 60-day engagement rate.
- **High Performers**: Count of influencers with >5% engagement.

### 2. 🧩 Influencer Segmentation
Classifies influencers into:
- **Nano**: <10K followers
- **Micro**: 10K–100K
- **Macro**: 100K–1M
- **Mega**: >1M

Also displays a bar chart showing the distribution of influencers across these segments.

### 3. 🔍 Discovery Filters
Lets users filter influencers based on:
- **Country**
- **Domain** (e.g., fashion, fitness, tech)
- **Follower Range**
- **Engagement Rate Range**

Filtered influencers are displayed in a dynamic table.

### 4. 🎯 Offer Personalization Analysis
Analyzes the types of campaign offers influencers are aligned with, such as:
- Sponsored posts
- Product reviews
- Giveaways
Displayed as an interactive pie chart.

### 5. 🏆 Influence & Brand Fit Score Ranking
Calculates and ranks influencers by:
- **Influence Score** = followers × engagement rate
- **Brand Fit Score** = 0.8 × influence score
Top influencers are displayed in a sortable table.

### 6. 🤖 AI-Powered Influencer Suggestions
Smart recommendations based on:
- Selected **Target Domain**
- Entered **Target Audience**

Returns the top 5 influencers most aligned by engagement rate.

### 7. 📊 Advanced Visual Analytics
Includes:
- **Radar Chart**: For top influencers based on likes, engagement, and influence score.
- **Bubble Plot**: Shows relationship between followers, engagement, and likes per influencer.
- *(More charts can be added as needed)*

--- ###Demo WebApp
![demo]("C:\Users\pg385\OneDrive\Pictures\Screenshots\Screenshot 2025-06-11 213538.png")
![demo]()
![demo]()
![demo]()
![demo]()
![demo]()
![demo]()
![demo]()

## 💡 How to Run

1. Install requirements:
```bash
pip install -r requirements.txt
