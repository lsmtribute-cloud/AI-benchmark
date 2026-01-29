import requests
import json
from datetime import datetime
import pytz

def clean_model_name(full_id):
    """
    모델 ID를 읽기 쉬운 이름으로 변환하는 함수
    예: 'meta-llama/Meta-Llama-3-8B' -> 'Llama 3 (8B)'
    """
    parts = full_id.split('/')
    if len(parts) == 2:
        org, name = parts[0], parts[1]
    else:
        return full_id

    # 유명한 모델 이름 정리
    if 'llama' in name.lower():
        return name.replace('Meta-Llama-', 'Llama ').replace('-', ' ').replace('.', ' ').strip()
    elif 'deepseek' in name.lower():
        return f"DeepSeek {name.split('-')[-1].upper()}"
    elif 'gemma' in name.lower():
        return f"Google Gemma {name.split('-')[-1]}"
    elif 'qwen' in name.lower():
        return f"Qwen {name.split('-')[-1]}"
    elif 'mistral' in name.lower() or 'mixtral' in name.lower():
        return name.replace('-', ' ').replace('v0.1', '').strip()
    
    return name.replace('-', ' ').replace('_', ' ')

def get_realtime_trends():
    # 🔥 핵심: 모델을 10개(limit=10) 가져옵니다.
    url = "https://huggingface.co/api/models?sort=trending&direction=-1&limit=10"
    response = requests.get(url)
    models = response.json()

    korea_tz = pytz.timezone('Asia/Seoul')
    now = datetime.now(korea_tz).strftime('%Y-%m-%d %H:%M')

    data = []
    for m in models:
        friendly_name = clean_model_name(m['id'])
        
        data.append({
            "name": friendly_name,   
            "full_name": m['id'],    
            "likes": m.get('likes', 0),
            "downloads": m.get('downloads', 0),
            "last_updated": now
        })
    
    # data.json에 저장
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    get_realtime_trends()
