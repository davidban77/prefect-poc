import httpx
from prefect import flow


@flow(log_prints=True)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    url = f"https://api.github.com/repos/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    repo = response.json()
    print(f"{repo_name} repository statistics 🤓:")
    print(f"Stars 🌠 : {repo['stargazers_count']}")
    print(f"Forks 🍴 : {repo['forks_count']}")


if __name__ == "__main__":
    get_repo_info.from_source(
        "https://github.com/davidban77/prefect-poc.git",
        entrypoint="flows/repo_info.py:get_repo_info",
    ).deploy(name="repo-info", work_pool_name="netpanda-k3s", build=False, push=False)
