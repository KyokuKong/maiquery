import httpx

def main():
    res = httpx.post("http://127.0.0.1:11663/api/v1/platform-binding", json={
        "platformId":"admin",
        "userId":10907518,
    })
    print(res.text)

if __name__ == "__main__":
    main()