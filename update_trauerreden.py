import re

with open('trauerreden.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Pricing text
old_pricing = """                        <h3>Persönliche Trauerrede mit Finnja Marie</h3>
                        <div class="price" style="font-size: 1.8rem; margin: 1rem 0;">Preis auf Anfrage</div>
                        <div class="travel-costs">zzgl. Fahrtkosten</div>
                    </div>
                    <div class="pricing-body">
                        <p style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.6; color: var(--text-light);">Jede Abschiedssituation ist anders. Gerne bespreche ich mit Ihnen persönlich, welche Begleitung Sie sich wünschen und welches Honorar dafür anfällt.</p>"""

new_pricing = """                        <h3>Persönliche Trauerrede mit Finnja Marie</h3>
                        <div class="price" style="font-size: 1.8rem; margin: 1rem 0;">Individuell wie das Leben</div>
                        <div class="travel-costs">Lassen Sie uns den passenden Rahmen finden.</div>
                    </div>
                    <div class="pricing-body">
                        <p class="includes-title" style="margin-bottom: 0.5rem; color: var(--text-main);">Jede Abschiedssituation ist anders.</p>
                        <p style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.6; color: var(--text-light);">Weil es mir wichtig ist, dass die Begleitung exakt zu Ihren Bedürfnissen passt, gibt es bei mir keine starren Pakete. Nach einem ersten, einfühlsamen und völlig unverbindlichen Gespräch erstelle ich Ihnen ein faires Angebot, das genau auf Sie zugeschnitten ist. Das Wichtigste: Wir finden gemeinsam einen Weg.</p>"""

if old_pricing in content:
    content = content.replace(old_pricing, new_pricing)

# 2. Update Stil Image
old_stil_img = """<div class="image-bg" style="background-image: url('https://images.unsplash.com/photo-1517480410764-bbcf7395015e?q=80&w=1600&auto=format&fit=crop');"></div>"""
new_stil_img = """<div class="image-bg" style="background-image: url('https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/652abf4a-15ad-4236-9e71-4edb504ff8df.jpg'); filter: brightness(0.6) sepia(20%);"></div>"""
content = content.replace(old_stil_img, new_stil_img)

# 3. Update Hero Trust Text Color
old_hero_trust = """<p class="hero-trust" style="color: rgba(255,255,255,0.8); margin-top: 1rem; font-size: 0.9rem;">"""
new_hero_trust = """<p class="hero-trust" style="color: #4A4A4A; margin-top: 1rem; font-size: 0.95rem; font-weight: 500; text-shadow: 0 0 15px rgba(255,255,255,0.8);">"""
content = content.replace(old_hero_trust, new_hero_trust)

# 4. Replace Über mich image
old_ueber_mich = """https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/46ac279a-f1ba-4742-993f-05dde6b1092c.jpg"""
new_ueber_mich = """https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/976369f6-13e7-4745-8da9-90cbe7711d9a.jpg"""
content = content.replace(old_ueber_mich, new_ueber_mich)

# Also remove the grayscale filter from the Über mich image if it's there
content = content.replace('class="rounded-image shadow-light portrait" style="filter: sepia(10%) brightness(95%);"', 'class="rounded-image shadow-light portrait"')
content = content.replace('class="rounded-image shadow-light portrait" style="filter: grayscale(80%);"', 'class="rounded-image shadow-light portrait"')


# 5. Add Slider under Hero
slider_html = """        </section>

        <!-- 1.5 Slider Sektion (Impressionen) -->
        <section class="section section-impressionen">
            <div class="container text-center reveal" style="margin-bottom: 3rem;">
                <span class="section-tag">Impressionen</span>
                <h2>Ein würdevoller Rahmen</h2>
            </div>
            <div class="container flex-center">
                <div class="vogue-slider-wrapper reveal delay-1">
                    <div class="slider-outline"></div>
                    <div class="editorial-slider">
                        <div class="slide slide-1" style="background-image: url('https://images.unsplash.com/photo-1499209974431-9dddcece7f88?q=80&w=800&auto=format&fit=crop');"></div>
                        <div class="slide slide-2" style="background-image: url('https://images.unsplash.com/photo-1440688807730-73e4e2169fb8?q=80&w=1600&auto=format&fit=crop');"></div>
                        <div class="slide slide-3" style="background-image: url('https://images.unsplash.com/photo-1518002171953-a080ee817e1f?q=80&w=800&auto=format&fit=crop');"></div>
                        <div class="slide slide-4" style="background-image: url('https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?q=80&w=800&auto=format&fit=crop');"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 2. Kurzer Einstieg -->"""

# We replace the boundary between hero section and einstiegs section
hero_boundary = """        </section>

        <!-- 2. Kurzer Einstieg -->"""

if hero_boundary in content:
    content = content.replace(hero_boundary, slider_html)

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(content)
