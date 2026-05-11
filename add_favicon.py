import glob
import os

favicon_tag = '<link rel="icon" type="image/png" href="https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/Logo-fm-fr-transparent.png">'

html_files = glob.glob("*.html")

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if favicon already exists
    if 'rel="icon"' in content:
        print(f"Favicon already exists in {filepath}")
        continue
        
    # Insert before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'    {favicon_tag}\n</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added favicon to {filepath}")
    else:
        print(f"Could not find </head> in {filepath}")
