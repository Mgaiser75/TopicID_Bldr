import requests

def scrape_youtube(q):
    return [{"title": f"YouTube result for {q}", "score": 0.92}]

def scrape_reddit(q):
    return [{"thread": f"Reddit discussion on {q}", "score": 0.88}]

def scrape_google(q):
    return [{"snippet": f"Google search result for {q}", "score": 0.77}]

def scrape_amazon(q):
    return [{"product": f"Amazon result for {q}", "score": 0.82}]

def run_engine(query, mode="multi"):
    out = {"query": query, "engine": []}
    out["engine"].extend(scrape_youtube(query))
    out["engine"].extend(scrape_reddit(query))
    out["engine"].extend(scrape_google(query))
    out["engine"].extend(scrape_amazon(query))
    return out
