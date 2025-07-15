import io, uuid, numpy as np, requests
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from moviepy.editor import ImageClip, concatenate_videoclips
from .config import SERVICE_JSON

W, H = 1080, 1920
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_BIG   = ImageFont.truetype(FONT_PATH, 64)
FONT_MID   = ImageFont.truetype(FONT_PATH, 54)
FONT_SMALL = ImageFont.truetype(FONT_PATH, 42)

def _dl(url: str):
    return Image.open(io.BytesIO(requests.get(url, timeout=10).content)).convert("RGB")

def _center(draw, text, y, font):
    w, h = draw.textsize(text, font=font)
    draw.text(((W-w)//2+2, y+2), text, font=font, fill="black")
    draw.text(((W-w)//2, y), text, font=font, fill="white")

def make_frame(item, idx):
    bg = _dl(item["img"]).resize((W, H))
    d  = ImageDraw.Draw(bg)
    y  = H//3
    _center(d, f"Item {idx}  {item['name']}", y, FONT_MID)
    _center(d, f"料率 {item['rate']}%", y+60, FONT_SMALL)
    _center(d, "ROOMリンクはプロフへ↓", y+120, FONT_SMALL)
    return bg

def build_reel(items):
    frames = []

    # title
    title = Image.new("RGB", (W, H), (30,30,30))
    d = ImageDraw.Draw(title)
    _center(d, "K-Interior Picks", H//2 - 30, FONT_BIG)
    frames.append(title)

    for idx, it in enumerate(items, 1):
        frames.append(make_frame(it, idx))

    cta = Image.new("RGB", (W, H), (50,50,50))
    d2 = ImageDraw.Draw(cta)
    _center(d2, "保存して真似する ↓", H//2 - 20, FONT_MID)
    frames.append(cta)

    clips = [ImageClip(np.array(im)).set_duration(3) for im in frames]
    video = concatenate_videoclips(clips, method="compose")
    outfile = f"/tmp/{uuid.uuid4()}.mp4"
    video.write_videofile(outfile, fps=24, codec="libx264", bitrate="2M", audio=False, logger=None)
    return outfile
