import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_css = """.split-image {
    position: relative;
    overflow: hidden;
    border-radius: var(--border-radius);
}"""

new_css = """.split-image, .contact-image-wrapper {
    position: relative;
    overflow: hidden;
    border-radius: var(--border-radius);
}"""

if old_css in css:
    css = css.replace(old_css, new_css)
else:
    print("Could not find the target CSS block!")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
