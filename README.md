# Django-web-Takenoko
## 開発メモ
### セットアップ
```
docker compose up --build
```
- --build <br>
イメージのビルドから始めてコンテナを起動 <br>
→ ビルド処理の変更をイメージに反映させたいときに付ける

### 開発のときに使うコマンド
#### **サーバをフォアグラウンドで起動**
```
docker compose up
```
- ソースコードの変更は反映される
#### **コンテナ内のbashに入る**
```
docker compose up -d && docker compose exec web bash
```
1. **コンテナをバックグラウンドで起動**
```
docker compose up -d
```
- -d <br>
コンテナをバックグラウンドで起動
2.  **コンテナ内のbashに入る**
```
docker compose exec web bash
```
例）bashに入ってからpythonファイルを実行
```
python sample.py
```
3. **コンテナの停止**
```
docker compose stop
```