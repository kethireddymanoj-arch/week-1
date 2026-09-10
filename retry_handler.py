import requests
from tenacity import retry, stop_after_attempt, wait_exponential


class RateLimitError(Exception):
    pass


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    reraise=True
)
def get_data(url):
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 429:
            print("Rate limit reached. Retrying...")
            raise RateLimitError("Too many requests")

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)
        raise


if __name__ == "__main__":
    url = "https://httpbin.org/get"

    try:
        data = get_data(url)
        print("Data received successfully")
        print(data)

    except Exception as error:
        print("Could not get data:", error)