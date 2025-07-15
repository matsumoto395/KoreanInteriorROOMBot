from .rakuten import get_items
from .generator import build_reel
from .uploader import upload
from .notifier import notify
import sys, traceback

def run():
    try:
        items = get_items(top_n=30)[:3]     # pick top3
        mp4 = build_reel(items)
        url = upload(mp4)
        notify("🎞 自動生成Reelが完成しました", url)
    except Exception as e:
        traceback.print_exc()
        notify("⚠️ Reel自動生成でエラー", str(e))

if __name__ == "__main__":
    run()
