import re

# Update trauungen.html
with open('trauungen.html', 'r', encoding='utf-8') as f:
    trauungen = f.read()

cta1_trauungen = """        <!-- CTA 1 -->
        <div class="container text-center reveal" style="padding: 3rem 1rem 1rem;">
            <p style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin-bottom: 1.5rem; color: var(--text-main);">Lasst uns gemeinsam eure Geschichte erzählen.</p>
            <a href="#kontakt" class="btn-primary">Kennenlernen anfragen</a>
        </div>
"""

# Insert after ueber-mich section
# We look for `</section>\n\n        <!-- 4. Leistungen -->`
ueber_mich_end = """        </section>

        <!-- 4. Leistungen -->"""

if ueber_mich_end in trauungen:
    trauungen = trauungen.replace(ueber_mich_end, "        </section>\n\n" + cta1_trauungen + "\n        <!-- 4. Leistungen -->")


cta2_trauungen = """        <!-- CTA 2 -->
        <div class="container text-center reveal" style="padding: 4rem 1rem 2rem;">
            <p style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin-bottom: 1.5rem; color: var(--text-main);">Bereit für euren großen Moment?</p>
            <a href="#kontakt" class="btn-primary">Jetzt Termin anfragen</a>
        </div>
"""

# Insert after ablauf section
ablauf_end = """        </section>

        <!-- 7. Preisbereich -->"""

if ablauf_end in trauungen:
    trauungen = trauungen.replace(ablauf_end, "        </section>\n\n" + cta2_trauungen + "\n        <!-- 7. Preisbereich -->")

with open('trauungen.html', 'w', encoding='utf-8') as f:
    f.write(trauungen)


# Update trauerreden.html
with open('trauerreden.html', 'r', encoding='utf-8') as f:
    trauerreden = f.read()

cta1_trauerreden = """        <!-- CTA 1 -->
        <div class="container text-center reveal" style="padding: 3rem 1rem 1rem;">
            <p style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin-bottom: 1.5rem; color: var(--text-main);">Ich bin gerne für Sie da, wenn Worte schwerfallen.</p>
            <a href="#kontakt" class="btn-primary">Kontakt aufnehmen</a>
        </div>
"""

if ueber_mich_end in trauerreden:
    trauerreden = trauerreden.replace(ueber_mich_end, "        </section>\n\n" + cta1_trauerreden + "\n        <!-- 4. Leistungen -->")

cta2_trauerreden = """        <!-- CTA 2 -->
        <div class="container text-center reveal" style="padding: 4rem 1rem 2rem;">
            <p style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin-bottom: 1.5rem; color: var(--text-main);">Lassen Sie uns gemeinsam den passenden Rahmen finden.</p>
            <a href="#kontakt" class="btn-primary">Persönliches Gespräch vereinbaren</a>
        </div>
"""

# The preisbereich comment in trauerreden might be slightly different
# Wait, let's check `trauerreden.html` sections
# In `trauerreden.html`:
#         <!-- 6. Ablauf -->
#         <section id="ablauf" class="section section-ablauf"> ... </section>
#         <!-- 7. Preisbereich -->

if ablauf_end in trauerreden:
    trauerreden = trauerreden.replace(ablauf_end, "        </section>\n\n" + cta2_trauerreden + "\n        <!-- 7. Preisbereich -->")

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(trauerreden)

