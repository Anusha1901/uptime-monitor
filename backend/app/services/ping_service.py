import time

import httpx


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


def ping_url(url: str):
    """
    Ping a URL and return:
    - status code
    - response time (ms)
    - whether the URL is up
    - error message (if any)
    """

    try:

        start = time.perf_counter()

        response = httpx.get(
            url,
            headers=HEADERS,
            timeout=10,
            follow_redirects=True,
        )

        end = time.perf_counter()

        return {
            "status_code": response.status_code,
            "response_time": round((end - start) * 1000, 2),
            "is_up": response.status_code < 400,
            "error_message": None,
        }

    except httpx.TimeoutException:

        return {
            "status_code": None,
            "response_time": None,
            "is_up": False,
            "error_message": "Request timed out",
        }

    except httpx.ConnectError:

        return {
            "status_code": None,
            "response_time": None,
            "is_up": False,
            "error_message": "Connection failed",
        }

    except httpx.RequestError as exc:

        return {
            "status_code": None,
            "response_time": None,
            "is_up": False,
            "error_message": str(exc),
        }

    except Exception as exc:

        return {
            "status_code": None,
            "response_time": None,
            "is_up": False,
            "error_message": str(exc),
        }