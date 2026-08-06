# Stage12-N1-2 文書案内

## 現行文書

- [`stage12-n1-2-final.md`](stage12-n1-2-final.md)：統合完成稿。今後の参照・レビュー対象は原則これのみ。

## 監査履歴

Stage12-N1-2j〜2p、review R03〜R05、対応する監査スクリプト・JSONは、導出過程と査読修復の履歴として保持する。これらは統合稿と矛盾する場合、後続の統合稿を優先する。

## Actions運用

現行のレビュー用workflowは `.github/workflows/review-bundle.yml` の1本だけとする。Actionsから `Review bundle` を手動実行すると、`stage12-n1-2-final-review.md` がArtifactとして生成される。
