import re

# 1. Update style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add flex: 1 to .contact-form-wrapper
css = css.replace('.contact-form-wrapper {\n    background-color: var(--white);', '.contact-form-wrapper {\n    flex: 1;\n    background-color: var(--white);')

# We need to add overrides for theme-trauer
# The salbeigrün color is #9CAEA0, which is rgb(156, 174, 160)
theme_trauer_overrides = """
/* Theme Trauer Specific Hover & Animations */
body.theme-trauer .btn-primary:hover {
    background-color: var(--accent-dark);
    box-shadow: 0 12px 24px rgba(156, 174, 160, 0.4);
}

body.theme-trauer .btn-premium:hover {
    box-shadow: 0 15px 30px rgba(156, 174, 160, 0.3);
}

body.theme-trauer .btn-premium-outline:hover {
    background: rgba(156, 174, 160, 0.05);
}

body.theme-trauer .timeline-dot {
    border-color: rgba(156, 174, 160, 0.2);
    box-shadow: 0 0 0 0 rgba(156, 174, 160, 0.5);
    animation: pulseTrauer 2s infinite;
}

@keyframes pulseTrauer {
    0% { transform: scale(0.9); box-shadow: 0 0 0 0 rgba(156, 174, 160, 0.5); }
    70% { transform: scale(1); box-shadow: 0 0 0 15px rgba(156, 174, 160, 0); }
    100% { transform: scale(0.9); box-shadow: 0 0 0 0 rgba(156, 174, 160, 0); }
}
"""

if "pulseTrauer" not in css:
    css += "\n" + theme_trauer_overrides

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Update zertifikate.html
with open('zertifikate.html', 'r', encoding='utf-8') as f:
    zert = f.read()

# Remove the second image
# <img src="https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/Zert5_black.png" alt="Zertifikat IHK" class="zertifikat-img">
cert_to_remove = '<img src="https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/Zert5_black.png" alt="Zertifikat IHK" class="zertifikat-img">'
zert = zert.replace(cert_to_remove, '')

with open('zertifikate.html', 'w', encoding='utf-8') as f:
    f.write(zert)


# 3. Just to be absolutely sure the H1 in trauerreden.html gets the cool gradient animation
with open('trauerreden.html', 'r', encoding='utf-8') as f:
    trauer = f.read()

trauer = trauer.replace('<span class="italic-text">Worte, die bleiben.</span>', '<span class="animated-gradient-text">Worte, die bleiben.</span>')

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(trauer)
