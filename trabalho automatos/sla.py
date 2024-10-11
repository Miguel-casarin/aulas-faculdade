import pyxel as px

def updat():
    pass

def draw():
    px.cls(0)
    px.text(25,44,"hello world",  px.frame_count %16)

px.init(100, 100, title='helo')
px.run(updat,draw)

