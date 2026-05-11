import re

with open('trauerreden.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<title>.*?</title>', '<title>Finnja Marie – Freie Rednerin für Trauerfeiern</title>', content)
content = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Einfühlsame und persönliche Trauerreden mit Finnja Marie. Ich begleite Sie mit Ruhe, Herz und Respekt für einen würdevollen Abschied.">', content)

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('trauungen.html', 'r', encoding='utf-8') as f:
    content = f.read()

nav_links_match = re.search(r'<ul class="nav-links">.*?</ul>', content, re.DOTALL)
if nav_links_match:
    old_nav = nav_links_match.group(0)
    if 'index.html' not in old_nav:
        new_nav = old_nav.replace('<li><a href="#philosophie">Philosophie</a></li>', '<li><a href="index.html" style="opacity: 0.7;">&larr; Startseite</a></li>\n                    <li><a href="#philosophie">Philosophie</a></li>')
        content = content.replace(old_nav, new_nav)

with open('trauungen.html', 'w', encoding='utf-8') as f:
    f.write(content)
