def extract_keywords(text: str) -> list:
    """
    Extract important keywords from text.
    Simple implementation using word frequency.
    """
    words = text.lower().split()
    common_words = set([
        "and", "or", "the", "a", "an", "to", "of",
        "in", "on", "for", "with", "is", "are"
    ])

    keywords = [word for word in words if word not in common_words]

    return list(set(keywords))[:20]
