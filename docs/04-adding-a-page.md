# Turning a stub into a real page

Example: the CV page. The route and nav link already exist; only the
view and template change.

**1. Content.** Put the page's text in `data/cv.json` (same pattern as
`about.json`). If it holds a list with rules (dates, types), add a
Pydantic model to `core/models.py` and a loader function to
`core/content.py`, like `get_quotes()`.

**2. View** (`app.py`): pass the data in.
```python
@app.route("/cv/")
def cv():
    return render_template("pages/cv.html", page=content.read_json("cv"))
```

**3. Template** (`templates/pages/cv.html`): extend `base.html` instead of
the placeholder.
```jinja
{% extends "base.html" %}
{% set title = page.title %}
{% set description = page.intro %}

{% block page_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/pages/cv.css') }}">
{% endblock %}

{% block content %}
  <section class="container">
    <h1>{{ page.title }}</h1>
  </section>
{% endblock %}
```

**4. Styles**: create `static/css/pages/cv.css`. Use the variables from
`tokens.css` (`var(--color-olive)`), not raw colors.

**5. Reuse** components with `{% from "components/x.html" import x %}`;
e.g. the CV can show `publication_list(...)`, like Research does.

**6. Check**: `python build.py` must finish without errors.

## A brand-new page (not in the nav yet)
Add the route in `app.py`, the template, and, if it belongs in the
menu, an entry in `NAV_ITEMS` (also in `app.py`). For a page with
many URLs (like `/research/<slug>/`), also add a generator in `build.py`
so the build knows every URL.
