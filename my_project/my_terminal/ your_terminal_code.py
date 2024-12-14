import os
import requests

def get_github_repo_info(repo):
    url = f"https://api.github.com/repos/{repo}"
    response = requests.get(url)
    
    if response.status_code == 200:
        repo_info = response.json()
        return {
            "name": repo_info.get("name"),
            "description": repo_info.get("description"),
            "url": repo_info.get("html_url"),
            "stars": repo_info.get("stargazers_count"),
            "forks": repo_info.get("forks_count"),
        }
    else:
        return None

def main():
    # Замените 'your_github_username/your_repo_name' на ваш реальный репозиторий
    repo = 'your_github_username/your_repo_name'
    info = get_github_repo_info(repo)
    
    if info:
        print(f"Repository Name: {info['name']}")
        print(f"Description: {info['description']}")
        print(f"URL: {info['url']}")
        print(f"Stars: {info['stars']}")
        print(f"Forks: {info['forks']}")
    else:
        print("Failed to retrieve repository information.")

if __name__ == "__main__":
    main()

