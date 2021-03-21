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
- NoSQLに変更
    - Firestore
- shell scriptをどの場所でも実行可能にする
    - API
- footerをつける
- ページ遷移後、トップに戻ってこれるようにする
- API serverをGCPに建てる

# flow
```bash
./DL.sh <== 何かトリガーで実行する <== mp4が作られる
http://localhost:3000
```
