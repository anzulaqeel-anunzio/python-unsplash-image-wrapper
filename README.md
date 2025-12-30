# Unsplash Image Search Wrapper (Python)

A Python client for the Unsplash API to search for high-quality photos.

## Features

-   **Search Photos**: Find photos by query.
-   **Get Random Photo**: Fetch a random photo (optional filters).
-   **User Stats**: Get basic stats for a user (not fully implemented in boilerplate, but structure allows it).

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Install Package**
    ```bash
    pip install .
    ```

## Usage

```python
import os
from unsplash_wrapper import UnsplashClient
from dotenv import load_dotenv

load_dotenv()
access_key = os.getenv("UNSPLASH_ACCESS_KEY")

client = UnsplashClient(access_key=access_key)

# Search for "nature"
results = client.search_photos("nature", per_page=5)
for photo in results['results']:
    print(f"Photo by {photo['user']['name']}: {photo['urls']['regular']}")

# Get a random photo
random_photo = client.get_random_photo(query="ocean")
print(f"Random Ocean Photo: {random_photo['urls']['regular']}")
```

## Configuration

Obtain an Access Key from [Unsplash Developers](https://unsplash.com/developers).

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
