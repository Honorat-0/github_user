import requests

user_name = "openai"

URL = f"https://api.github.com/users/{user_name}"

response = requests.get(URL, timeout=15)

status = response.status_code

if status == 200:
    print(f"Request pass with status {status}")
    req_json = response.json()
    user_name = req_json["login"]
    followers = req_json["followers"]
    public_repos = req_json["public_repos"]
    print(f"{user_name} has {followers} followers and {public_repos} public repos.")


    repos_response = requests.get(f"{URL}/repos", timeout=15)
    repo_response_stat = repos_response.status_code 


    if repo_response_stat == 200:
    
        repos = repos_response.json()

        if len(repos):
            
            if len(repos) == public_repos:
                print(f"\nList of all repos ({public_repos}) with their number of stars:\n")
            else:
                print(f"\nShowing {len(repos)} repos of {public_repos} public repos:\n")

            for repo in repos:
                print(f"The repo name = {repo["name"]} with {repo["stargazers_count"]} stars.")
        else:
            print(f"{user_name} doesn't have a repo.")

    else:
        print(f"Request failed with status {status}")

else:
    print(f"Request failed with status {status}")


