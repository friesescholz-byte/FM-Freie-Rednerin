import re

# Update contact image in trauerreden.html
with open('trauerreden.html', 'r', encoding='utf-8') as f:
    trauer_html = f.read()

# Find the contact image block in trauerreden.html
# We know it is in `<section id="kontakt"...` and has `<div class="contact-image-wrapper mt-4 reveal delay-2">`
# Followed by `<img src="https://images.unsplash.com/photo-1518002171953-a080ee817e1f?q=80&w=800&auto=format&fit=crop" alt="Kontakt"`

old_contact_img = "https://images.unsplash.com/photo-1518002171953-a080ee817e1f?q=80&w=800&auto=format&fit=crop"
new_contact_img = "https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/Trauerfeier_01.png"

if old_contact_img in trauer_html:
    trauer_html = trauer_html.replace(old_contact_img, new_contact_img)

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(trauer_html)
