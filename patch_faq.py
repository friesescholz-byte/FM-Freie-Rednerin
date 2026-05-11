import re

with open('trauerreden.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<span class="section-tag">FAQ</span>\s*<h2>.*?</h2>', '<span class="section-tag">FAQ</span>\n                    <h2>Häufige Fragen zur persönlichen Trauerrede</h2>', content, count=1)

content = re.sub(r'<div class="faq-container reveal delay-1">.*?</div>\s*</div>\s*</section>', '''<div class="faq-container reveal delay-1">
                    <div class="faq-item">
                        <div class="faq-question">
                            <h3>Wie läuft das Trauergespräch ab?</h3>
                            <span class="faq-icon">+</span>
                        </div>
                        <div class="faq-answer">
                            <p>Das Gespräch findet in ruhiger Atmosphäre statt – persönlich, telefonisch oder nach Absprache auch online. Wir sprechen über den verstorbenen Menschen, wichtige Lebensstationen, besondere Erinnerungen und alles, was Ihnen für die Rede wichtig ist.</p>
                        </div>
                    </div>
                    
                    <div class="faq-item">
                        <div class="faq-question">
                            <h3>Was ist, wenn uns selbst die Worte fehlen?</h3>
                            <span class="faq-icon">+</span>
                        </div>
                        <div class="faq-answer">
                            <p>Das ist vollkommen verständlich. Sie müssen nichts vorbereiten oder perfekt formulieren. Ich stelle behutsame Fragen und helfe Ihnen dabei, Erinnerungen und Gedanken zu ordnen.</p>
                        </div>
                    </div>
                    
                    <div class="faq-item">
                        <div class="faq-question">
                            <h3>Kann die Rede auch persönliche und leichte Momente enthalten?</h3>
                            <span class="faq-icon">+</span>
                        </div>
                        <div class="faq-answer">
                            <p>Ja. Eine Trauerrede darf neben Traurigkeit auch Dankbarkeit, Wärme und ein leises Lächeln enthalten. Oft sind es gerade kleine persönliche Geschichten, die einen Menschen besonders nahbar machen.</p>
                        </div>
                    </div>
                    
                    <div class="faq-item">
                        <div class="faq-question">
                            <h3>Stimmen Sie sich mit dem Bestattungsinstitut ab?</h3>
                            <span class="faq-icon">+</span>
                        </div>
                        <div class="faq-answer">
                            <p>Auf Wunsch ja. Ich kann mich mit dem Bestattungsinstitut oder anderen Beteiligten abstimmen, damit der Ablauf der Trauerfeier ruhig und stimmig gestaltet wird.</p>
                        </div>
                    </div>
                    
                    <div class="faq-item">
                        <div class="faq-question">
                            <h3>Kann Musik oder ein Ritual eingebunden werden?</h3>
                            <span class="faq-icon">+</span>
                        </div>
                        <div class="faq-answer">
                            <p>Ja. Musik, persönliche Beiträge, Erinnerungsrituale oder besondere Symbole können Teil der Zeremonie sein. Gemeinsam finden wir heraus, was zur Familie und zum verstorbenen Menschen passt.</p>
                        </div>
                    </div>
                    
                    <div class="faq-item">
                        <div class="faq-question">
                            <h3>Wie kurzfristig ist eine Trauerrede möglich?</h3>
                            <span class="faq-icon">+</span>
                        </div>
                        <div class="faq-answer">
                            <p>Trauerfeiern finden oft kurzfristig statt. Melden Sie sich gerne direkt bei mir, damit wir gemeinsam schauen können, was zeitlich möglich ist.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>''', content, count=1, flags=re.DOTALL)

with open('trauerreden.html', 'w', encoding='utf-8') as f:
    f.write(content)
