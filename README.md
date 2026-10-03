# San Francisco Meat Co. — Website

A 5-page static site for the Hayes Valley butcher shop at 320 Fell Street.

**Live:** `https://dafaris-dev.github.io/sfmeatco/`

## Pages

| # | Page | File |
|---|---|---|
| 1 | About | `index.html` |
| 2 | Mission | `mission.html` |
| 3 | Services | `services.html` |
| 4 | Menu | `menu.html` |
| 5 | Visit | `visit.html` |

## Stack

Plain HTML + CSS + a tiny bit of vanilla JS. No build step is required to view the site — just open `index.html` or serve the folder.

```
styles.css     — shared stylesheet
script.js      — shared behavior (sticky nav, mobile menu, reveal animations)
assets/        — logo, dry-age cabinet photo, about collage, 8 sandwich photos
build_pages.py — generator script that re-emits all 5 HTML pages from a shared template
```

To regenerate pages after editing `build_pages.py`:

```bash
python3 build_pages.py
```

## Deploy — GitHub Pages

1. Push the branch you want to serve.
2. On GitHub: **Settings → Pages**
3. Source: **Deploy from a branch**
4. Branch: pick this branch, folder `/ (root)`
5. Save, wait ~1 minute, open the URL GitHub shows.

The `.nojekyll` file in the repo root tells Pages to serve files as-is (no Jekyll processing).

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Business info (verified)

- **Address:** 320 Fell Street, San Francisco, CA 94102
- **Phone:** (415) 529-2349
- **Hours:** Tue–Sat 10 am – 7 pm · Sun 11 am – 6 pm · Monday closed
- **Founders:** Justin Seabridge & Kevin Nishikawa
- **Opened:** 2023, on the former Fatted Calf corner in Hayes Valley
