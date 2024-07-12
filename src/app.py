from dataclasses import dataclass

from fasthtml.common import *
from fasthtml.core import FastHTML
from starlette.staticfiles import StaticFiles
from components import hero_section

app = FastHTMLWithLiveReload(
    hdrs=(Link(rel="stylesheet", href="/static/dist/css/output.css"),
          )
)
app.mount("/static", StaticFiles(directory="../static"), name="static")

rt: app.route = app.route

@rt("/", methods=["GET"])
async def index():
    return hero_section()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)