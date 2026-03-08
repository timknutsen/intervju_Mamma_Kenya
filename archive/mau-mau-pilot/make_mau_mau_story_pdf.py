from pathlib import Path

from reportlab.graphics.shapes import Circle, Drawing, Line, Rect, String
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUTPUT = ROOT / "outputs" / "mamma-mau-mau-story-english.pdf"


def styles():
    s = getSampleStyleSheet()
    s.add(
        ParagraphStyle(
            name="StoryTitle",
            parent=s["Title"],
            fontName="Times-Bold",
            fontSize=26,
            leading=31,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#2E221C"),
            spaceAfter=6,
        )
    )
    s.add(
        ParagraphStyle(
            name="Deck",
            parent=s["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#5B4A3E"),
            spaceAfter=8,
        )
    )
    s.add(
        ParagraphStyle(
            name="Section",
            parent=s["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=colors.HexColor("#513628"),
            spaceBefore=10,
            spaceAfter=5,
        )
    )
    s.add(
        ParagraphStyle(
            name="Story",
            parent=s["BodyText"],
            fontName="Times-Roman",
            fontSize=11.5,
            leading=17,
            alignment=TA_JUSTIFY,
            textColor=colors.HexColor("#231A15"),
            spaceAfter=7,
        )
    )
    s.add(
        ParagraphStyle(
            name="Caption",
            parent=s["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=8.8,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#6A5748"),
            spaceAfter=6,
        )
    )
    s.add(
        ParagraphStyle(
            name="Small",
            parent=s["BodyText"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=12,
            textColor=colors.HexColor("#493C33"),
            spaceAfter=3,
        )
    )
    s.add(
        ParagraphStyle(
            name="Note",
            parent=s["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=9.4,
            leading=13,
            textColor=colors.HexColor("#645247"),
            spaceAfter=5,
        )
    )
    return s


def on_page(canvas, doc):
    page_w, page_h = A4
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#FCF6EE"))
    canvas.rect(0, 0, page_w, page_h, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#C9A27E"))
    canvas.rect(16 * mm, page_h - 14 * mm, page_w - 32 * mm, 2, fill=1, stroke=0)
    canvas.setFont("Helvetica", 8.5)
    canvas.setFillColor(colors.HexColor("#7A6455"))
    canvas.drawRightString(page_w - 16 * mm, 10 * mm, f"Page {doc.page}")
    canvas.restoreState()


def scaled_image(path: Path, max_width_mm: float, max_height_mm: float):
    img = Image(str(path))
    iw, ih = img.imageWidth, img.imageHeight
    scale = min((max_width_mm * mm) / iw, (max_height_mm * mm) / ih)
    img.drawWidth = iw * scale
    img.drawHeight = ih * scale
    return img


def info_box(style, title, items):
    rows = [[Paragraph(f"<b>{title}</b>", style)]]
    rows.extend([[Paragraph(item, style)] for item in items])
    tbl = Table(rows, colWidths=[165 * mm])
    tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8D4BF")),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F5EADC")),
                ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#C8AB8D")),
                ("INNERGRID", (0, 1), (-1, -1), 0.25, colors.HexColor("#E2CCB5")),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return tbl


def timeline():
    d = Drawing(460, 90)
    d.add(Rect(0, 20, 460, 50, fillColor=colors.HexColor("#F4E6D7"), strokeColor=colors.HexColor("#D3B69A")))
    d.add(Line(30, 45, 430, 45, strokeColor=colors.HexColor("#7F5D47"), strokeWidth=2))
    points = [
        (70, "1952", "Emergency declared"),
        (190, "1954", "Mother born"),
        (315, "1960", "Emergency ends"),
        (400, "1963", "Kenya independent"),
    ]
    for x, year, label in points:
        d.add(Circle(x, 45, 6, fillColor=colors.HexColor("#9E6F51"), strokeColor=colors.white))
        d.add(String(x - 16, 58, year, fontName="Helvetica-Bold", fontSize=10, fillColor=colors.HexColor("#3B2B21")))
        d.add(String(x - 28, 27, label, fontName="Helvetica", fontSize=8.5, fillColor=colors.HexColor("#4E3D33")))
    return d


def build_story():
    s = styles()
    parts = []

    parts.append(Spacer(1, 10 * mm))
    parts.append(scaled_image(ASSETS / "nairobi-1950.jpg", 150, 78))
    parts.append(Spacer(1, 4 * mm))
    parts.append(Paragraph("A Small Story from Kenya", s["StoryTitle"]))
    parts.append(
        Paragraph(
            "Based on a short side-conversation between mother and son, rewritten in English as a gentle narrative with historical backdrop.",
            s["Deck"],
        )
    )
    parts.append(
        Paragraph(
            "This is not a strict transcript. It is a readable story built from the first six-minute test recording.",
            s["Note"],
        )
    )
    parts.append(
        Paragraph(
            "For a few minutes, the interview turns away from personal chronology and toward the atmosphere surrounding one of the great wounds of colonial Kenya: the Mau Mau uprising. "
            "The mother pauses almost immediately to qualify what she is saying. She is not a historian, she says. She remembers fragments, family stories, and things she later read for herself. "
            "That hesitation becomes part of the story. It tells us how memory works. Some things are lived directly. Some are inherited. Some arrive later, when a child has become an adult and starts asking what the adults around her had once been afraid of.",
            s["Story"],
        )
    )
    parts.append(PageBreak())

    parts.append(Paragraph("The Story", s["Section"]))
    parts.append(
        Paragraph(
            "She describes Kenya as the world into which she was born in 1954: a British colony where settlers had taken land and built lives on African soil. "
            "In her telling, the violence is not abstract. It appears in practical details: barbed wire around the house, a guarded gate, dogs at night, and a man named Jakob who, in her memory, was always armed. "
            "These are not the grand symbols of history books. They are the domestic architecture of fear.",
            s["Story"],
        )
    )
    parts.append(
        Paragraph(
            "The conversation circles around Mau Mau as something dangerous and divisive, but also something that cannot be understood from only one side. "
            "She senses that the colonial state set groups against one another. She recalls that not everyone in the same community stood together. "
            "Some people worked for settlers. Others resisted. Even inside her brief recollection there is already a more complicated truth: the conflict was not a simple line between British and African, but a struggle over land, loyalty, survival, and power.",
            s["Story"],
        )
    )
    parts.append(
        Paragraph(
            "Her own position in time matters. She was born after the uprising had already begun. She does not claim vivid first-hand memories of its earliest and bloodiest phase. "
            "What she does remember is the atmosphere left behind by it. Security. Anxiety. Adults who carried weapons. A household arranged as if danger might arrive in the dark. "
            "The son, asking questions from the present, pushes gently toward the historical frame. When did it begin? When did it end? When did Kenya become independent? "
            "Step by step, private memory opens into public history.",
            s["Story"],
        )
    )
    parts.append(
        Paragraph(
            "Seen that way, the power of the conversation lies not in perfect factual precision, but in the meeting point between lived memory and researched context. "
            "The mother does not offer a finished account. She offers something more valuable for a family history: a remembered atmosphere, a moral uncertainty, and a few solid images that still endure.",
            s["Story"],
        )
    )

    parts.append(Spacer(1, 4 * mm))
    parts.append(scaled_image(ASSETS / "kar-mau-mau.jpg", 120, 70))
    parts.append(
        Paragraph(
            "A period image from the Emergency years in Kenya. Included here as historical atmosphere, not as an illustration of the family's exact experience. "
            "Source: Wikimedia Commons, “KAR Mau Mau”.",
            s["Caption"],
        )
    )

    parts.append(PageBreak())

    parts.append(Paragraph("Historical Backdrop", s["Section"]))
    parts.append(
        Paragraph(
            "Modern historical summaries describe the Mau Mau conflict as part anti-colonial revolt, part civil conflict within Kenyan society, especially among Kikuyu communities. "
            "Britannica places the main Emergency period between 1952 and 1960, while Kenya achieved independence on 12 December 1963. "
            "That means your mother was born into the middle of the Emergency and left for Norway only a few years after independence.",
            s["Story"],
        )
    )
    parts.append(Spacer(1, 2 * mm))
    parts.append(timeline())
    parts.append(Spacer(1, 5 * mm))
    parts.append(
        info_box(
            s["Story"],
            "What the research adds",
            [
                "Land was central. The uprising grew in part from dispossession, forced labor structures, and political exclusion under British rule.",
                "The conflict was internally divided. Some Kikuyu joined or supported Mau Mau, while others remained loyal to the colonial administration or were compelled into cooperation.",
                "British counterinsurgency involved mass detention, screening, punishment, and camp systems. Later scholarship and official records complicated the older colonial narrative that framed the struggle only as terrorism.",
                "For family storytelling, this matters because the adults around a child could experience the same years through entirely different roles: settler, employee, loyalist, detainee, observer, child, or dependent.",
            ],
        )
    )
    parts.append(Spacer(1, 5 * mm))
    parts.append(
        Paragraph(
            "The key insight for this project is simple: the family memory does not need to carry the whole burden of historical explanation. "
            "It can do what memory does best, which is to preserve scenes, feelings, and textures. Research can then help place those scenes within the larger history of colonial rule, rebellion, repression, and independence.",
            s["Story"],
        )
    )

    parts.append(PageBreak())
    parts.append(Paragraph("Sources and Image Credits", s["Section"]))
    sources = [
        "Encyclopaedia Britannica, “Mau Mau Rebellion.” https://www.britannica.com/event/Mau-Mau-Rebellion",
        "Encyclopaedia Britannica, “What led to Kenya's independence in 1963?” https://www.britannica.com/question/What-led-to-Kenyas-independence-in-1963",
        "U.S. Office of the Historian, “Kenya.” https://history.state.gov/countries/kenya",
        "The National Archives (UK), Discovery catalogue entry on rehabilitation camps during the Kenya Emergency. https://discovery.nationalarchives.gov.uk/details/r/C11107560",
        "Wikimedia Commons, “File:Nairobi._1950.jpg.” https://commons.wikimedia.org/wiki/File:Nairobi._1950.jpg",
        "Wikimedia Commons, “File:KAR_Mau_Mau.jpg.” https://commons.wikimedia.org/wiki/File:KAR_Mau_Mau.jpg",
    ]
    for src in sources:
        parts.append(Paragraph(src, s["Small"]))
    parts.append(Spacer(1, 4 * mm))
    parts.append(
        Paragraph(
            "Working note: this booklet is intentionally modest in scope. It is based only on the first short test file, then shaped into a readable English story. "
            "If you like the tone, the next step is to build a longer illustrated family narrative from the full interviews.",
            s["Note"],
        )
    )

    return parts


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=18 * mm,
        bottomMargin=16 * mm,
        title="A Small Story from Kenya",
        author="Codex",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=on_page)])
    doc.build(build_story())
    print(OUTPUT)


if __name__ == "__main__":
    main()
