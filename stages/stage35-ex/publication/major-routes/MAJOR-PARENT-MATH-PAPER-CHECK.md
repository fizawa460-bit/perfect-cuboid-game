# Stage35EX｜継承する主要親証明の限定数学監査（2026-11-09）

**判定：PARTIAL_PASS_EXACT_ALGEBRA_AND_ENDPOINTS / PARENT_THEOREMS_NOT_FULLY_AUDITED。** 出典本文の単なる転記は監査と別。今回実際に独立計算した範囲と、現時点で依存している数学的な親前提を明示する。

## 1. C195の実際の倍算点の初等代数：直接確認 PASS

[E:y²=x(x−A²)(x+C²)](proofs/C195-canonical-source.md)でa=A²,c=C²,D²=ac、(u,v)∈E、v²=u(u−a)(u+c)とする。倍算の平方表示の必要恒等式

```text
(u²+ac)² − 4a·u(u−a)(u+c) = (u²−2au−ac)²
(u²+ac)² + 4c·u(u−a)(u+c) = (u²+2cu−ac)²
```

はSymPyで両辺を展開し、差がいずれも0と独立検算した。したがって元のactual倍算点のx、x−A²、x+C²の三平方への代数的接続は矛盾しない。これは任意のE上の点に対する「その点自身のr,p,qの三平方」ではなく、**元の倍算点**の公式である。

## 2. C195のJ/Kのℓ付値・役割 bound：初等部分を論理確認

C195の正の補平方 `T_n=b²−Z²=Y²`、`gcd(Z,b)=1`、`gcd(b,2ABC)=1`から、p|bではp∤Z,Y、R=BZ, S=BYがp-unit、整数U=bp,V=bqも`U²=A²b²+R²`,`V²=C²b²−R²`によりp-unitである。J=UV+RS、K=UV−RSの和2UVはp-unit、積`JK=(Db²)²`のp付値は4v_p(b)だから、`{v_p(J),v_p(K)}={4v_p(b),0}`。この部分は初等整数付値として独立確認した。

rs=tと置けば`0<t<B²/2`（正の有理r,sかつr²+s²=B²）。`J=sqrt(D²+t²)+t`と`C²=A²+B²`から`J<C²`が従う。よって`1<M/N=sqrt(J/D)<sqrt(C/A)`は同じcanonical分解が成立する場合に整合する。

**未再監査**：p|DのS237 formal depthが一様に`v_p(J)=v_p(K)=v_p(D)`を与える全素数・2進の場合分け、C174の20,856基底を含む一様高さ入力、S268のreduced norm全証明、S289/S290のglobal four-root/Q∞転送の全証明。これらを今回の二つの初等代数検算のPASSから自動的に昇格させない。

## 3. C195のN=1排除に使う数値係数：有理計算一致

旧C174の実際のPに対して`lambda>0`,`432lambda≥c_E`、さらに`log C<c_E/16`、actualの高さ誤差`|h_x−2hhat|≤c_E/3`を**仮定**すると、C195本文の式

```text
log b − 1/2 log(C/A)
  > 4 n² lambda − 25 c_E/96
  ≥ c_E (n²/108 − 25/96)
```

となり、n=6で右端は`7c_E/96>0`。25/96は`1/6+1/16+1/32`、n²/108は`4n²/432`であることを独立計算した。**その前提の一様高さ定理そのものは未監査**で、最終の物理解排除を新規に得たわけではない。

## 4. R2/C189の155/197：有理端点を独立Fraction/SymPyで確認

[R2証明](proofs/R2-uniform-thresholds.md)の二次式について

| 値 | 独立計算結果 |
|---|---|
| Q4(154) | −266408/54525 |
| Q4(155) | 104425/4362 |
| Q1(196) | −1176986/54525 |
| Q1(197) | 724039/109050 |

を正確に再現。正側で増加する二次式の閾値としては整合する。**未再監査**：C174/C175のλ*一様下界、旧C185 protected TOPの十分条件の全証明、S270のprime-to-root割当の全数学証明、R0 C189の旧数値コード全再実行。したがってMID/HIGHの相関上界やBranch B閉鎖は主張しない。

## 5. 連鎖C196〜C200・LOW・−30の扱い

[C196〜C200](C196-C200-DEPENDENCY-REVIEW.md)は成立条件・失効NEXTの資料間突合は済んだが、Jacobian-isogeny核・Prym/dual4・16次被覆の数学的独立再検算はまだ行っていない。[LOW P112](P112-RESIDUAL-RECONCILIATION.md)は整数指数集合の再計算を行っただけで、C181/R5-C212/S264およびrow367/368/369/376の親全称証明は継承する。−30のrow385〜393の高次数算術・局所unit code・relation matrixを今回全再実行したという主張もしない。

**結論**：C195とR2のボトルネック周辺の簡明な恒等式・係数はPASS。ただし「継承する親証明の数学的妥当性を全件独立確認済み」という判定は不可。次に必要な独立監査はS237の全formal-depth分岐、C174の全基底高さ根拠、S268/S269/S289/S290の前提適用、R2のprime-to-root・height主要補題である。

[移植要件](MIGRATION-COMPLETION-CHECKLIST.md) · [row393一次文献ゲート](ROW393-PRIMARY-THEOREM-GATE.md)
