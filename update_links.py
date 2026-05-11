import os

def replace_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('<a href="#impressum">Impressum</a>', '<a href="impressum.html">Impressum</a>')
    content = content.replace('<a href="#datenschutz">Datenschutz</a>', '<a href="datenschutz.html">Datenschutz</a>')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

replace_links('trauungen.html')
replace_links('trauerreden.html')

# Now add small footer to index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

footer_html = """
    <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 10; display: flex; gap: 20px;">
        <a href="impressum.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">Impressum</a>
        <a href="datenschutz.html" style="color: rgba(255,255,255,0.7); text-decoration: none; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">Datenschutz</a>
    </div>
</body>
"""
if 'impressum.html' not in index_content:
    index_content = index_content.replace('</body>', footer_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
