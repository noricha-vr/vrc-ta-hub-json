import requests
import json


if __name__ == '__main__':
    # 指定されたURL
    urls = {
        'community': 'https://vrc-ta-hub.com/api/v1/community/?format=json',
        'event': 'https://vrc-ta-hub.com/api/v1/event/?format=json',
        'lt': 'https://vrc-ta-hub.com/api/v1/event_detail/?format=json',
    }
    for name, url in urls.items():
        # URLからデータを取得する
        response = requests.get(url)

        # 正常な応答であるか確認する
        response.raise_for_status()

        # JSONデータを取得する
        data = response.json()

        # JSONデータをファイルに保存する
        with open(f'docs/{name}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"JSONデータを{name}.jsonに保存しました。")
