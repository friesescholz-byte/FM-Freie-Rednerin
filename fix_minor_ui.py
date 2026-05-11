import re

# 1. Update style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

theme_trauer_section_tag = """
body.theme-trauer .section-tag::after {
    background: linear-gradient(90deg, transparent, rgba(156, 174, 160, 0.4), transparent);
}
"""

if "body.theme-trauer .section-tag::after" not in css:
    css += "\n" + theme_trauer_section_tag

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Update trauerreden.html (remove second button)
with open('trauerreden.html', 'r', encoding='utf-8') as f:
    trauer = f.read()

cta_block_old = """<p style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin-bottom: 1.5rem; color: var(--text-main);">Ich bin gerne für Sie da, wenn Worte schwerfallen.</p>
                    <a href="zertifikate.html" class="btn-premium-outline" style="margin-top: 2rem; display: inline-block; font-size: 0.9rem; padding: 0.8rem 1.5rem;">Meine Zertifikate</a>
            <a href="#kontakt" class="btn-primary">Kontakt aufnehmen</a>"""

cta_block_new = """<p style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin-bottom: 1.5rem; color: var(--text-main);">Ich bin gerne für Sie da, wenn Worte schwerfallen.</p>
            <a href="#kontakt" class="btn-primary">Kontakt aufnehmen</a>"""

trauer = trauer.replace(cta_block_old, cta_block_new)

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(trauer)

