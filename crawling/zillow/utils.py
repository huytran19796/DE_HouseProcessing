from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

URL = "https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22California%22%2C%22mapBounds%22%3A%7B%22west%22%3A-124.2779624765625%2C%22east%22%3A-114.62098005468751%2C%22south%22%3A32.6550292679444%2C%22north%22%3A40.31046513605901%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A9%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D&wants={%22cat1%22:[%22listResults%22,%22mapResults%22],%22cat2%22:[%22total%22]}&requestId=5"

setting_for_airflow = {
   'BOT_NAME': 'zillow',
   'DOWNLOAD_DELAY': 10,
   'FEED_EXPORT_ENCODING': 'utf-8',
   'NEWSPIDER_MODULE': 'zillow.spiders',
   'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
   'SPIDER_MODULES': ['zillow.spiders'],
   'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor',
   'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
   "ITEM_PIPELINES": {
      "zillow.pipelines.ZillowPipeline": 1,
   }}

def cookies_parser():
    cookie_string = 'x-amz-continuous-deployment-state=AYABeKZnlQeSO+ev8eWp5OjlnTgAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADMnxhtzcjIoLJ6PBjQAwEVHoSbf4BN6fy3YvLkr9cHszO8kl+PJhRXHJoo9QDX9oAQyanhynwSVviuYvA2llAgAAAAAMAAQAAAAAAAAAAAAAAAAAAOvKqAJLhBSW7+4o%2FRa0jW7%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwW3OTgCpyzh2HxlDGU+o+PE+lViv99VSMBaRY5; zguid=24|%2414325deb-9819-4f7d-909a-056e3bb880b5; zgsession=1|e082b403-3b98-4dbf-8f80-6fc308bd6906; x-amz-continuous-deployment-state=AYABeJcLjVLyF3jtIXaPnvDNMKkAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADG3q%2FXwr4VjtkRdSWwAwhQ3yKT8c1a%2Fq7UkpSOytdSeuiHae6BLUcsBHbYNNqzV1JzAPn9LOh2CQVn9551F0AgAAAAAMAAQAAAAAAAAAAAAAAAAAAKzYxW2%2FAkYcy8EWOaQ5utT%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxk%2FyboiGFz7eh+GAOeRzT6yIxeLOkfsvru18S0T6yIxeLOkfsvru18Sw==; _ga=GA1.2.1514011060.1692589271; _gid=GA1.2.84509151.1692589271; zjs_anonymous_id=%2214325deb-9819-4f7d-909a-056e3bb880b5%22; zjs_user_id=null; zg_anonymous_id=%22da427d5d-886d-4364-b1e6-7b671766db55%22; _gcl_au=1.1.1504572024.1692589271; DoubleClickSession=true; _hp2_id.1215457233=%7B%22userId%22%3A%221382902985447561%22%2C%22pageviewId%22%3A%225420064718313391%22%2C%22sessionId%22%3A%227540295824609103%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; pxcts=90adc5aa-3fd4-11ee-8b31-68754c554f52; _pxvid=90adb44f-3fd4-11ee-8b31-8ef4c74408a0; tfpsi=f2a75549-67c2-483e-b4a9-721b389d3f5c; _hp2_ses_props.1215457233=%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1692589271025%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; _fbp=fb.1.1692589276233.1247892380; _clck=1fip929|2|fec|0|1328; _pin_unauth=dWlkPU5tWm1PR05tTldNdE56bGhNUzAwTURrNUxUazBOR010WTJFNU5qQmhNamsyWVdZMQ; JSESSIONID=3BE54589FDE3D7E4D317707EAAC482BE; __gads=ID=e66db6a519c9f7de:T=1692589281:RT=1692589281:S=ALNI_MZL4vBKveuuiX43EwGR9dx5lSDucw; __gpi=UID=00000c3027547387:T=1692589281:RT=1692589281:S=ALNI_MaWPx_7EnLgqHeklhHkmVtHiuI7lA; _uetsid=950242803fd411ee94c03750ea2a7a3d; _uetvid=950236f03fd411eea6eb7f1c3a2e49d4; AWSALB=C+DHRF4U0PTNmu+o5doIeIpDGuDRVidVxkhqB9bVboXO5hm6KdmfGsud7m2HxaL3Eig0slv0L+Ax0YpAosqZa3ADh5H1j9oWVKMoXyJkloc8iRvC0e8/zsoG2a5O; AWSALBCORS=C+DHRF4U0PTNmu+o5doIeIpDGuDRVidVxkhqB9bVboXO5hm6KdmfGsud7m2HxaL3Eig0slv0L+Ax0YpAosqZa3ADh5H1j9oWVKMoXyJkloc8iRvC0e8/zsoG2a5O; search=6|1695181478605%7Crect%3D25.949007869779425%252C-80.1190500961914%252C25.45652001387422%252C-80.56880290380859%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0912700%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09; _px3=671dcf8369ffb3370536b133a38472f5b416eb59bc1e2f5972ca8041293aa0de:ragvAdu/tLe7/AeKoSx+HTFUafmuM2i90fZX3CO1yJIkW/q3ZC16KnuK47apOvA6fwEYMu9WPJRGBbANOM3KXg==:1000:5+H4qTOXoMPKZ9WP/EIHsn01nXoHAqz+Iy7tQFt1nwfPOcgXmnR+moL2SCb3e1FcGYjwvqAUdDyDwfIMAzmNTxcmWeXxVJ9iyjaXRH7FJbJ8cLIHazuuDyEGV+2q2rGWzYvQIPHYxNGarhrJ9H5dQ65uTI6308extQBoK3yzVVgSlX96AMudXQKgSc2VTrYsG9t5ELKB+9evzdd9xCVwkQ==; _clsk=dmfsoh|1692590303023|8|0|x.clarity.ms/collect; _gat=1'
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies

def parse_new_url(url, page_number):
    url_parsed = urlparse(url)
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {"currentPage": page_number}
    query_string.get('searchQueryState')[0] = search_query_state

    encode_qs = urlencode(query_string, doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encode_qs}"
    return new_url