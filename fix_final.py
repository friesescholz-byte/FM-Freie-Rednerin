import re

# 1. Update index.html hero image
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace the old image url
old_img = "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/051056a8-e1a0-402f-b239-9122f7ef3cc0.jpg"
new_img = "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/FM-Trauerfeier.png"

if old_img in index_html:
    index_html = index_html.replace(old_img, new_img)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)


# 2. Update trauerreden.html hero image
with open('trauerreden.html', 'r', encoding='utf-8') as f:
    trauer_html = f.read()

if old_img in trauer_html:
    trauer_html = trauer_html.replace(old_img, new_img)

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(trauer_html)


# 3. Fix CSS for contact-image-wrapper
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will append specific CSS to the end of the file to guarantee it overrides any weird previous behaviour.
contact_fix_css = """

/* --- Fix for Contact Image Hover Overflow --- */
.contact-image-wrapper {
    position: relative;
    overflow: hidden;
    border-radius: var(--border-radius);
    display: inline-block; /* ensures the wrapper tightly hugs the image */
    max-width: 300px; /* same as small-image */
}
.contact-image-wrapper img {
    display: block;
    width: 100%;
    height: auto;
    transition: transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
    transform-origin: center center;
}
.contact-image-wrapper:hover img {
    transform: scale(1.05) !important;
}
@media (max-width: 768px) {
    .contact-image-wrapper {
        max-width: 100%;
    }
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(contact_fix_css)

