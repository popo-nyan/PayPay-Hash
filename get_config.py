import hashlib
import hmac
from typing import Optional
import httpx

HMAC_SECRET_KEY = "717198a8bcf3405384abcb4815d1efb9"
CLIENT_NAME = "android-pp"


def hash_calculating(http_method: str,
                     endpoint: str,
                     payload: Optional[str] = "") -> str:
    return hmac.new(key=HMAC_SECRET_KEY.encode(),
                    msg=str(http_method + "|" + endpoint + "|" + "x-requester" + ":" + CLIENT_NAME + "|" + payload).encode(),
                    digestmod=hashlib.sha256).hexdigest()


response = httpx.get(url="https://push-config.paypay.ne.jp/v1/config",
                     headers={
                         "Host": "push-config.paypay.ne.jp",
                         "Content-Type": "application/json",
                         "Cache-Control": "no-cache",
                         "X-Requester": CLIENT_NAME,
                         "User-Agent": "okhttp/4.11.0",
                         "hash": hash_calculating("GET", "/v1/config")})
print(response, response.json())
