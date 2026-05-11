import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the absolute footer with a fixed footer and add text-shadow for better visibility
old_footer = """<div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 10; display: flex; gap: 20px;">
        <a href="impressum.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">Impressum</a>
        <a href="datenschutz.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">Datenschutz</a>
    </div>"""

new_footer = """<div style="position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 100; display: flex; gap: 30px; background: rgba(0,0,0,0.4); padding: 8px 20px; border-radius: 50px; backdrop-filter: blur(5px);">
        <a href="impressum.html" style="color: #ffffff; text-decoration: none; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 500;">Impressum</a>
        <a href="datenschutz.html" style="color: #ffffff; text-decoration: none; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 500;">Datenschutz</a>
    </div>"""

if old_footer in content:
    content = content.replace(old_footer, new_footer)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
