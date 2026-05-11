import os
import re

css_path = 'css/style.css'
with open(css_path, 'rb') as f:
    content = f.read()

# The corrupted part starts around "/* ===================== */" but with null bytes.
# We'll just truncate everything after the last valid closing brace before the mobile-menu-btn media query ends.
# The last valid CSS was at line 1552: `    .small-image {\n        max-width: 100%;\n    }\n}\n`

# Let's decode with utf-8, ignoring errors, to find the cutoff
decoded = content.decode('utf-8', errors='ignore')
cutoff_index = decoded.find('\n}\n \n / *')
if cutoff_index == -1:
    cutoff_index = decoded.find('\n}\n\x00')

if cutoff_index != -1:
    valid_css = decoded[:cutoff_index + 3]
else:
    # Just split by 'max-width: 100%;\n    }\n}'
    parts = decoded.split('max-width: 100%;\n    }\n}')
    valid_css = parts[0] + 'max-width: 100%;\n    }\n}'

dark_theme_css = """
/* ===================== */
/* THEME: TRAUERREDEN    */
/* ===================== */
body.theme-trauer {
    --bg-main: #1C1C1C;
    --bg-alt: #242424;
    --accent: #A39171; /* Muted gold */
    --accent-dark: #8C7B5D;
    --text-main: #EAEAEA;
    --text-light: #A8A8A8;
}

body.theme-trauer .content-box,
body.theme-trauer .card,
body.theme-trauer .pricing-card,
body.theme-trauer .faq-item,
body.theme-trauer .contact-form-wrapper,
body.theme-trauer .slogan-box {
    background-color: #242424;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.05);
}

body.theme-trauer .faq-question:hover {
    background-color: #2a2a2a;
}

body.theme-trauer input[type="text"],
body.theme-trauer input[type="email"],
body.theme-trauer input[type="tel"],
body.theme-trauer input[type="date"],
body.theme-trauer textarea,
body.theme-trauer .radio-group-container {
    background-color: #1a1a1a;
    border-color: #333;
    color: #EAEAEA;
}

body.theme-trauer input:focus,
body.theme-trauer textarea:focus {
    background-color: #222;
}

body.theme-trauer .header.scrolled {
    background-color: rgba(28, 28, 28, 0.95);
}

body.theme-trauer .image-overlay-light {
    background-color: rgba(28, 28, 28, 0.85);
}

body.theme-trauer h1, body.theme-trauer h2, body.theme-trauer h3, body.theme-trauer .solid-text {
    color: #EAEAEA;
}

body.theme-trauer .split-image.reveal::after, body.theme-trauer .contact-image-wrapper.reveal::after {
    background-color: var(--bg-main);
}
body.theme-trauer .bg-alt .split-image.reveal::after, body.theme-trauer .bg-alt .contact-image-wrapper.reveal::after {
    background-color: var(--bg-alt);
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(valid_css + '\n' + dark_theme_css)
