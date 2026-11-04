"""
Build the site into plain HTML files in build/, ready for GitHub Pages.

Frozen-Flask visits every URL of the app (like a crawler) and saves each
response as a file:  /about/  ->  build/about/index.html
After this runs, no Python is needed to serve the site.

Usage:  python build.py
"""

from flask_frozen import Freezer

from app import app
from core import content

app.config["FREEZER_DESTINATION"] = "build"
app.config["FREEZER_REMOVE_EXTRA_FILES"] = True  # delete stale files from old builds
# Show the real error (e.g. "Invalid content in ...md") instead of a bare "500".
app.config["PROPAGATE_EXCEPTIONS"] = True

freezer = Freezer(app)


@freezer.register_generator
def research_detail():
    """Tell the freezer about every write-up page (one per published entry)."""
    for entry in content.get_research():
        yield {"slug": entry.slug}


if __name__ == "__main__":
    pages = freezer.freeze()
    print(f"Built {len(pages)} files into build/")
