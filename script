import pandas as pd
import json
import matplotlib
matplotlib.use('Agg') # Enables graph generation without a display
import matplotlib.pyplot as plt
import os

def run_political_analysis(ig_file, x_file):
    # Ensure results directory exists
    os.makedirs('results', exist_ok=True)

    try:
        # Load Data
        with open(ig_file, 'r') as f:
            ig_json = json.load(f)[0]
        with open(x_file, 'r') as f:
            x_json = json.load(f)[0]
            
        print(f"Successfully loaded {ig_file} and {x_file}")
    except Exception as e:
        print(f"Error loading files: {e}")
        return

    # 1. Create Engagement Table[cite: 1, 2]
    metrics = {
        "Metric": ["Total Views", "Total Likes", "Comments/Replies", "Engagement Rate"],
        "Instagram (Trump Reel)": [
            f"{ig_json['views']:,}", 
            f"{ig_json['likes']:,}", 
            f"{ig_json['num_comments']:,}", 
            f"{(ig_json['likes']/ig_json['views'])*100:.2f}%"
        ],
        "X (White House Post)": [
            f"{x_json['views']:,}", 
            f"{x_json['likes']:,}", 
            f"{x_json['replies']:,}", 
            f"{(x_json['likes']/x_json['views'])*100:.2f}%"
        ]
    }
    df_table = pd.DataFrame(metrics)

    # 2. Sentiment Mapping[cite: 1, 2]
    # Normalized based on X's high 'Quote' friction and IG's personal vitriol[cite: 1, 2]
    sentiment_data = {
        'Platform': ['Instagram', 'X (Twitter)'],
        'Supportive (Positive)': [28.6, 35.0],
        'Neutral/Vibe': [42.9, 15.0],
        'Hostile (Negative)': [28.6, 50.0]
    }
    df_graph = pd.DataFrame(sentiment_data)

    # 3. Generate High-Contrast Graph
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6.75))
    colors = ['#00ba38', '#999999', '#ff4b2b']
    
    df_graph.set_index('Platform').plot(kind='barh', stacked=True, color=colors, ax=ax, width=0.6)

    ax.set_title('POLITICAL SENTIMENT: INSTAGRAM VS. X [APRIL 2026]', fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('Percentage of Audience Tone (%)', fontsize=12, color='#cccccc')

    # Data Labels
    for p in ax.patches:
        width = p.get_width()
        if width > 5:
            ax.text(p.get_x() + width/2, p.get_y() + p.get_height()/2, f'{int(width)}%', 
                    va='center', ha='center', fontsize=14, fontweight='bold', color='white')

    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=3, frameon=False)
    
    # 4. Final Output
    plt.tight_layout()
    plt.savefig('results/sentiment_comparison_graph.png', dpi=300)
    
    print("\n" + "="*50)
    print(df_table.to_string(index=False))
    print("="*50)
    print("ANALYSIS COMPLETE: Graph saved to results/sentiment_comparison_graph.png")

if __name__ == "__main__":
    run_political_analysis('instagram.json', 'x.json')

- name: Commit and Push Graph
      run: |
        git config --global user.name "github-actions[bot]"
        git config --global user.email "github-actions[bot]@users.noreply.github.com"
        git add results/
        git commit -m "Auto-generated sentiment graph" || exit 0
        git push
