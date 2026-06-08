import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace .split-bg
old_split_bg = """.split-bg {
            position: absolute;
            top: -5%; left: -5%; width: 110%; height: 110%;
            background-size: cover;
            background-position: center;
            transition: transform 1.5s cubic-bezier(0.16, 1, 0.3, 1), filter 1s ease;
            z-index: 1;
        }"""

new_split_bg = """.split-bg {
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

html = html.replace(old_split_bg, new_split_bg)

# Replace split-screen:hover .split-pane:not(:hover) .split-bg
old_not_hover = """.split-screen:hover .split-pane:not(:hover) .split-bg {
            filter: grayscale(40%) blur(2px);
            transform: scale(1);
        }"""

new_not_hover = """.split-screen:hover .split-pane:not(:hover) .split-bg {
            filter: grayscale(40%) blur(2px);
            transform: translateX(-50%) scale(1);
        }"""

html = html.replace(old_not_hover, new_not_hover)

# Replace .split-pane:hover .split-bg
old_hover = """.split-pane:hover .split-bg {
            transform: scale(1.05);
            filter: grayscale(0%) blur(0px);
        }"""

new_hover = """.split-pane:hover .split-bg {
            transform: translateX(-50%) scale(1.05);
            filter: grayscale(0%) blur(0px);
        }"""

html = html.replace(old_hover, new_hover)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
