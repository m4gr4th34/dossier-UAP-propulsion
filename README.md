# UAP Propulsion

**An Open Dossier: a living, executable, publicly audited research record.**
*Don't trust this paper — run it.*
Irfan Ali-Khan · Independent Researcher · 2026

### 📖 Live preview (work in progress)
> **This dossier is an active pre-release draft — not yet released, no version asserted.** Only **Section 1** (Track A — within known physics) and the **claim ledger** are built; the interactive console, audit trail, and PDF are not. Shared early so the ideas can be read and discussed as they develop.

▶ **[Read the self-explaining edition — Section 1](https://m4gr4th34.github.io/dossier-UAP-propulsion/paper.html)** · [Claim ledger (the object of sign-off)](https://m4gr4th34.github.io/dossier-UAP-propulsion/ledger.html)

### ✦ [Publish your own like this →](https://github.com/m4gr4th34/open-dossier-template/blob/main/GETTING-STARTED.md)  — free template, ~20 minutes, no LaTeX or web skills needed

[![claims: verified](https://github.com/m4gr4th34/dossier-UAP-propulsion/actions/workflows/verify.yml/badge.svg)](https://github.com/m4gr4th34/dossier-UAP-propulsion/actions/workflows/verify.yml)
<!-- After Zenodo release, paste your DOI badge here:
[![DOI](https://zenodo.org/badge/REPOID.svg)](https://doi.org/10.5281/zenodo.XXXXXXX) -->

> **Status: PRE-RELEASE WORKING DRAFT — review build, not released.** No version
> number is asserted; no release, DOI, or timestamp. Built so far: **Section 1**
> (Track A — within known physics) in [`paper.html`](paper.html), four executable
> checks (A01–A04) in [`verification/verify_numbers.py`](verification/verify_numbers.py),
> and the readable [`ledger.html`](ledger.html). Not yet built: the interactive
> console, the audit trail, and the formal PDF. Track B / exploratory-conjecture
> material is intentionally absent until that label is written into the doctrine.

## Companion dossier

**Companion dossier: Global energy is not conserved in an FRW universe** (repo: [`dossier-energy-not-conserved`](https://github.com/m4gr4th34/dossier-energy-not-conserved)) — DOI: **[TO BE LINKED ON RELEASE]**. Distinct research lineages live in separate repos; where they cross-pollinate they cross-cite by DOI, never merged.

## What this is

A research dossier on UAP propulsion, shipped as a versioned repository in the
**Open Dossier format**: every quantitative claim is executable and checked under
CI, every revision is versioned, and the adversarial review ships with the work.

> _TODO (research phase): replace this with the paper's abstract — the core
> claim, why it's interesting, and the headline result — ending with_
> **Don't trust this paper — run it.**

## Publish your own

This repository uses the **Open Dossier format** — executable claims under CI, a
self-explaining edition, published adversarial review and dated amendments, and
auto-DOI'd, blockchain-timestamped releases. It all comes from a free template:

**→ [open-dossier-template](https://github.com/m4gr4th34/open-dossier-template/blob/main/GETTING-STARTED.md)** — roughly twenty minutes from idea to a live, archived, verifiable publication. No journal, no gatekeeper, no fees.

## Read it

- **Living paper (start here):** https://m4gr4th34.github.io/dossier-UAP-propulsion/
- **Self-explaining edition:** https://m4gr4th34.github.io/dossier-UAP-propulsion/paper.html
- **Audit trail** (red team, citation audit, live checks): https://m4gr4th34.github.io/dossier-UAP-propulsion/dossier.html
- **PDF:** [`paper/manuscript.pdf`](paper/manuscript.pdf) _(added during the research phase)_

## Run it

```bash
python3 verification/verify_numbers.py
```

The checks recompute every number in the manuscript from its stated assumptions
and exit nonzero on any failure. CI runs this on every commit — the badge above
is the paper's claims passing, continuously. The same checks run in your browser
on the living-paper page.

## Review it

This repository **is** the review venue. To referee this dossier:

1. Run the checks; push any explorer past its stated ranges.
2. Read the red-team report under [`verification/`](verification/) — findings published, not hidden.
3. **[File an issue](../../issues) against any claim** — cite the claim id from [`claim_ledger.csv`](claim_ledger.csv) if possible. Disagreement is a contribution. Every response is versioned; nothing is memory-holed.

## Priority & ownership

Attribution is preserved by the record itself, not by gatekeepers:

- **Git history** — every contribution hashed, attributed, and ordered.
- **Tagged releases + Zenodo DOI** — each version archived at CERN with a permanent citable identifier.
- **OpenTimestamps** — release hashes anchored in the Bitcoin blockchain: institution-free, cryptographic proof of priority.

## Repository map

| Path | Layer |
|---|---|
| `index.html`, `dossier.html` | Reading layer (GitHub Pages) |
| `paper/manuscript.tex` / `.pdf` | Citable artifact |
| `verification/verify_numbers.py` | Executable claims (CI-enforced) |
| `verification/research_pipeline.md` | The method (Open Dossier format spec) |
| `claim_ledger.csv` | Every claim, typed and routed to its verifier |

## Cite it

See [`CITATION.cff`](CITATION.cff) (GitHub renders a "Cite this repository" button from it). Tagged releases are archived with a DOI via Zenodo.

## Disclosure

Built with substantive AI assistance (Claude, Anthropic). The verification model
is **honest labeling, not universal verification**: every claim carries a public,
granular status, and claims nobody has verified are labeled, never asserted.

## License

Paper and prose: CC BY 4.0 · Code: MIT. See [`LICENSE.md`](LICENSE.md).
