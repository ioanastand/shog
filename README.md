# Image Processor

Image Processor is a small utility for preparing batches of images before publishing or archiving.

The demo scans a virtual image collection, applies simple processing operations and prints an export report.

---

## Processing Pipeline

Scan Images
      │
      ▼
Resize
      │
      ▼
Convert
      │
      ▼
Export

---

## Example Output

```
Scanning image collection...

holiday.jpg
Resize: 1920x1080 → 1280x720
Format: JPG → PNG

portrait.png
Resize: 1200x1600 → 900x1200

Export completed.

Images processed: 2
```

---

## Files

- scanner.py — image discovery
- processor.py — processing workflow
- filters.py — resize and conversion
- exporter.py — export simulation
- report.py — summary
- sample_images.py — demo images

Run:

```bash
python app.py
```

The project uses sample data stored in memory.
