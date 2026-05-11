import re

with open('trauerreden.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Images
content = content.replace('https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/298b66ce-2aae-4c24-851d-4a20d3ebc687.jpg', 'https://images.unsplash.com/photo-1499209974431-9dddcece7f88?q=80&w=800&auto=format&fit=crop')
content = content.replace('https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/68e4c63d-aaf4-48a6-8454-2a6d2a35c7ad.jpg', 'https://images.unsplash.com/photo-1440688807730-73e4e2169fb8?q=80&w=1600&auto=format&fit=crop')
content = content.replace('https://pub-b33108412309406a9a941ddc51e9a5b9.r2.dev/FM-Freie-Rednerin/76755cd8-e90f-4171-9dc5-59e24303fea5.jpg', 'https://images.unsplash.com/photo-1518002171953-a080ee817e1f?q=80&w=800&auto=format&fit=crop')

# Fix "Warum eure Trauung bei mir in guten Händen ist" section which was missed
trust_html_old = """<h2>Warum eure Trauung bei mir in guten Händen ist</h2>
                    <p class="intro">Ich weiß, wie besonders dieser Moment für euch ist. Deshalb geht es mir nicht darum, einfach eine schöne Rede zu halten. Es geht darum, eure Geschichte so zu erzählen, dass ihr euch darin wiedererkennt.</p>
                    <p class="intro">Mit viel Gefühl, einem offenen Ohr und einem Gespür für die richtigen Worte begleite ich euch durch die Planung und durch eure Zeremonie. Dabei dürft ihr euch sicher sein: Ihr steht im Mittelpunkt – mit allem, was euch ausmacht.</p>"""

trust_html_new = """<h2>In schweren Momenten gut begleitet</h2>
                    <p class="intro">Ein Abschied bringt viele Gefühle mit sich. Trauer, Dankbarkeit, Schmerz, Liebe und manchmal auch Sprachlosigkeit. Genau deshalb ist es wichtig, jemanden an der Seite zu haben, der zuhört, sortiert und behutsam die richtigen Worte findet.</p>
                    <p class="intro">Ich begegne jeder Lebensgeschichte mit Respekt. Jeder Mensch verdient einen Abschied, der nicht austauschbar ist, sondern seinem Wesen gerecht wird.</p>
                    <p class="intro">Mit Ruhe, Feingefühl und einer klaren Sprache gestalte ich Trauerreden, die Angehörige entlasten und Erinnerungen würdevoll bewahren.</p>"""

if trust_html_old in content:
    content = content.replace(trust_html_old, trust_html_new)
else:
    # try regex fallback
    content = re.sub(r'<h2>Warum eure Trauung bei mir in guten Händen ist</h2>.*?<div class="trust-grid">', trust_html_new + '\n                    <div class="trust-grid">', content, flags=re.DOTALL)


# Fix the stray elements in trust-grid
stray_elements = """</div>
                        <div class="trust-item"><span class="check">✓</span> Keine Standardreden</div>
                        <div class="trust-item"><span class="check">✓</span> Viel Raum für eure Wünsche</div>
                        <div class="trust-item"><span class="check">✓</span> Emotionale Zeremonien mit Leichtigkeit</div>
                        <div class="trust-item"><span class="check">✓</span> Erfahrung, Struktur und kreative Ideen</div>
                        <div class="trust-item"><span class="check">✓</span> Verlässliche Planung bis zum Hochzeitstag</div>
                    </div>"""

stray_replacement = """    <div class="trust-item reveal delay-4"><span class="check">✓</span> würdevoller Auftritt bei der Trauerfeier</div>
                        <div class="trust-item reveal delay-5"><span class="check">✓</span> Abstimmung mit Familie und Bestattungsinstitut möglich</div>
                    </div>"""

if stray_elements in content:
    content = content.replace(stray_elements, stray_replacement)


# Also ensure the slogan at the end of Vertrauen is right
slogan_old = '<p class="slogan highlight-slogan-light">Weil eure Liebe eine Zeremonie verdient, die genauso besonders ist wie ihr.</p>'
slogan_new = '<p class="slogan highlight-slogan-light">Weil jeder Mensch einen Abschied verdient, der seine Geschichte würdigt.</p>'
content = content.replace(slogan_old, slogan_new)

# Add class grayscale to portrait image in trauerreden so it fits better
content = content.replace('class="rounded-image shadow-light portrait"', 'class="rounded-image shadow-light portrait" style="filter: grayscale(80%);"')

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(content)
