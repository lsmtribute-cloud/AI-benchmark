import requests
import json
import os

def get_benchmarks():
    # 실제로는 특정 API나 크롤링 대상 URL을 넣습니다.
    # 여기서는 예시로 Hugging Face의 인기 모델 데이터를 가져오는 구조입니다.
    url = "https://huggingface.co/api/models?sort=downloads&direction=-1&limit=5"
    response = requests.get(url)
    models = response.json()

    data = []
    for m in models:
        data.append({
            "name": m['id'],
            "downloads": m.get('downloads', 0),
            "last_updated": m.get('lastModified', '')
        })
    
    # 결과를 data.json 파일로 저장
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    get_benchmarks()
