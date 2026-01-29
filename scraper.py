name: Daily AI Data Scrape

on:
  schedule:
    - cron: '0 0 * * *' # 매일 한국 시간 오전 9시 실행
  workflow_dispatch:   # 수동으로도 실행 가능하게 설정

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install requests
      - name: Run Scraper
        run: python scraper.py
      - name: Commit and Push
        run: |
          git config --global user.name "Auto-Scraper"
          git config --global user.email "actions@github.com"
          git add data.json
          git commit -m "Update benchmark data" || exit 0
          git push
