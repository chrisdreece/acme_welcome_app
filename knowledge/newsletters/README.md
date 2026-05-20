Drop Acme newsletter content into this folder.

What the app reads:
- `.txt` files
- `.md` files

How it works:
- each file in this folder is added to the system prompt as reference material
- files are loaded automatically on app start
- if a newsletter conflicts with the main Acme context in `scripts/welcome_prompt.py`, the main Acme context wins

Recommended approach:
- one newsletter per file
- use clear filenames like `2026-04-office-hydration-bulletin.md`
- keep each file reasonably concise so the prompt does not get too large

Not loaded automatically:
- `.pdf`
- `.docx`
- images

If you want, a next step is to add PDF support or a retrieval step so the app can handle a much larger newsletter archive.
