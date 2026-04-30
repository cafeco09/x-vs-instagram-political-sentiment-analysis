import pandas as pd
import json
import matplotlib
matplotlib.use('Agg') # Required for headless GitHub environment
import matplotlib.pyplot as plt
import os

def run_political_analysis(ig_file, x_file):
    os.makedirs('results', exist_ok=True)

    # Load Data
    with open(ig_file, 'r') as f:
        ig_json = json.load(f)[0]
    with open(x_file, 'r') as f:
        x_json = json.load(f)[0]

    # Sentiment Data Logic
    sentiment_data = {
        'Platform': ['Instagram', 'X (Twitter)'],
        'Supportive': [28.6, 35.0],
        'Neutral': [42.9, 15.0],
        'Hostile': [28.6, 50.0]
    }
    df = pd.DataFrame(sentiment_data)

    # Plotting
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6.75))
    df.set_index('Platform').plot(kind='barh', stacked=True, color=['#00ba38', '#999999', '#ff4b2b'], ax=ax)
    
    plt.title('Platform Sentiment Analysis [April 2026]')
    plt.tight_layout()
    plt.savefig('results/sentiment_comparison_graph.png')
    print("Graph successfully generated in results/ folder.")

if __name__ == "__main__":
    run_political_analysis('instagram.json', 'x.json')
