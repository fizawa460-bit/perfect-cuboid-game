# Stage14 H dispatch checklist

Use this checklist when a proof route emits a new auxiliary H/tH/sH request.

```text
[ ] H_NEEDED=true is justified by a named minimal receiver
[ ] H_REQUESTED_OBJECT is explicit
[ ] source stage and exact source SHA are recorded
[ ] target.md contains do-not-reopen items and all physical masks
[ ] target.md contains required verdict fields
[ ] blocking/nonblocking status is explicit
[ ] target is frozen when H starts
[ ] parent route will not rewrite this H after dispatch
[ ] later receiver needing audit will use the next H number
[ ] completed H result will be merged as a snapshot certificate
```

See `H-PROTOCOL.md` for the governing contract.
