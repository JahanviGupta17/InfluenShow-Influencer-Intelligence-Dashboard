import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a fast and free model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def build_influencer_context(profile):
    return f"""
Influencer Profile:
- Username: @{profile.get("channel_id", "N/A")}
- Domain: {profile.get("domain", "N/A")}
- Followers: {profile.get("followers", "N/A")}
- Country: {profile.get("country", "N/A")}
- Average Likes: {profile.get("avg_likes", "N/A")}
- Engagement Rate: {profile.get("60_day_eng_rate", "N/A")}
- Offer Type: {profile.get("offer_type", "N/A")}
"""

def get_brand_suitability(context, target_domain, target_audience, model_name=None):
    try:
        # Use default model if none provided
        if model_name is None:
            model_name = "models/gemini-1.5-pro"

        # Load the Gemini model
        model = genai.GenerativeModel(model_name)

        # Construct prompt
        prompt = f"""
You are a brand strategist AI.

Based on the following influencer profile, analyze their **brand suitability** for a campaign targeting **{target_audience}** in the **{target_domain}** niche.

Be brief and highlight:
- Alignment with audience
- Type of content
- Potential for impact

---

{context}
        """

        # Generate response
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Gemini Error: {e}"
