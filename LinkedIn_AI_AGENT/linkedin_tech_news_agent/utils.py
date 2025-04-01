import random

def generate_linkedin_post(article):
    """
    Generate an engaging LinkedIn post for a tech article
    
    :param article: Dictionary containing article details
    :return: Formatted post content
    """
    hashtags = [
        '#TechInnovation', 
        '#FutureOfTech', 
        '#AITrends', 
        '#Technology', 
        '#Innovation'
    ]
    
    post_templates = [
        "🚀 Tech Innovation Spotlight 🌟\n\n"
        "{title}\n\n"
        "Key Insights:\n"
        "• Cutting-edge technology transforming our digital landscape\n"
        "• Potential impact on industry innovation\n\n"
        "Dive deeper: {url}\n\n"
        "{hashtags}",
        
        "💡 Breaking Tech News Alert 📡\n\n"
        "{title}\n\n"
        "Why It Matters:\n"
        "• Revolutionary approach in tech development\n"
        "• Potential game-changer for the industry\n\n"
        "Full Story: {url}\n\n"
        "{hashtags}"
    ]
    
    # Select random template and hashtags
    template = random.choice(post_templates)
    selected_hashtags = ' '.join(random.sample(hashtags, 3))
    
    return template.format(
        title=article['title'],
        url=article['url'],
        hashtags=selected_hashtags
    )