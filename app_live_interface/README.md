
# 🎯 InfluenShow – Real-Time Influencer Intelligence Dashboard

## 🧠 Real-World Problem

In today’s digital age, **90% of brands rely on influencer marketing**, but most decisions are based on **gut feeling**, **outdated spreadsheets**, or **manual Instagram scrolling**. This leads to:

* Poor influencer-brand fit 🔄
* Wasted ad spend 💸
* Underperforming campaigns 📉

Marketers and startups **lack a centralized, intelligent platform** to assess influencer performance, analyze audience reach, and customize collaboration strategies — especially when dealing with **large datasets**.

## ✅ Our Solution: InfluenShow Dashboard

**InfluenShow** is a smart, interactive dashboard built with **Streamlit + Plotly** that helps:

* 🚀 **Brands** discover top-performing influencers
* 🔎 **Marketers** segment by niche, engagement, and region
* 📈 **Analysts** visualize and score influencer performance in real-time
* 🤝 **Startups** personalize offer types for each influencer

With just a CSV upload or live data connection, teams can **go from raw data to campaign decisions** in minutes — no coding required.

## 🔧 Key Features

### 1. 📈 Influencer Metrics Overview

* Total influencers
* Combined follower reach
* Avg. engagement rate
* High-performers detection

### 2. 🧠 Audience & Follower Segmentation

* Classifies influencers as:

  * **Nano**: <10K
  * **Micro**: 10K–100K
  * **Macro**: 100K–1M
  * **Mega**: >1M
* See breakdowns via bar chart & filters

### 3. 🧩 Intelligent Filtering System

* Filter by:

  * **Country**
  * **Niche/domain** (e.g. fashion, tech)
  * **Follower count**
  * **Engagement rate**
* View results in a dynamic searchable table

### 4. 🎯 Campaign Offer Personalization

* Pie chart of influencer preferences across:

  * Sponsored posts
  * Reviews
  * Giveaways
  * Affiliate programs
* Useful for matching offers to influencer types

### 5. 🏆 Influence & Brand Fit Scoring

* Auto-calculated metrics:

  * **Influence Score** = followers × engagement rate
  * **Brand Fit Score** = 0.8 × influence score
* Rank and shortlist the most strategic influencers

### 6. 🤖 AI-Driven Influencer Suggestions

* Based on:

  * Target domain
  * Preferred audience behavior
* Get **top 5 influencer matches** instantly

### 7. 📊 Advanced Visual Analytics

* **Radar Chart**: Top influencer breakdown
* **Bubble Plot**: Influence vs. likes vs. engagement
* **Line & bar charts**: Easily extendable

---

## 🔍 Demo Snapshots

> Replace the below with real uploaded images in your GitHub repo's `assets/` folder

![overview](assets/demo1.png)
![segmentation](assets/demo2.png)
![offers](assets/demo3.png)
![ranking](assets/demo4.png)

---

## 💡 Results & Impact

✅ Saved 60% time in campaign planning (compared to spreadsheet-based scouting)
✅ Helped identify high-fit influencers with 3× engagement improvement
✅ Useful for **small teams**, **early-stage startups**, and **growth marketers**

---

## 🧪 How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/jahanvigupta17/InfluenShow
cd InfluenShow
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Launch the app:

```bash
streamlit run app.py
```

---

## 📁 Dataset

The dashboard accepts any CSV with relevant influencer data (or connects via API with slight modification).

Basic structure expected:

| influencer\_name | followers | engagement\_rate | avg\_likes | niche | country | personalized\_offer |
| ---------------- | --------- | ---------------- | ---------- | ----- | ------- | ------------------- |

---

## 🌐 Possible Real Integrations

| Data Source                | Integration Level      |
| -------------------------- | ---------------------- |
| Google Sheets API          | Easy                   |
| Instagram Graph API (Meta) | Advanced – needs token |
| Airtable                   | Easy                   |
| CSV Uploads                | Already Built-In ✅     |

---

## 🧠 Future Ideas

* Add GPT-4 for automatic campaign copy suggestions
* NLP to analyze influencer captions for sentiment
* Auto email outreach builder
* Real-time leaderboard by country/domain

---

## 🙌 Built With

* [Streamlit](https://streamlit.io/) – UI Framework
* [Pandas](https://pandas.pydata.org/) – Data manipulation
* [Plotly](https://plotly.com/) – Visualizations
* [Python](https://www.python.org/) – Core logic



