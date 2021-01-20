SHIBUYA="lkIJYc4UH60
def download_video(url: str):
    import pafy
    p = pafy.new(url)
    b=getbest()
    b.download()
    return b.title + ".mp4"

