import requests

# LeetCode's single GraphQL endpoint
LEETCODE_URL = "https://leetcode.com/graphql" # this is the API endpoint (the address we send requests to)

def fetch_user_stats(username):
    """Fetch a user's solved-problem counts by difficulty from LeetCode."""

    # The GraphQL query: we describe EXACTLY the data we want back
    query = """
    query userStats($username: String!) {
        matchedUser(username: $username) {
            username
            submitStatsGlobal {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
    }
    """

    # Variables plug into the query ($username above)
    variables = {"username": username}

    # Send a POST request with the query + variables as JSON
    response = requests.post(
        LEETCODE_URL,
        json={"query": query, "variables": variables},
        headers={"Referer": "https://leetcode.com"}  # LeetCode requires this
    )

    # Turn the JSON response into a Python dictionary
    data = response.json()
    return data



def get_clean_stats(username):
    """Return solved counts as a simple dict: {'All': 140, 'Easy': 53, ...}"""
    raw = fetch_user_stats(username)

    # Safety: if username is wrong, matchedUser comes back as None
    user = raw.get("data", {}).get("matchedUser")
    if user is None:
        return None  # user not found

    # Dig out the list and flatten it into a clean dict
    submissions = user["submitStatsGlobal"]["acSubmissionNum"]
    clean = {}
    for item in submissions:
        clean[item["difficulty"]] = item["count"]

    return clean

# Quick test: run this file directly to see your own data
if __name__ == "__main__":
    result = get_clean_stats("Krina_Paghadar")
    print(result)
