# Workflow cleanup note

この整理では、Stage12-N1-2 の完成ルートに直接対応していた次の専用workflowを廃止した。

- Stage12-N1-2l hypothesis audit
- Stage12-N1-2m iterated Selberg–Delange audit
- Stage12-N1-2n coupled-region audit
- Stage12-N1-2o analytic-closure audit
- Stage12-N1-2p final-bookkeeping audit
- R04 review bundle
- R05 review bundle

代替は `.github/workflows/review-bundle.yml` の1本である。古い研究段階の再現用スクリプト・JSON・文書は削除せず、履歴として保持する。
