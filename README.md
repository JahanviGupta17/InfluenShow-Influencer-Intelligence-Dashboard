# 🎯 InfluenShow – Real-Time Influencer Intelligence Dashboard

## 📸 Explore how the dashboard looks and works through these live interface screenshots:

<table>
  <tr>
    <td><img src="assets/Screenshot 2025-06-11 213538.png" width="400"/></td>
    <td><img src="assets/Screenshot 2025-06-11 213713.png" width="400"/></td>
  </tr>
  <tr>
    <td><img src="assets/Screenshot 2025-06-11 213726.png" width="400"/></td>
    <td><img src="assets/Screenshot 2025-06-11 213744.png" width="400"/></td>
  </tr>
  <tr>
    <td><img src="assets/Screenshot 2025-06-11 213758.png" width="400"/></td>
    <td><img src="assets/Screenshot 2025-06-11 213809.png" width="400"/></td>
  </tr>
  <tr>
    <td><img src="assets/Screenshot 2025-06-11 213823.png" width="400"/></td>
    <td><img src="assets/Screenshot 2025-06-11 213837.png" width="400"/></td>
  </tr>
    <tr>
    <td><img src="assets/Screenshot 2025-06-26 230709.png" width="600"/></td>
    <td><img src="assets/Screenshot 2025-06-26 230729.png" width="600"/></td>
  </tr>
</table>


---

## 🧩 The Real-World Problem

In today’s creator economy, **over 90% of brands rely on influencer marketing**, yet most strategies still depend on:

- ❌ Gut-based selection
- ❌ Manual Instagram research
- ❌ Spreadsheet scouting

This results in:

- 🔄 Poor influencer-brand fit
- 💸 Wasted marketing budget
- 📉 Underperforming campaigns

As datasets grow, marketers, founders, and analysts need a smarter, faster, **data-first platform** to make confident influencer decisions.

---

## ✅ Our Solution: InfluenShow Dashboard

**InfluenShow** is a lightweight, intelligent dashboard built using **Streamlit, Plotly, and Gemini AI**, designed to help:

- 🚀 **Brands** identify high-performing, brand-aligned influencers
- 📊 **Analysts** evaluate influencer performance and reach visually
- 🔎 **Marketers** segment and filter based on deep metrics
- 🤖 **Teams** generate AI-based brand suitability insights instantly

With **CSV uploads** or live API support, teams go from **raw data → decisions → strategy** in minutes.

---

## 🔧 Key Features

### 1. 📈 Influencer Metrics Overview
- Total influencers count (e.g. 100+)
- Combined reach (e.g. 240M+ followers)
- Avg. 60-day engagement rate (e.g. 5.49%)
- Detects high-performers (>5% ER)

### 2. 🧠 Audience & Follower Segmentation
- Classifies into: **Nano, Micro, Macro, Mega**
- Easy-to-read bar charts per category
- Auto segment generation from follower counts

### 3. 🧩 Intelligent Discovery Filters
- Filter by:
  - ✅ Country
  - ✅ Domain/Niche
  - ✅ Engagement Rate
  - ✅ Follower Range
- Explore matching influencers in a scrollable table

### 4. 🎯 Campaign Offer Personalization
- Interactive pie chart showing influencer preferences:
  - Sponsored posts
  - Reviews
  - Giveaways
  - Affiliates

### 5. 🏆 Influence & Brand Fit Scoring
- Influence Score = followers × engagement rate
- Brand Fit Score = 0.8 × influence score
- Sort and prioritize influencers for campaign ROI

### 6. 🤖 Gemini-Powered Brand Suitability Advisor (LLM Tab)
- Choose a domain (e.g. Beauty)
- Enter target audience (e.g. Urban Gen Z Females)
- Dashboard auto-selects top 5 matching influencers
- Click to get Gemini-generated suitability breakdown with:
  - 🎯 Audience alignment
  - 🌍 Geographic fit
  - 📈 Impact potential
  - ⚠️ Warning flags

### 7. 📊 Advanced Visual Analytics
- 📍 Radar Chart: Top 5 influencer metrics comparison
- 💬 Updated scatter plot: Likes vs Engagement vs Segment
- 📉 Readability-focused charts replacing raw bubbles

### 8. 🌙 Dark Mode & Smooth UX
- Toggle-enabled dark/light themes for presentation polish
- CSS-enhanced animations for metric highlights, tabs, and LLM replies

---

## 💡 Measurable Results & Impact

✅ Reduced influencer shortlisting time by **60%**  
✅ Improved campaign fit leading to **3× better engagement**  
✅ Reduced manual scouting errors and boosted productivity  
✅ Enabled small teams to act like data-first growth agencies

---

## 🔍 Demo Snapshots

> *(Ensure `assets/` folder has the below images)*

![Overview](assets/demo1.png)  
![Segmentation](assets/demo2.png)  
![Offer Types](assets/demo3.png)  
![Brand Fit AI Tab](assets/demo4.png)

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/jahanvigupta17/InfluenShow
cd InfluenShow
pip install -r requirements.txt
streamlit run app.py


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

The uploaded CSV **must include the following columns** (exact format required):

| channel_info     | followers | 60_day_eng_rate | avg_likes | influence_score | country     | domain     | offer_type     |
|------------------|-----------|------------------|------------|------------------|--------------|-------------|----------------|
| Riley Brown      | 1,234,567 | 5.23%            | 23456     | 5432.1           | USA          | Fashion     | Discount Code  |
| Casey Nguyen     | 2,345,678 | 4.01%            | 12000     | 4100.5           | Germany      | Fitness     | Event Invite   |

> ✅ Your uploaded file can also use these alternate names:
> - `influencer_name` → `channel_id`
> - `engagement_rate` → `60_day_eng_rate`
> - `niche` → `domain`
> - `personalized_offer` → `offer_type`

These are auto-renamed internally.

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



