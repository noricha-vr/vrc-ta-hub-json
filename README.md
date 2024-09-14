# VRChat TA Hub

Untranslated URL の問題に対応するため、
VRChat 技術学術系イベントHubのデータを取得して、Github Pagesで公開します。

## JSONデータ

- [community.json](./docs/community.json)
- [event.json](./docs/event.json) 過去の情報は表示しない
- [lt.json](./docs/lt.json) 過去の情報は表示しない

## データの取得元

- [VRChat技術学術系イベントHub](https://vrc-ta-hub.com/)

- 集会情報: <https://vrc-ta-hub.com/api/v1/community/>
- イベント情報: <https://vrc-ta-hub.com/api/v1/event/>　過去の情報は表示しない
- LT情報: <https://vrc-ta-hub.com/api/v1/event_detail/>　過去の情報は表示しない

## リポジトリ

- [vrc-ta-hub-json](https://github.com/noricha-vr/vrc-ta-hub-json)

データの取得は、`fetch_data.py`を実行しています。
