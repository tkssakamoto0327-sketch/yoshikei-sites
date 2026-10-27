# yoshikei-sites

ヨシケイの公開サイト（献立表・メニューブック・レシピ帳）をまとめたリポジトリ。**ここが唯一の正本**です（デスクトップの upload フォルダは今後使いません）。

| フォルダ | 公開先 | 中身 |
|---|---|---|
| `kondate/` | https://yoshikei-kondate.pages.dev/ | 献立表（`data.js` と `pdf/`） |
| `menubook/` | https://yoshikei-menubook.pages.dev/ | Webメニューブック（`index.html` の `ALL_WEEKS`、号フォルダ `wMMDD/`、特集 `sp/`） |
| `recipe/` | https://yoshikei-recipe.pages.dev/ | レシピ帳（`data.js` の `COURSES`、写真 `photos/`） |

## 公開のしくみ
- `kondate/`・`menubook/`・`recipe/` のどれかに変更が入ると、GitHub Actions が変更のあったサイトだけを Cloudflare Pages に公開します（1〜2分）。公開後、本番URLに反映されたかも自動で確かめます。
- 手動で公開し直したいときは、GitHub の「Actions」タブ → 対象のワークフロー → 「Run workflow」。
- 必要な Secrets：`CLOUDFLARE_API_TOKEN`（Cloudflare Pages: Edit 権限）、`CLOUDFLARE_ACCOUNT_ID`。

## 古いファイルの片付け
期限切れの号フォルダや古い献立PDFは、このリポジトリから削除すれば、次の公開でサイトからも消えます。
