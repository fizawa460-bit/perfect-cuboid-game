# Stage32-18AJ — d16 b16 promote 18AI scout winner

18AI raced three exact algorithms on representative walls `(436,5)` and `(922,13)` under one matrix with `max-parallel: 6`. The exact summary artifact from run `33124686161` is `9668228265`, digest `sha256:487e3c8d5e8ef9b1947ca520f421b07415032cd170c0ceb1f6a644f039b1fb03`. Its winner is `baseline`.

18AJ therefore returns to the clean 18AF scheduler-1.0 certifier and promotes that exact algorithm to all six unresolved b16 walls:

- `(436,5)`, `(436,362)`
- `(503,118)`, `(503,665)`
- `(922,13)`, `(922,38)`

The run remains x1024 with primary split coordinate 54 and secondary split coordinate 48. No finer split is authorized. The purpose is a resource-safe exact production pass after the algorithm race, not theorem credit.

The six production jobs live in one matrix with `max-parallel: 6`. Each gets node cap 18,000,000 and wallclock 45 minutes. Job success is not interpreted as exact completion: compact JSON status and the final summary are authoritative.

All numerical/global/theorem/receiver/controller firewalls remain false until exact global aggregation is separately established.
