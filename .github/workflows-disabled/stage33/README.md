# Stage33 archived Actions workflows

Historical Stage33 workflow definitions are retained here verbatim so they no longer auto-trigger on every PR synchronize event. GitHub Actions only discovers workflow files under `.github/workflows/`.

Current live Stage33 workflows stay under `.github/workflows/`. Restore an archived workflow there only when that leaf becomes active again, and give it a PR-scoped concurrency group with `cancel-in-progress: true`.
