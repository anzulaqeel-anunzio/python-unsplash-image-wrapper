# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import requests

class UnsplashClient:
    BASE_URL = "https://api.unsplash.com"

    def __init__(self, access_key: str):
        """
        Initialize the Unsplash client.
        :param access_key: Your Unsplash Access Key.
        """
        if not access_key:
            raise ValueError("Access Key is required.")
        self.access_key = access_key
        self.headers = {
            "Authorization": f"Client-ID {self.access_key}",
            "Accept-Version": "v1"
        }

    def _make_request(self, endpoint: str, params: dict = None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def search_photos(self, query: str, page: int = 1, per_page: int = 10):
        """Search for photos."""
        return self._make_request("/search/photos", params={
            "query": query,
            "page": page,
            "per_page": per_page
        })

    def get_random_photo(self, query: str = None, count: int = 1):
        """Get a random photo."""
        params = {"count": count}
        if query:
            params["query"] = query
        return self._make_request("/photos/random", params=params)

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
