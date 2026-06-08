import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace .split-bg
old_split_bg = """.split-bg {
            position: absolute;
            top: -5vh; 
            left: 50%; 
            width: 110vw; 
            height: 110vh;
            transform: translateX(-50%);
            background-size: cover;
            background-position: center;
            transition: transform 1.5s cubic-bezier(0.16, 1, 0.3, 1), filter 1s ease;
            z-index: 1;
        }"""

new_split_bg = """.split-bg {
            position: absolute;
            top: -5vh; 
            left: 50%; 
            width: 60vw; 
            height: 110vh;
            transform: translateX(-50%);
            background-size: cover;
            background-position: center;
            transition: transform 1.5s cubic-bezier(0.16, 1, 0.3, 1), filter 1s ease;
            z-index: 1;
        }"""

html = html.replace(old_split_bg, new_split_bg)

# Now add the media query fix for mobile split-bg
media_query_end = """            .pane-funeral .explore-btn { background: rgba(255,255,255,0.1); }
            .pane-wedding .explore-btn { background: rgba(74, 59, 50, 0.05); }
        }"""

new_media_query_end = """            .pane-funeral .explore-btn { background: rgba(255,255,255,0.1); }
            .pane-wedding .explore-btn { background: rgba(74, 59, 50, 0.05); }
            
            .split-bg {
                width: 110vw;
                height: 60vh;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
            }
            .split-screen:hover .split-pane:not(:hover) .split-bg {
                transform: translate(-50%, -50%) scale(1);
            }
            .split-pane:hover .split-bg {
                transform: translate(-50%, -50%) scale(1.05);
            }
        }"""

html = html.replace(media_query_end, new_media_query_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
