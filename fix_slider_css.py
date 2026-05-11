import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove background-attachment: fixed from .slide
old_slide = """.slide {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    opacity: 0;
    animation: fadeSlide 48s infinite;
}"""

new_slide = """.slide {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
    opacity: 0;
    animation: fadeSlide 48s infinite;
}"""

if old_slide in css:
    css = css.replace(old_slide, new_slide)
else:
    # Try more robust replacement
    css = css.replace("background-attachment: fixed;\n    opacity: 0;\n    animation: fadeSlide 48s infinite;", "opacity: 0;\n    animation: fadeSlide 48s infinite;")


# Limit max-width of vogue-slider-wrapper so the pill shape remains intact
old_wrapper = """.vogue-slider-wrapper {
    position: relative;
    width: 100%;
    height: 60vh;
    max-height: 650px;
    min-height: 450px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
}"""

new_wrapper = """.vogue-slider-wrapper {
    position: relative;
    width: 100%;
    max-width: 1200px; /* Constrain width to keep pill shape */
    height: 60vh;
    max-height: 650px;
    min-height: 450px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
}"""

if old_wrapper in css:
    css = css.replace(old_wrapper, new_wrapper)


with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
