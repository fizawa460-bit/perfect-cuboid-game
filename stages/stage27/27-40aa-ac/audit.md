# Stage27 checkpoint40 aa/ab/ac consolidated audit

```text
AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT=PASS
CI_AUDIT=PASS
PR=1028
PR_MERGEABLE=true
PR_MERGED=true
MERGE_COMMIT=b60f35fcea451a53ab3dd193963d3c98066c1924
AUDIT_SCOPE=Stage27-40aa+Stage27-40ab+Stage27-40ac
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CONTINUE_UPPER_EXPLORATION_AFTER_PASS=true
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
ABSOLUTE_REPO_NATIVE_EXHAUSTIVENESS_CLAIMED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

The mathematical PASS previously assigned to 40aa/40ab/40ac is retained. The only failing item in the first re-audit was the dedicated Stage27-40aa CI path for archived Stage14 sources. Commit `440a8ee32b6253b1d39760d591e3052097ca7bf1` corrected the Stage14 archive paths, after which `Stage27-40aa MAIN CRT2 support attack` passed. The other Stage27-10/20/30/40 and r401a checks remained successful.

The audit therefore authorizes merge of PR #1028 but does not authorize checkpoint50. The three mandatory r401a continuations are accepted as executed, while the global upper remains `N2(B) <<_epsilon B^(1/2+epsilon)`. Checkpoint40 stays open for further upper-side exploration.
