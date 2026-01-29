import requests
import json
from datetime import datetime
import pytz # 한국 시간을 위해 필요

def get_benchmarks():
    url = "https://huggingface.co/api/models?sort=downloads&direction=-1&limit=5"
    response = requests.get(url)
    models = response.json()

    # 한국 시간 기준 현재 시각 생성
    korea_tz = pytz.timezone('Asia/Seoul')
    now = datetime.now(korea_tz).strftime('%Y-%m-%d %H:%M:%S')

    data = []
    for m in models:
        data.append({
            "name": m['id'],
            "downloads": m.get('downloads', 0),
            "last_updated": now # 모든 항목에 현재 수집 시간 기록
        })
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    get_benchmarks()
