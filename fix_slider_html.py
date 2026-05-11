import re

def fix_slider_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The bad structure looks like:
    # </div>
    #                         <div class="slide slide-2" ...></div>
    #                         <div class="slide slide-3" ...></div>
    #                         <div class="slide slide-4" ...></div>
    #                     </div>
    # 
    # We want to replace it so that the new slides are just cleanly inside one <div class="editorial-slider">...</div>

    # Find where the 8 slides end. We know they end with slide-8's div, then </div>.
    # The simplest way is to find the block of old slides and the stray </div> and remove them.
    # Actually, let's just use regex to clean up anything between `<div class="editorial-slider">` and the actual `</div></div>` of the wrapper.

    pattern = re.compile(r'(<div class="editorial-slider">.*?</div>)\s*<div class="slide slide-2".*?<div class="slide slide-4".*?</div>\s*</div>', re.DOTALL)
    
    # Wait, the </div> at the end of slide-8 closed the editorial-slider. 
    # We want to remove the `</div>` after `slide-8` and remove the old slides, leaving the last `</div>`.
    
    # Let's do it safer:
    pattern2 = re.compile(r'(<div class="slide slide-8"[^>]+></div>)\s*</div>\s*<div class="slide slide-2"[^>]+></div>\s*<div class="slide slide-3"[^>]+></div>\s*<div class="slide slide-4"[^>]+></div>\s*</div>', re.DOTALL)
    
    if pattern2.search(content):
        # We replace the matched block with just the slide-8 div and the final closing div.
        content = pattern2.sub(r'\1\n                    </div>', content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file_path}")
    else:
        print(f"Pattern not found in {file_path}")

fix_slider_html('trauungen.html')
fix_slider_html('trauerreden.html')
