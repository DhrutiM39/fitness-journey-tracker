# fitness-journey-tracker
Personal fitness tracker with daily workouts, diet checklist, motivational quotes, and monthly progress measurements.

## GitHub Pages

The published site starts at [`index.html`](./index.html). In the repository, open **Settings → Pages**, choose **Deploy from a branch**, and select **main** and **/(root)**.

## Updating the site

The site is a static HTML page and needs no package installation. To regenerate `index.html` after changing the workout data or layout, run:

```powershell
python build_tracker.py
```

The workout reference images must remain beside `index.html`. Daily checklist progress and body measurements are stored in the browser's local storage, so they are specific to each browser and device.
