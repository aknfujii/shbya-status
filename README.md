# 概要
- 渋谷スクランブル交差点のライブストリーミングを物体検知　人数と傘の数を表示
- https://shbya-status.web.app

# 構成
- front
    - React
    - インフラ: Firebase
- server
    - Flask
    - 物体検知: 教師データ利用 opencv
    - インフラ: GAE, CloudScheduler(cron)
- database: Firestore
- CD: CloudBuild

# 別構成
- branch: flask_ver
- front
    - React
- server
    - Flask
    - 物体検知: 教師データ利用 opencv
- database: sqlite(SQLAlchemy)