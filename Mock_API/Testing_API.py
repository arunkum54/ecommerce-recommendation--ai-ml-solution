import requests

def fetch_content_version(version):
    url = f'http://127.0.0.1:5000/api/content/{version}'
    response = requests.get(url)
    if response.status_code == 200:
        content = response.json()
        return content['content']
    else:
        print(f"Failed to fetch content version {version}: {response.status_code}")
        return None

if __name__ == "__main__":
    versions = ['A', 'B', 'C']
    for version in versions:
        content = fetch_content_version(version)
        if content:
            print(f"Content Version {version}: {content}")
