
---

# Political Sentiment Analysis: Instagram vs. X (Twitter)

## Project Overview
This repository contains a comparative data analysis of the same political discourse themes—specifically the "Two Kings" / "Golden Age" narrative—as they manifest on different social media platforms[cite: 1, 2]. By analyzing engagement metrics and linguistic sentiment, this project highlights how platform architecture dictates the "temperature" of political conversation[cite: 1, 2].

## Key Data Insights (April 2026)

| Metric | Instagram (@realdonaldtrump) | X (@WhiteHouse) |
| :--- | :--- | :--- |
| **Reach (Views)** | 697,562[cite: 1] | 22,481,283[cite: 2] |
| **Engagement (Likes)** | 89,081[cite: 1] | 154,533[cite: 2] |
| **Interaction (Comments)** | 6,676[cite: 1] | 25,403[cite: 2] |
| **Engagement Rate** | ~12.7% (Loyalty-driven)[cite: 1] | ~0.7% (Reach-driven)[cite: 2] |

## Sentiment & Tone Comparison

### 📸 Instagram: The "Loyalty Bubble"
*   **Tone**: Highly emotive and symbolic[cite: 1].
*   **Support**: Expressed through repetitive strings of heart (❤️‍🩹), crown (👑), and fire (🔥) emojis[cite: 1].
*   **Critique**: Negative sentiment is visceral but often disjointed, utilizing extreme metaphors like "parasitic infestation" and "mafia"[cite: 1].

### 🐦 X (Twitter): The "Rhetorical Battleground"
*   **Tone**: Institutional, provocative, and argumentative[cite: 2].
*   **Friction**: Characterized by a high "Quote-to-Repost" ratio (9,778 quotes vs. 17,910 reposts), indicating that the audience is largely engaging in "ratioing" or secondary debate[cite: 2].
*   **Narrative**: The "TWO KINGS" branding triggers intense rhetorical conflict, with a normalized hostility rate of approximately 50%[cite: 2].

## Repository Structure
*   `data/`: Contains the raw JSON datasets (**sd_molrk7n714qld1w5q0.json** and **sd_molrn7ts1y5da9suv.json**)[cite: 1, 2].
*   `results/`: Generated visualizations and summary tables.
*   `sentiment_analysis_report.py`: The Python script used to process the data and render the "Twitter-ready" sentiment graph.

## How to Reproduce
1. Ensure you have Python installed with `pandas` and `matplotlib`.
2. Run the analysis script:
   ```bash
   python sentiment_analysis_report.py
   ```
3. Check the `results/` folder for the updated sentiment comparison graph.

## Summary Findings
The data suggests that **Instagram** users interact like a celebrity fan base (or anti-fan base), leading to a highly polarized but less argumentative environment[cite: 1]. Conversely, **X** users interact as political combatants, resulting in a discourse dominated by narrative-setting and high-friction rhetorical engagement[cite: 2].
```
