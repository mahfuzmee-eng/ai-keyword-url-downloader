from duckduckgo_search import DDGS

def search_urls(query: str, max_results: int = 5) -> list:
    urls = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            urls.append(r["href"])
    return urls
