import re

images = [
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/pexels-karola-g-6769865.jpg",
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/pexels-karola-g-6769865.jpg",
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/Trauerfeier.png",
    "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/Trauerfeier_01.png"
] * 2

slides_html = ""
for i, img in enumerate(images):
    slides_html += f"                        <div class=\"slide slide-{i+1}\" style=\"background-image: url('{img}');\"></div>\n"

# Update trauerreden.html
with open('trauerreden.html', 'r', encoding='utf-8') as f:
    trauer_html = f.read()

# We find the .editorial-slider div and replace its inner HTML
pattern = re.compile(r'(<div class="editorial-slider">).*?(</div>)', re.DOTALL)
trauer_html = pattern.sub(rf'\1\n{slides_html}\2', trauer_html)

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(trauer_html)
