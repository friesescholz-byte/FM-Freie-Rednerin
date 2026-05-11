import re

# 1. Update css/style.css for .split-text max-width
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change max-width of .split-text from 600px to 680px
css = css.replace('.split-text {\n    max-width: 600px;\n}', '.split-text {\n    max-width: 680px;\n}')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Update trauungen.html
with open('trauungen.html', 'r', encoding='utf-8') as f:
    trau_html = f.read()

# We look for the end of the Über mich section
# <p class="slogan">Fr Worte, die nicht nur gesagt werden - sondern bleiben.</p>
# </div>
# We insert the button there.

btn_html = '\n                    <a href="zertifikate.html" class="btn-premium-outline" style="margin-top: 2rem; display: inline-block; font-size: 0.9rem; padding: 0.8rem 1.5rem;">Meine Zertifikate</a>'
pattern_trau = re.compile(r'(<p class="slogan">.*?</div>)', re.DOTALL)
# Wait, this is too generic. Let's find exactly the slogan in "Über mich"
old_trau_slogan = '<p class="slogan">Für Worte, die nicht nur gesagt werden - sondern bleiben.</p>'
if old_trau_slogan in trau_html:
    trau_html = trau_html.replace(old_trau_slogan, old_trau_slogan + btn_html)
else:
    # If encoding issue
    trau_html = trau_html.replace('sondern bleiben.</p>', 'sondern bleiben.</p>' + btn_html)

with open('trauungen.html', 'w', encoding='utf-8') as f:
    f.write(trau_html)


# 3. Update trauerreden.html
with open('trauerreden.html', 'r', encoding='utf-8') as f:
    trauer_html = f.read()

# <p class="slogan">Mit Worten, die Halt geben, wenn Worte schwerfallen.</p>
old_trauer_slogan = 'schwerfallen.</p>'
if old_trauer_slogan in trauer_html:
    trauer_html = trauer_html.replace(old_trauer_slogan, old_trauer_slogan + btn_html)

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(trauer_html)


# 4. Create zertifikate.html
zert_content = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine Zertifikate - Finnja Marie Freie Rednerin</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <style>
        .zertifikate-content {
            max-width: 800px;
            margin: 0 auto;
            padding: 8rem 2rem 4rem;
            text-align: center;
        }
        .zertifikate-content h1 {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: var(--text-main);
        }
        .zertifikate-content p {
            margin-bottom: 3rem;
            color: var(--text-light);
            font-size: 1.1rem;
        }
        .zertifikat-img {
            max-width: 100%;
            height: auto;
            margin-bottom: 3rem;
            border-radius: var(--border-radius);
            box-shadow: 0 10px 40px rgba(0,0,0,0.08);
            display: block;
        }
    </style>
</head>
<body>
    <header class="header scrolled" id="header" style="background-color: var(--white); box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
        <div class="container navbar">
            <a href="index.html" class="logo">
                <img src="https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/Logo-fm-fr-transparent.png" alt="Finnja Marie Logo">
            </a>
            <nav class="nav-menu" style="display: flex; gap: 2rem;">
                <a href="index.html" style="text-decoration: none; color: var(--text-main); font-weight: 500;">&larr; Zurück zur Startseite</a>
            </nav>
        </div>
    </header>

    <main class="zertifikate-content fade-in-up">
        <span class="section-tag" style="margin-bottom: 1rem;">Qualifikation</span>
        <h1>Meine Zertifikate</h1>
        <p>Erfahrung und fundierte Ausbildung für emotionale und professionelle Reden.</p>
        
        <img src="https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/ZertBanner%20m3.png" alt="Zertifikat Banner" class="zertifikat-img">
        <img src="https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/Zert5_black.png" alt="Zertifikat IHK" class="zertifikat-img">
    </main>

    <footer class="footer">
        <div class="container footer-content" style="display: flex; flex-direction: column; align-items: center; gap: 1.5rem;">
            <div class="footer-links" style="margin-bottom: 0;">
                <a href="impressum.html">Impressum</a>
                <a href="datenschutz.html">Datenschutz</a>
            </div>
            <div class="footer-copyright" style="padding-top: 1rem; width: 100%; max-width: 400px; text-align: center;">
                &copy; <span id="year"></span> Finnja Marie. Alle Rechte vorbehalten.
            </div>
        </div>
    </footer>
    <script>
        document.getElementById('year').textContent = new Date().getFullYear();
    </script>
</body>
</html>"""

with open('zertifikate.html', 'w', encoding='utf-8') as f:
    f.write(zert_content)
