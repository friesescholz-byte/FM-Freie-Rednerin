import re

images = [
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/298b66ce-2aae-4c24-851d-4a20d3ebc687.jpg",
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/68e4c63d-aaf4-48a6-8454-2a6d2a35c7ad.jpg",
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/IMG_3535.JPG",
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/IMG_3538.JPG",
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/J_u_L_Wed_394.jpg",
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/bfa84e6e-1100-4f8f-8ac9-c5a7f48706d7.jpg",
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/d82f5b03-fbd1-4793-b136-ca9b64c222c6.jpg",
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/e1dc078d-5f8a-40ca-b5f1-0cd19d5dfe04.jpg"
]

slides_html = ""
for i, img in enumerate(images):
    slides_html += f"                        <div class=\"slide slide-{i+1}\" style=\"background-image: url('{img}');\"></div>\n"

# Update trauungen.html
with open('trauungen.html', 'r', encoding='utf-8') as f:
    trauungen = f.read()

# We find the .editorial-slider div and replace its inner HTML
pattern = re.compile(r'(<div class="editorial-slider">).*?(</div>)', re.DOTALL)
trauungen = pattern.sub(rf'\1\n{slides_html}\2', trauungen)

with open('trauungen.html', 'w', encoding='utf-8') as f:
    f.write(trauungen)

# Update style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change 24s to 48s
css = css.replace("animation: fadeSlide 24s infinite;", "animation: fadeSlide 48s infinite;")

# Replace the old slide delays and keyframes
old_slide_css = """.slide-1 { animation-delay: 0s; }
.slide-2 { animation-delay: 6s; }
.slide-3 { animation-delay: 12s; }
.slide-4 { animation-delay: 18s; }

@keyframes fadeSlide {
    0%   { opacity: 0; animation-timing-function: ease-in; }
    8%   { opacity: 1; animation-timing-function: linear; }
    25%  { opacity: 1; animation-timing-function: ease-out; }
    33%  { opacity: 0; }
    100% { opacity: 0; }
}"""

new_slide_css = """.slide-1 { animation-delay: 0s; }
.slide-2 { animation-delay: 6s; }
.slide-3 { animation-delay: 12s; }
.slide-4 { animation-delay: 18s; }
.slide-5 { animation-delay: 24s; }
.slide-6 { animation-delay: 30s; }
.slide-7 { animation-delay: 36s; }
.slide-8 { animation-delay: 42s; }

@keyframes fadeSlide {
    0%   { opacity: 0; animation-timing-function: ease-in; }
    4%   { opacity: 1; animation-timing-function: linear; }
    12.5% { opacity: 1; animation-timing-function: ease-out; }
    16.5% { opacity: 0; }
    100% { opacity: 0; }
}"""

if old_slide_css in css:
    css = css.replace(old_slide_css, new_slide_css)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
