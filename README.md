# GitHub User

A small practice script I wrote while learning Python and APIs. It takes a GitHub username and prints the account's number of followers, its number of public repos, and each repo's name with its number of stars.

## Requirements and how to run

Requires Python and the `requests` library (`pip install requests`).

1. Open `github_user.py` and set the `user_name` line at the top to the GitHub username you want.

## Example user_name

```Python
user_name = "Honorat-0"
```
2. Run `github_user.py`.

## Example output

```
Request pass with status 200
Honorat-0 has 0 followers and 6 public repos.

List of all repos (6) with their number of stars:

The repo name = admin-dashboard with 0 stars.
The repo name = deadzone with 0 stars.
The repo name = findzi with 0 stars.
The repo name = library with 0 stars.
The repo name = mini-message with 0 stars.
The repo name = neon-dash with 0 stars.

```

## Limits (what I'd change)

- It shows only the first 30 repos, because GitHub returns long lists one page at a time. Planned: fetch every page.
- It crashes on network errors and timeouts. Only HTTP status codes are handled.
- GitHub allows 60 unauthenticated requests per hour per IP address, and each run of the script uses 2.