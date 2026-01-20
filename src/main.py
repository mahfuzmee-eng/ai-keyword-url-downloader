from search.keyword_expander import expand
from search.web_search import search_urls
from downloader.file_downloader import download
import yaml
from pathlib import Path

def main():
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    keyword = input("Enter search keyword: ")

    expanded_keywords = expand(keyword)

    all_urls = set()
    for k in expanded_keywords:
        urls = search_urls(k, config["search"]["max_results"])
        all_urls.update(urls)

    output_dir = config["download"]["output_dir"]
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for url in all_urls:
        download(url, output_dir)

if __name__ == "__main__":
    main()
