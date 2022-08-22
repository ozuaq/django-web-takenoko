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

### git
#### **非追跡ファイル設定**
以下、2つ書き方は同じ <br>
- 開発メンバ共通で非追跡にしたいファイルの非追跡設定 <br>
.gitignoreに書く <br>
例）.DS_Store, \_\_pycache__
- 個人的なファイルの非追跡設定<br>
.git/info/excludeに書く <br>
例）sample.py
