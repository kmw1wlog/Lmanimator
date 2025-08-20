from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

static_dir = Path(__file__).parent / "static"
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

out_dir = Path(__file__).parent / "out"
out_dir.mkdir(exist_ok=True)
app.mount("/out", StaticFiles(directory=out_dir), name="out")


@app.post("/api/generate-animation")
async def generate_animation(payload: dict):
    """Generate a Manim animation from a text prompt.

    This placeholder endpoint returns the path to a pre-rendered video.
    """
    prompt = payload.get("prompt", "")
    video_path = out_dir / "result.mp4"
    return JSONResponse({"video_url": f"/out/{video_path.name}"})
