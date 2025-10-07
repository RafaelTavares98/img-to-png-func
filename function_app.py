import azure.functions as func
from PIL import Image
from io import BytesIO
import requests
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="process_image", auth_level=func.AuthLevel.ANONYMOUS)
def process_image(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing image request...")

    url = req.params.get("url")
    if not url:
        return func.HttpResponse("Error: No URL provided.", status_code=400)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        img_bytes = response.content
    except Exception as e:
        return func.HttpResponse(f"Error fetching image: {e}", status_code=400)

    try:
        img = Image.open(BytesIO(img_bytes)).convert("L")  # grayscale
        buf = BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        return func.HttpResponse(buf.read(), mimetype="image/png", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Error processing image: {e}", status_code=400)
