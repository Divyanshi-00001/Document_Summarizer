import yake

def extract_keywords(text, max_keywords=10):
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)
    return [kw[0] for kw in keywords[:max_keywords]]