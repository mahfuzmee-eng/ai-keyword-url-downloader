import requests
from pathlib import Path

def download(url: str, output_dir: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        filename = url.split("/")[-1] or "index.html"
        path = Path(output_dir) / filename

        with open(path, "wb") as f:
            f.write(response.content)

        print(f"[DOWNLOADED] {url}")

    except Exception as e:
        print(f"[FAILED] {url} → {e}")
