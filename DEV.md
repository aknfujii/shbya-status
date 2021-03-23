# 入れたもの

## front

- `npx create-react-app`
- @material-ui/core @material-ui/icons
- (@theme-ui/presets)
- react-router-dom

## server

- pafy youtube-dl(pafy に必須)

# やること

-[x] 物体検知して混雑状況を把握してステータスを返す

```
{
    people: 10,
    capture: hoge.img,
    updated_at: 2021012910:00 +0900,
}
```
- ロギングにプログレスバー表示
- [x]NoSQLに変更
    - Firestore
- [x]shell scriptをどの場所でも実行可能にする
    - API
- footerをつける
    - footerに日時
- ページ遷移後、トップに戻ってこれるようにする
- [x] API serverをGCPに建てる
- 画面遷移後、cloudstorageから取ってきたgifを表示 or 過去データのチャート表示
- create_statusに認証
- [x]cronを実施
    - 成功の時は成功で返すようにする
    - ログが残ってないのでログが残ろうようにする
    - 実施状況の確認
- githubactionsにmasterのfrontを変更したらfrontをdeploy,serverを変更したらserverをdeploy(一緒にはしない)
- typescriptに変更
- tslint入れる
- frontの表示を中央寄せにする
- requiremens.txtの整理 


# deploy
```bash
# front
gcloud builds submit --config front/cloudbuild.yaml front
# server
cd server
gcloud app deploy
# cron
gcloud app deploy cron.yaml
```