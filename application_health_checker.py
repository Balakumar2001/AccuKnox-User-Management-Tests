import requests

def check_application_health(url):
    try:
        response = requests.get(url, timeout=5)  # 5-second timeout
        if response.status_code == 200:
            print(f"✅ Application is UP | URL: {url} | Status Code: {response.status_code}")
        else:
            print(f"❌ Application is DOWN | URL: {url} | Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Application is DOWN | URL: {url} | Error: {e}")

if __name__ == "__main__":
    app_url = "https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=10216258730976413038&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9040240&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1"  # Replace with the actual URL to check
    check_application_health(app_url)
