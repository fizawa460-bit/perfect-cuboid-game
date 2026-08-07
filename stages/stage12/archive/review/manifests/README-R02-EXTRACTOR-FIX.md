# Stage12-N1-2 review bundle R02 extractor compatibility

R01 remains immutable and contains the complete embedded research payload. Some AI readability extractors returned only the HTML `<main>` element, while the R01 bundle handshake was outside `<main>` in `<header>` and `<footer>`.

R02 preserves the same canonical research payload (`CONTENT_SHA256=201cad458d172e0939e5508b78e6e06abe894d908390f0c1b54c51a16e63d586`) and repeats the full handshake four times inside `<main>`:

- `START_OF_MAIN`
- `BEFORE_EMBEDDED_SOURCES`
- `AFTER_EMBEDDED_SOURCES`
- `END_OF_MAIN`

Current page after merge:

`review/PC-N1-2-PROOF-REVIEW-20260806-R02.html`
