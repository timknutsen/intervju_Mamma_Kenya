from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs" / "mamma-mau-mau-review.pdf"


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=styles["Title"],
            fontName="Times-Bold",
            fontSize=24,
            leading=30,
            textColor=colors.HexColor("#4B2E1E"),
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSub",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#705344"),
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=colors.HexColor("#5A3825"),
            spaceBefore=10,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["BodyText"],
            fontName="Times-Roman",
            fontSize=11,
            leading=16,
            textColor=colors.HexColor("#2B211B"),
            alignment=TA_JUSTIFY,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Note",
            parent=styles["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=9.5,
            leading=13,
            textColor=colors.HexColor("#5A4A40"),
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Speaker",
            parent=styles["BodyText"],
            fontName="Times-Roman",
            fontSize=11,
            leading=16,
            textColor=colors.HexColor("#2B211B"),
            leftIndent=8,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Small",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=12,
            textColor=colors.HexColor("#44352C"),
            spaceAfter=4,
        )
    )
    return styles


def on_page(canvas, doc):
    page_w, page_h = A4
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#FBF4EA"))
    canvas.rect(0, 0, page_w, page_h, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#D8C1A8"))
    canvas.rect(18 * mm, page_h - 16 * mm, page_w - 36 * mm, 3, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#8A6B57"))
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(page_w - 18 * mm, 12 * mm, f"Side {doc.page}")
    canvas.restoreState()


def speaker_line(styles, who, text):
    return Paragraph(f"<b>{who}:</b> {text}", styles["Speaker"])


def bullet_table(styles, items):
    rows = [[Paragraph(f"• {item}", styles["Body"])] for item in items]
    table = Table(rows, colWidths=[160 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4E8D9")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D2B79C")),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#E6D2BC")),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def story():
    s = build_styles()
    parts = []

    parts.append(Spacer(1, 28 * mm))
    parts.append(Paragraph("Mamma i Kenya", s["CoverTitle"]))
    parts.append(Paragraph("Kort samtale om Mau Mau, renskrevet til gjennomgang", s["CoverTitle"]))
    parts.append(Spacer(1, 6 * mm))
    parts.append(
        Paragraph(
            "Laget fra den første testfilen, et sidespor i intervjuet. "
            "Teksten under er lett renskrevet for lesbarhet, ikke en ord-for-ord-transkripsjon.",
            s["CoverSub"],
        )
    )
    parts.append(Spacer(1, 10 * mm))
    parts.append(
        bullet_table(
            s,
            [
                "Opptak: «Mamma intervju Sidespor 1 - Mau Mau»",
                "Varighet: ca. 6 minutter",
                "Formål: lese sammen, rette faktafeil og fange opp navn, steder og minner",
            ],
        )
    )
    parts.append(Spacer(1, 10 * mm))
    parts.append(
        Paragraph(
            "Til mamma: Dette er et arbeidsdokument. Det viktigste er ikke perfekt språk, "
            "men at minnene og nyansene dine kommer tydelig fram.",
            s["Note"],
        )
    )
    parts.append(PageBreak())

    parts.append(Paragraph("Renskrevet samtale", s["Section"]))
    parts.append(
        Paragraph(
            "Denne delen bygger på AI-transkripsjonen, men er glattet ut der lydmodellen hørte feil. "
            "Noen korte avbrytelser og gjentakelser er tatt bort for å gjøre teksten lettere å lese.",
            s["Note"],
        )
    )

    convo = [
        ("Tim", "Jeg har et lite sidespor om Mau Mau. Kan vi ta det kort?"),
        ("Mamma", "Ja, men jeg er ikke historiker, så det er greit å si med en gang."),
        ("Mamma", "Det jeg har forsøkt, er å tenke litt rundt det og sette meg litt inn i det i ettertid."),
        ("Mamma", "Kenya var jo en britisk koloni. Europeiske settlere fikk land, og mye av jorda ble tatt fra afrikanerne."),
        ("Tim", "Med militær makt?"),
        ("Mamma", "Det vet jeg ikke godt nok, men kolonimakten mente i hvert fall at de visste bedre hvordan jorda skulle brukes. Her må vi grave litt dypere senere."),
        ("Mamma", "Jeg tror også britene satte folkegrupper opp mot hverandre og støttet noen framfor andre."),
        ("Mamma", "Slik jeg har forstått det, vokste Mau Mau fram som et voldelig opprør, særlig med røtter i Kikuyu-miljøer."),
        ("Mamma", "Samtidig var ikke alle kikuyuer på samme side. Noen var lojale mot settlerne og jobbet på farmene, andre støttet opprøret."),
        ("Mamma", "Jeg har lest at folk kunne bli presset eller påvirket inn i det, og at volden ble veldig brutal."),
        ("Mamma", "Da svarte myndighetene hardt. Det fantes både militære tiltak og en sivil beredskap blant settlerne."),
        ("Mamma", "Jakob var en del av dette miljøet, og et tydelig barndomsminne for meg er at han alltid gikk bevæpnet."),
        ("Mamma", "Jeg husker også farmen som sterkt sikret: piggtråd rundt våningshuset, port, vaktmann og hunder om natten."),
        ("Tim", "Men du har ikke egne minner fra selve opprøret?"),
        ("Mamma", "Nei. Jeg ble født i 1954, så det er for tidlig for at jeg kan huske den første og mest intense perioden."),
        ("Tim", "Så mye av dette er noe du har fått fortalt senere?"),
        ("Mamma", "Ja, enten fortalt i familien eller lest i ettertid."),
        ("Tim", "Når ble Kenya selvstendig?"),
        ("Mamma", "Ikke før i 1963."),
        ("Tim", "Da gir det mening å fylle inn litt historisk bakgrunn rundt minnene dine."),
        ("Mamma", "Ja, det tror jeg er lurt."),
    ]
    parts.extend(speaker_line(s, who, text) for who, text in convo)

    parts.append(Spacer(1, 6 * mm))
    parts.append(Paragraph("Kort historisk ramme", s["Section"]))
    parts.append(
        Paragraph(
            "For å lese samtalen ryddig kan det være nyttig å skille mellom tre lag: "
            "1) det mamma faktisk husker fra barndommen, 2) det hun senere fikk fortalt i familien, "
            "og 3) historisk kontekst fra kilder.",
            s["Body"],
        )
    )
    parts.append(
        bullet_table(
            s,
            [
                "Britannica beskriver Mau Mau-opprøret som en konflikt i Britisk Kenya fra 1952 til 1960, hovedsakelig drevet av kikuyu-forkjempere som ville ta tilbake land og frihet.",
                "Samtidig understreker samme kilde at konflikten også ble en bitter intern splittelse, særlig blant kikuyuer, mellom opprørere og lojale grupper.",
                "Britiske myndigheter svarte med svært hard motmakt. Kildene peker både på militære operasjoner, internering og leirsystemer.",
                "Kenya ble selvstendig 12. desember 1963. Det betyr at mamma ble født midt under unntakstilstanden, men var fortsatt et lite barn da de tidlige og mest dramatiske årene pågikk.",
            ],
        )
    )

    parts.append(Spacer(1, 6 * mm))
    parts.append(Paragraph("Punkter å sjekke med mamma", s["Section"]))
    parts.append(
        bullet_table(
            s,
            [
                "Hvem er Jakob i denne sammenhengen, og hvilken rolle hadde han på farmen?",
                "Hva het farmen, og hvor i Kenya lå den?",
                "Hvilke konkrete ting husker mamma selv: piggtråd, port, vakthold, hunder, våpen?",
                "Hva i denne samtalen er familiens fortelling, og hva er mamma sine egne minner?",
                "Hvilke navn eller ord må rettes: Mau Mau, Kikuyu, britiske myndigheter, årstall?",
            ],
        )
    )

    parts.append(Spacer(1, 6 * mm))
    parts.append(Paragraph("Kildegrunnlag", s["Section"]))
    sources = [
        "Encyclopaedia Britannica, «Mau Mau Rebellion», oppdatert 9. januar 2026. https://www.britannica.com/event/Mau-Mau-Rebellion",
        "Encyclopaedia Britannica, «What led to Kenya's independence in 1963?», åpnet 7. mars 2026. https://www.britannica.com/question/What-led-to-Kenyas-independence-in-1963",
        "U.S. Office of the Historian, «Kenya», åpnet 7. mars 2026. https://history.state.gov/countries/kenya",
        "The National Archives (UK), katalogpost om «Rehabilitation camp at Athi River and the re-education of Kikuyu tainted with Mau Mau», åpnet 7. mars 2026. https://discovery.nationalarchives.gov.uk/details/r/C11107560",
    ]
    for src in sources:
        parts.append(Paragraph(src, s["Small"]))

    parts.append(Spacer(1, 4 * mm))
    parts.append(
        Paragraph(
            "Arbeidsnotat: I samtalen brukes enkelte ord og forklaringer slik de sies i familien eller i eldre framstillinger. "
            "Den historiske forskningen er mer nyansert enn kolonitidens språkbruk. Derfor er denne teksten ment som et lesedokument til gjennomgang, ikke som endelig historisk framstilling.",
            s["Note"],
        )
    )

    return parts


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
        topMargin=20 * mm,
        bottomMargin=18 * mm,
        title="Mamma i Kenya - Mau Mau review",
        author="Codex",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="warm", frames=[frame], onPage=on_page)])
    doc.build(story())
    print(OUTPUT)


if __name__ == "__main__":
    main()
