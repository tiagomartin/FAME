# GitHub update plan — FAME v1.1.0

Repository:
https://github.com/tiagomartin/FAME

## Recommended workflow

1. Create a branch:
   `release/v1.1.0-companion-manuscripts`

2. Add/replace the files contained in this update package.

3. Do **not** remove existing v1.0.2 transfer outputs.

4. Verify that no file exceeds GitHub's 100 MB per-file limit.

5. Commit with:
   `release: add companion FAME/DOC and DRR/DRVM reproducibility tracks`

6. Open a pull request with the title:
   `FAME v1.1.0: companion manuscripts and DRVM reproducibility`

7. Merge after checking links and notebook paths.

8. Create GitHub tag:
   `v1.1.0`

9. Create GitHub Release:
   title `FAME v1.1.0`
   body from `release/RELEASE_NOTES_v1.1.0.md`.

10. Publish a new version of the existing Zenodo record, or let the GitHub-Zenodo
    integration archive the GitHub release if that integration is already
    enabled.

11. After Zenodo assigns the new version DOI, patch README/CITATION metadata
    with the new DOI.

## Scientific status wording

Until actual journal submission occurs, use:

- `companion manuscript`
- `submission package prepared`
- `target journal: ...`

Do not use:

- `published`
- `accepted`
- `in press`

unless those statuses become true.
