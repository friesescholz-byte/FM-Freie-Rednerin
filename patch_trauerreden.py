import re

with open('trauerreden.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add theme class
content = content.replace('<body>', '<body class="theme-trauer">')

# 2. Add Back Button to Navigation
nav_links_match = re.search(r'<ul class="nav-links">.*?</ul>', content, re.DOTALL)
if nav_links_match:
    old_nav = nav_links_match.group(0)
    new_nav = old_nav.replace('<li><a href="#philosophie">Philosophie</a></li>', '<li><a href="index.html" style="opacity: 0.7;">&larr; Startseite</a></li>\n                    <li><a href="#philosophie">Philosophie</a></li>')
    content = content.replace(old_nav, new_nav)

# 3. Hero Section
content = re.sub(r'<div class="vogue-hero-background" style="background-image: url\([^)]+\);"></div>', 
                 '<div class="vogue-hero-background" style="background-image: url(\'https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/051056a8-e1a0-402f-b239-9122f7ef3cc0.jpg\');"></div>', content)
content = re.sub(r'<h1 class="hero-title fade-in-up">.*?</h1>', '<h1 class="hero-title fade-in-up">Worte, die erinnern. Worte, die trösten. Worte, die bleiben.</h1>', content, flags=re.DOTALL)
content = re.sub(r'<p class="hero-subtitle-premium fade-in-up delay-1">.*?</p>', '<p class="hero-subtitle-premium fade-in-up delay-1">Ich begleite Angehörige mit einfühlsamen und persönlichen Trauerreden, die das Leben eines geliebten Menschen würdevoll in den Mittelpunkt stellen.</p>', content, flags=re.DOTALL)
content = re.sub(r'<a href="#kontakt" class="btn-premium fade-in-up delay-2">.*?</a>', '<a href="#kontakt" class="btn-premium fade-in-up delay-2">Trauerrede anfragen</a>', content, flags=re.DOTALL)
content = re.sub(r'<p class="hero-trust">.*?</p>', '<p class="hero-trust">In einem persönlichen Gespräch nehme ich mir Zeit für Ihre Erinnerungen, Gedanken und Wünsche.</p>', content, flags=re.DOTALL)


# 4. Impressionen
# Remove the impressionen section from Trauerreden
content = re.sub(r'<!-- 1\.5 Slider Sektion \(Impressionen\) -->.*?<!-- 2\. Kurzer Einstieg -->', '<!-- 2. Kurzer Einstieg -->', content, flags=re.DOTALL)

# 5. Einstieg (Philosophie)
content = re.sub(r'<span class="section-tag">Philosophie</span>', '<span class="section-tag">Einstieg</span>', content)
content = re.sub(r'<div class="split-text reveal">.*?<div class="slogan-box">', '''<div class="split-text reveal">
                    <span class="section-tag">Einstieg</span>
                    <h2>Ein Abschied, der dem Menschen gerecht wird</h2>
                    <p>Wenn ein geliebter Mensch geht, fehlen oft die Worte. Und gleichzeitig gibt es so vieles, was gesagt werden möchte: Erinnerungen, besondere Momente, kleine Eigenheiten, Dankbarkeit, Liebe und all das, was diesen Menschen ausgemacht hat.</p>
                    <p>Eine persönliche Trauerrede gibt diesen Gedanken einen würdevollen Rahmen. Sie erzählt nicht nur von einem Leben, sondern lässt spürbar werden, wer dieser Mensch war – mit seiner Geschichte, seinen Werten, seinen Spuren und seiner Bedeutung für die Menschen, die zurückbleiben.</p>
                    <p>Ich unterstütze Sie dabei, Worte für diesen Abschied zu finden. Ruhig, einfühlsam und mit viel Respekt.</p>
                    <div class="slogan-box">''', content, count=1, flags=re.DOTALL)
content = re.sub(r'<p class="slogan-small">.*?</p>', '<p class="slogan-small">Für einen Abschied, der nicht allgemein klingt – sondern persönlich berührt.</p>', content, count=1)

# 6. Über mich
content = re.sub(r'<span class="section-tag">Über mich</span>', '<span class="section-tag">Über mich</span>', content, count=1)
content = re.sub(r'<h2>Hallo, ich bin Finnja Marie.*?</h2>', '<h2>Ich bin Finnja Marie – freie Rednerin mit Herz, Ruhe und Feingefühl</h2>', content, count=1, flags=re.DOTALL)
content = re.sub(r'<p>Schon immer haben mich die Geschichten.*?<p class="slogan">', '''<p>Als freie Rednerin begleite ich Menschen in besonderen Lebensmomenten. Dazu gehören nicht nur freudige Anlässe, sondern auch die stillen und schweren Augenblicke des Abschieds.</p>
                    <p>Mir ist wichtig, Angehörigen mit Ruhe, Offenheit und Respekt zu begegnen. Ich höre zu, stelle behutsame Fragen und nehme mir Zeit für das, was erzählt werden möchte.</p>
                    <p>Aus Ihren Erinnerungen, Gedanken und Gefühlen entsteht eine Trauerrede, die persönlich, ehrlich und würdevoll ist. Eine Rede, die nicht beschönigt, nicht überhöht und nicht austauschbar klingt – sondern den Menschen so zeigt, wie er war.</p>
                    <p class="slogan">Mit Worten, die Halt geben, wenn Worte schwerfallen.</p>
                    <p style="display:none;" class="slogan">''', content, count=1, flags=re.DOTALL)

# 7. Leistungen (Ablauf -> Leistungen)
content = re.sub(r'<span class="section-tag">Ablauf</span>', '<span class="section-tag">Leistungen</span>', content, count=1)
content = re.sub(r'<h2>Wie wir gemeinsam.*?</p>', '''<h2>Wie ich Sie in der Zeit des Abschieds begleite</h2>
                <p>In einer Zeit, in der vieles organisiert und entschieden werden muss, möchte ich Ihnen einen Teil abnehmen. Ich begleite Sie vom ersten Gespräch bis zur Trauerfeier mit Ruhe, Struktur und Einfühlungsvermögen.</p>''', content, count=1, flags=re.DOTALL)

# Timeline Items
content = re.sub(r'<div class="timeline">.*?</div>\s*</div>\s*</section>', '''<div class="timeline">
                    <!-- Step 1 -->
                    <div class="timeline-item reveal">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <h3>Persönliches Trauergespräch</h3>
                            <p>In einem persönlichen Gespräch nehmen wir uns Zeit für Erinnerungen, Lebensstationen, besondere Eigenschaften und alles, was Ihnen wichtig ist. Sie entscheiden, was erzählt werden soll und was nicht.</p>
                        </div>
                    </div>
                    
                    <!-- Step 2 -->
                    <div class="timeline-item reveal delay-1">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <h3>Einfühlsame Begleitung</h3>
                            <p>Ich führe Sie behutsam durch das Gespräch und unterstütze Sie dabei, Gedanken und Erinnerungen zu ordnen. Auch wenn Ihnen selbst die Worte fehlen, helfe ich dabei, das Wesentliche sichtbar zu machen.</p>
                        </div>
                    </div>
                    
                    <!-- Step 3 -->
                    <div class="timeline-item reveal delay-2">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <h3>Individuell geschriebene Trauerrede</h3>
                            <p>Jede Rede entsteht persönlich und individuell. Keine Vorlage, keine Standardformulierungen, sondern Worte, die zum verstorbenen Menschen und zur Familie passen.</p>
                        </div>
                    </div>
                    
                    <!-- Step 4 -->
                    <div class="timeline-item reveal delay-3">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <h3>Durchführung der Trauerfeier</h3>
                            <p>Am Tag der Beisetzung oder Trauerfeier führe ich mit ruhiger Stimme und würdevoller Präsenz durch die Zeremonie. Dabei steht der verstorbene Mensch im Mittelpunkt – mit seiner Geschichte, seinem Wesen und seinen Spuren.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>''', content, count=1, flags=re.DOTALL)

# 8. Dein Stil (Checklist)
content = re.sub(r'<h2>Eure Trauung, euer Stil</h2>.*?</p>', '''<h2>Trauerreden mit Würde, Wärme und Persönlichkeit</h2>
                    <p>Eine Trauerrede darf traurig sein. Sie darf aber auch dankbar sein, liebevoll, ehrlich und manchmal sogar von einem leisen Lächeln begleitet. Denn ein Leben besteht nicht nur aus dem Abschied, sondern aus vielen Momenten, Begegnungen und Erinnerungen.</p>
                    <p>Ich schreibe Trauerreden, die den Menschen in den Mittelpunkt stellen. Nicht nur Daten und Lebensstationen, sondern das, was zwischen den Zeilen liegt: Charakter, Gewohnheiten, Werte, kleine Geschichten und das, was bleibt.</p>''', content, count=1, flags=re.DOTALL)

content = re.sub(r'<ul class="checklist">.*?</ul>', '''<ul class="checklist">
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> persönliche Worte statt Standardformulierungen</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> einen würdevollen und ruhigen Rahmen</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> ehrliche Erinnerungen mit Herz und Respekt</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Raum für Trauer, Dankbarkeit und Liebe</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> behutsame Gespräche mit den Angehörigen</li>
                        </ul>''', content, count=1, flags=re.DOTALL)

content = re.sub(r'<div class="highlight-slogan highlight-slogan-light mt-4">.*?</div>', '''<div class="highlight-slogan highlight-slogan-light mt-4">
                        "Nicht das Ende steht im Mittelpunkt – sondern das Leben, das Spuren hinterlassen hat."
                    </div>''', content, count=1, flags=re.DOTALL)

# 9. Preise
content = re.sub(r'<h2>Investition in euren besonderen Moment</h2>.*?</p>', '''<h2>Honorar für eine persönliche Trauerrede</h2>
                    <p>Eine persönliche Trauerrede braucht Zeit, Ruhe und Aufmerksamkeit. Sie entsteht aus Gesprächen, Erinnerungen und dem Wunsch, einem Menschen mit würdevollen Worten gerecht zu werden.</p>
                    <p>Mein Honorar umfasst das persönliche Trauergespräch, die individuelle Ausarbeitung der Rede, die Abstimmung des Ablaufs sowie die Durchführung der Trauerfeier.</p>''', content, count=1, flags=re.DOTALL)

content = re.sub(r'<h3>Freie Trauung mit Finnja Marie</h3>', '<h3>Persönliche Trauerrede mit Finnja Marie</h3>', content, count=1)
content = re.sub(r'<div class="price" style="font-size: 1.8rem; margin: 1rem 0;">.*?</div>', '<div class="price" style="font-size: 1.8rem; margin: 1rem 0;">Preis auf Anfrage</div>', content, count=1)
content = re.sub(r'<div class="travel-costs">.*?</div>', '<div class="travel-costs">zzgl. Fahrtkosten</div>', content, count=1)
content = re.sub(r'<p class="includes-title".*?>Jedes Paar ist anders.*?</p>', '<p class="includes-title" style="margin-bottom: 0.5rem; color: var(--text-main);">Jede Abschiedssituation ist anders.</p>', content, count=1)
content = re.sub(r'<p style="margin-bottom: 2rem;.*?</p>', '<p style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.6; color: var(--text-light);">Gerne bespreche ich mit Ihnen persönlich, welche Begleitung Sie sich wünschen und welches Honorar dafür anfällt.</p>', content, count=1)

content = re.sub(r'<ul class="pricing-list">.*?</ul>', '''<ul class="pricing-list">
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> persönliches Trauergespräch</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> behutsame Begleitung der Angehörigen</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> individuell geschriebene Trauerrede</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> Abstimmung des Ablaufs</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> Durchführung der Trauerfeier</li>
                        </ul>''', content, count=1, flags=re.DOTALL)

# 10. Vertrauen
content = re.sub(r'<h2>Warum wir die perfekte Wahl füreinander sind</h2>', '<h2>In schweren Momenten gut begleitet</h2>', content, count=1)
content = re.sub(r'<p class="solid-text">An eurem Hochzeitstag solltet ihr euch.*?</p>', '''<p class="solid-text">Ein Abschied bringt viele Gefühle mit sich. Trauer, Dankbarkeit, Schmerz, Liebe und manchmal auch Sprachlosigkeit. Genau deshalb ist es wichtig, jemanden an der Seite zu haben, der zuhört, sortiert und behutsam die richtigen Worte findet.</p>
<p class="solid-text">Ich begegne jeder Lebensgeschichte mit Respekt. Jeder Mensch verdient einen Abschied, der nicht austauschbar ist, sondern seinem Wesen gerecht wird.</p>''', content, count=1, flags=re.DOTALL)

content = re.sub(r'<div class="trust-grid">.*?</div>', '''<div class="trust-grid">
                        <div class="trust-item reveal"><span class="check">✓</span> einfühlsame und ruhige Gesprächsführung</div>
                        <div class="trust-item reveal delay-1"><span class="check">✓</span> persönliche Reden ohne Standardtexte</div>
                        <div class="trust-item reveal delay-2"><span class="check">✓</span> respektvoller Umgang mit jeder Lebensgeschichte</div>
                        <div class="trust-item reveal delay-3"><span class="check">✓</span> klare Struktur in einer schweren Zeit</div>
                    </div>''', content, count=1, flags=re.DOTALL)

content = re.sub(r'<p class="highlight-slogan reveal">.*?</p>', '<p class="highlight-slogan reveal">Weil jeder Mensch einen Abschied verdient, der seine Geschichte würdigt.</p>', content, count=1)

# 11. Kontakt
content = re.sub(r'<h2>Lasst uns über eure freie Trauung sprechen</h2>', '<h2>Wenn Sie Unterstützung für einen persönlichen Abschied wünschen</h2>', content, count=1)
content = re.sub(r'<p>Wenn ihr euch eine Zeremonie.*?</p>\s*<p>Erzählt mir von eurem.*?</p>', '''<p>Wenn Sie eine Trauerrede suchen, die einfühlsam, persönlich und würdevoll ist, begleite ich Sie gerne in dieser schweren Zeit.</p>
                    <p>In einem Gespräch nehmen wir uns Raum für Erinnerungen, Gedanken und alles, was über den geliebten Menschen gesagt werden soll.</p>''', content, count=1, flags=re.DOTALL)

# Rewrite Form
content = re.sub(r'<label for="name">Name\(n\) \*</label>\s*<input type="text" id="name" name="name" required placeholder="Eure Namen">', '<label for="name">Ihr Name *</label>\n<input type="text" id="name" name="name" required placeholder="Ihr Name">', content, count=1)
content = re.sub(r'<label for="phone">Telefonnummer \*</label>\s*<input type="tel" id="phone" name="phone" required placeholder="Für Rückfragen">', '<label for="phone">Telefonnummer *</label>\n<input type="tel" id="phone" name="phone" required placeholder="Für Rückfragen">', content, count=1)
content = re.sub(r'<label for="date">Wunschdatum der Trauung</label>', '<label for="date">Datum der Beisetzung (falls bekannt)</label>', content, count=1)
content = re.sub(r'<label for="location">Wo findet die Trauung statt\?</label>\s*<input type="text" id="location" name="location" placeholder="Ort oder Location">', '<label for="location">Ort der Trauerfeier</label>\n<input type="text" id="location" name="location" placeholder="Ort">', content, count=1)

# Remove radio buttons for contact
content = re.sub(r'<div class="form-group">\s*<label>Habt ihr schon eine feste Location\?</label>.*?</div>\s*</div>', '</div>', content, count=1, flags=re.DOTALL)

content = re.sub(r'<label for="wishes">Was wünscht ihr euch für eure freie Trauung\?</label>\s*<textarea id="wishes" name="wishes" rows="3" placeholder="Gibt es schon erste Ideen oder Vorstellungen\?"></textarea>', '', content, count=1)
content = re.sub(r'<textarea id="message" name="message" rows="4" required placeholder="Erzählt mir gerne schon ein bisschen was über euch..."></textarea>', '<textarea id="message" name="message" rows="4" required placeholder="Ihre Nachricht..."></textarea>', content, count=1)
content = re.sub(r'<button type="submit" class="btn-primary btn-full">Kennenlernen anfragen</button>', '<button type="submit" class="btn-primary btn-full">Jetzt Kontakt aufnehmen</button>', content, count=1)
content = re.sub(r'<p class="form-hint">Ich melde mich schnellstmöglich.*?Finnja Marie – Freie Rednerin</p>', '<p class="form-hint">Ich melde mich schnellstmöglich bei Ihnen zurück.<br><br><b>Ich bin gerne für Sie da.</b><br>Finnja Marie – Freie Rednerin für Trauerfeiern</p>', content, count=1, flags=re.DOTALL)


with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(content)

