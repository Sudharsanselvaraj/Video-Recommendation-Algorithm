import requests
headers = {
    "Flic-Token": "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"
}
def fetch_data(url):
    print(f"Fetching data from: {url}")
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("Data fetched successfully!")
            data = response.json()
            return data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            print(f"Response content: {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
posts_url = 'https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000'
users_url = 'https://api.socialverseapp.com/users/get_all?page=1&page_size=1000'
posts_data = fetch_data(posts_url)
users_data = fetch_data(users_url)
if posts_data:
    print("Fetched Posts Data:", posts_data)
else:
    print("Failed to fetch posts data.")
    
if users_data:
    print("Fetched Users Data:", users_data)
else:
    print("Failed to fetch users data.")
