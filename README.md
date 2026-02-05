# Handwriting Synthesis API on Render

Uses https://github.com/otuva/handwriting-synthesis (TensorFlow 2.x compatible)

## Setup

1. Create a new GitHub repo and push these files:
   - app.py
   - requirements.txt
   - render.yaml

2. Go to https://render.com and sign in

3. Click "New" → "Web Service"

4. Connect your GitHub repo

5. Render will auto-detect render.yaml and configure everything

6. Wait for deploy (first build takes a while due to TensorFlow)

## API Usage

### Generate Handwriting

```bash
curl -X POST https://your-app.onrender.com/generate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "style": 3}'
```

### Parameters

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| text | string | required | Text to convert |
| style | int | random | Style 0-11 |
| bias | float | 0.75 | Uniformity (0-1, higher = more uniform) |
| width | int | 1000 | SVG width |

### Health Check

```bash
curl https://your-app.onrender.com/
```

## Notes

- Free tier: spins down after 15min inactive, cold start ~30s
- Paid tier: always on, recommended for production
