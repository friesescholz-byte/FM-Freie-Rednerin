import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find the start of the theme
start_idx = css.find('/* THEME: TRAUERREDEN')
if start_idx != -1:
    css = css[:start_idx - 25] # Cut off before the comment

new_theme = """
/* ===================== */
/* THEME: TRAUERREDEN    */
/* ===================== */
body.theme-trauer {
    --bg-main: #FAF8F5; /* warmes Creme */
    --bg-alt: #EFECE6; /* helles Beige/Taupe */
    --accent: #9CAEA0; /* zartes Salbeigrün */
    --accent-dark: #7D8F81;
    --text-main: #2C302E; /* dunkles Anthrazit */
    --text-light: #595B5A;
    --white: #FFFFFF;
}

body.theme-trauer .btn-premium {
    background-color: var(--accent);
    color: #fff;
    border-color: var(--accent);
}
body.theme-trauer .btn-premium:hover {
    background-color: var(--accent-dark);
}

body.theme-trauer .btn-primary {
    background-color: var(--accent);
    color: #fff;
}
body.theme-trauer .btn-primary:hover {
    background-color: var(--accent-dark);
}

body.theme-trauer .split-image.reveal::after, body.theme-trauer .contact-image-wrapper.reveal::after {
    background-color: var(--bg-main);
}
body.theme-trauer .bg-alt .split-image.reveal::after, body.theme-trauer .bg-alt .contact-image-wrapper.reveal::after {
    background-color: var(--bg-alt);
}
"""

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css + new_theme)
