"""Gera memorando em HTML/PDF e DOCX a partir do Markdown (subconjunto simples).

Uso: python3 build.py
Requer o Chrome/Chromium headless para o PDF (variável CHROME ou caminho padrão).
"""
import html
import os
import re
import subprocess
import zipfile
from xml.sax.saxutils import escape as xesc

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "memorando-executivo-meridiano.md")
BASE = os.path.join(HERE, "memorando-executivo-meridiano")
CHROME = os.environ.get("CHROME", "/inner_container/opt/playwright/chromium-1232/chrome-linux64/chrome")


# ---------- parser ----------
def parse(md):
    blocks, lines, i = [], md.splitlines(), 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1
            continue
        if ln.strip() == "<!-- pagebreak -->":
            blocks.append(("pagebreak", None)); i += 1; continue
        m = re.match(r"^(#{1,3}) (.*)", ln)
        if m:
            blocks.append(("h%d" % len(m.group(1)), m.group(2))); i += 1; continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append(("table", rows)); continue
        if re.match(r"^(- |\d+\. )", ln):
            ordered = bool(re.match(r"^\d+\. ", ln))
            items = []
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i]).strip()); i += 1
            blocks.append(("ol" if ordered else "ul", items)); continue
        para = [ln.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||- |\d+\. |<!--)", lines[i]):
            para.append(lines[i].strip()); i += 1
        blocks.append(("p", " ".join(para)))
    return blocks


def runs(text):
    """Divide texto em [(trecho, negrito)]."""
    out = []
    for k, part in enumerate(re.split(r"\*\*", text)):
        if part:
            out.append((part, k % 2 == 1))
    return out


# ---------- HTML / PDF ----------
CSS = """
@page { size: A4; margin: 1.6cm 1.7cm 1.6cm 1.7cm; }
body { font-family: 'Liberation Sans', Arial, Helvetica, sans-serif; font-size: 9.6pt; line-height: 1.32; color: #1a1a1a; }
h1 { font-size: 15pt; margin: 0 0 6px 0; color: #0b3a5b; letter-spacing: 1px; }
h2 { font-size: 11.5pt; color: #0b3a5b; border-bottom: 1.5px solid #0b3a5b; padding-bottom: 2px; margin: 11px 0 5px 0; }
h3 { font-size: 10pt; color: #0b3a5b; margin: 8px 0 3px 0; }
p { margin: 0 0 5px 0; text-align: justify; }
ul, ol { margin: 0 0 5px 0; padding-left: 18px; }
li { margin-bottom: 2px; text-align: justify; }
table { border-collapse: collapse; width: 100%; margin: 3px 0 7px 0; font-size: 8.4pt; line-height: 1.22; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th, td { border: 0.6px solid #9aa9b5; padding: 2.5px 4px; vertical-align: top; text-align: left; }
th { background: #dfe8ef; }
table.meta td, table.meta th { border: none; padding: 1px 4px; font-size: 9.4pt; }
table.meta { border-top: 2px solid #0b3a5b; border-bottom: 2px solid #0b3a5b; margin-bottom: 8px; }
table.meta thead { display: none; }
.annex table { font-size: 7.7pt; }
.annex p { font-size: 8.8pt; }
.pb { page-break-before: always; }
"""


def h_inline(text):
    return "".join("<strong>%s</strong>" % html.escape(t) if b else html.escape(t) for t, b in runs(text))


def to_html(blocks):
    body, first_table, annex = [], True, False
    for kind, val in blocks:
        if kind == "pagebreak":
            body.append('<div class="pb"></div><div class="annex">'); annex = True
        elif kind in ("h1", "h2", "h3"):
            body.append("<%s>%s</%s>" % (kind, h_inline(val), kind))
        elif kind == "p":
            body.append("<p>%s</p>" % h_inline(val))
        elif kind in ("ul", "ol"):
            body.append("<%s>%s</%s>" % (kind, "".join("<li>%s</li>" % h_inline(x) for x in val), kind))
        elif kind == "table":
            cls = ' class="meta"' if first_table else ""
            first_table = False
            head = "".join("<th>%s</th>" % h_inline(c) for c in val[0])
            rows = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % h_inline(c) for c in r) for r in val[1:])
            body.append("<table%s><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (cls, head, rows))
    if annex:
        body.append("</div>")
    return ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
            "<title>Memorando Executivo - Grupo Meridiano</title><style>%s</style></head><body>%s</body></html>"
            % (CSS, "\n".join(body)))


# ---------- DOCX ----------
W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'


def d_runs(text, size=None, color=None):
    out = []
    for t, b in runs(text):
        rpr = ""
        if b: rpr += "<w:b/>"
        if color: rpr += '<w:color w:val="%s"/>' % color
        if size: rpr += '<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (size, size)
        out.append('<w:r><w:rPr>%s</w:rPr><w:t xml:space="preserve">%s</w:t></w:r>' % (rpr, xesc(t)))
    return "".join(out)


def d_par(text, style=None, size=None, jc=None, num=None, after=80, color=None, keep=False):
    ppr = ""
    if style: ppr += '<w:pStyle w:val="%s"/>' % style
    if keep: ppr += "<w:keepNext/>"
    if num is not None: ppr += '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="%d"/></w:numPr>' % num
    ppr += '<w:spacing w:after="%d" w:line="252" w:lineRule="auto"/>' % after
    if jc: ppr += '<w:jc w:val="%s"/>' % jc
    return "<w:p><w:pPr>%s</w:pPr>%s</w:p>" % (ppr, d_runs(text, size, color))


def d_table(rows, size, meta=False):
    ncol = max(len(r) for r in rows)
    width = 9900
    first_w = 1500 if meta else None
    if meta:
        widths = [first_w, width - first_w]
        rows = rows[1:]
    else:
        widths = [width // ncol] * ncol
    borders = "" if meta else (
        "<w:tblBorders>" + "".join('<w:%s w:val="single" w:sz="4" w:color="9AA9B5"/>' % s
                                   for s in ("top", "left", "bottom", "right", "insideH", "insideV")) + "</w:tblBorders>")
    xml = ['<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/>%s<w:tblLayout w:type="autofit"/>'
           '<w:tblCellMar><w:left w:w="60" w:type="dxa"/><w:right w:w="60" w:type="dxa"/></w:tblCellMar></w:tblPr>' % (width, borders)]
    xml.append("<w:tblGrid>%s</w:tblGrid>" % "".join('<w:gridCol w:w="%d"/>' % w for w in widths))
    for ri, r in enumerate(rows):
        hdr = ri == 0 and not meta
        xml.append("<w:tr>%s" % ("<w:trPr><w:tblHeader/></w:trPr>" if hdr else ""))
        for ci in range(ncol):
            c = r[ci] if ci < len(r) else ""
            shade = '<w:shd w:val="clear" w:color="auto" w:fill="DFE8EF"/>' if hdr else ""
            txt = "**%s**" % c if hdr and not c.startswith("**") else c
            xml.append('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>%s</w:tcPr>%s</w:tc>'
                       % (widths[ci], shade, d_par(txt, size=size, after=0)))
        xml.append("</w:tr>")
    xml.append("</w:tbl>")
    return "".join(xml) + d_par("", size=6, after=60)


def to_docx(blocks, path):
    body, first_table, annex = [], True, False
    for kind, val in blocks:
        if kind == "pagebreak":
            body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>'); annex = True
        elif kind == "h1":
            body.append(d_par(val, style="Heading1", keep=True))
        elif kind == "h2":
            body.append(d_par(val, style="Heading2", keep=True))
        elif kind == "h3":
            body.append(d_par(val, style="Heading3", keep=True))
        elif kind == "p":
            body.append(d_par(val, jc="both", size=17 if annex else None))
        elif kind in ("ul", "ol"):
            for x in val:
                body.append(d_par(x, jc="both", num=1 if kind == "ul" else 2, after=40))
        elif kind == "table":
            body.append(d_table(val, size=19 if first_table else (14 if annex else 16), meta=first_table))
            first_table = False
    sect = ('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
            '<w:pgMar w:top="907" w:right="964" w:bottom="907" w:left="964" w:header="0" w:footer="0" w:gutter="0"/></w:sectPr>')
    document = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document %s><w:body>%s%s</w:body></w:document>' % (
        W, "".join(body), sect)
    styles = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles %s>'
              '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'
              '<w:sz w:val="19"/><w:szCs w:val="19"/><w:lang w:val="pt-BR"/></w:rPr></w:rPrDefault></w:docDefaults>'
              '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>'
              '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/>'
              '<w:pPr><w:spacing w:after="100"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:color w:val="0B3A5B"/><w:sz w:val="30"/></w:rPr></w:style>'
              '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/>'
              '<w:pPr><w:pBdr><w:bottom w:val="single" w:sz="8" w:space="1" w:color="0B3A5B"/></w:pBdr><w:spacing w:before="200" w:after="80"/><w:outlineLvl w:val="1"/></w:pPr>'
              '<w:rPr><w:b/><w:color w:val="0B3A5B"/><w:sz w:val="23"/></w:rPr></w:style>'
              '<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/>'
              '<w:pPr><w:spacing w:before="120" w:after="40"/><w:outlineLvl w:val="2"/></w:pPr><w:rPr><w:b/><w:color w:val="0B3A5B"/><w:sz w:val="20"/></w:rPr></w:style>'
              '</w:styles>') % W
    numbering = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:numbering %s>'
                 '<w:abstractNum w:abstractNumId="1"><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/>'
                 '<w:lvlText w:val="\u2022"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="360" w:hanging="240"/></w:pPr></w:lvl></w:abstractNum>'
                 '<w:abstractNum w:abstractNumId="2"><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="decimal"/>'
                 '<w:lvlText w:val="%%1."/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="360" w:hanging="300"/></w:pPr></w:lvl></w:abstractNum>'
                 '<w:num w:numId="1"><w:abstractNumId w:val="1"/></w:num><w:num w:numId="2"><w:abstractNumId w:val="2"/></w:num>'
                 '</w:numbering>') % W
    ctypes = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
              '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
              '<Default Extension="xml" ContentType="application/xml"/>'
              '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
              '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
              '<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>'
              '</Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            '</Relationships>')
    doc_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
                '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>'
                '</Relationships>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", ctypes)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", document)
        z.writestr("word/styles.xml", styles)
        z.writestr("word/numbering.xml", numbering)
        z.writestr("word/_rels/document.xml.rels", doc_rels)


def main():
    blocks = parse(open(SRC, encoding="utf-8").read().replace("R$ ", "R$\u00a0"))
    with open(BASE + ".html", "w", encoding="utf-8") as f:
        f.write(to_html(blocks))
    to_docx(blocks, BASE + ".docx")
    subprocess.run(["node", os.path.join(HERE, "pdf.js"), BASE + ".html", BASE + ".pdf"], check=True)
    # Conferência de páginas: corpo e anexos separadamente.
    cut = next(i for i, b in enumerate(blocks) if b[0] == "pagebreak")
    tmp_html, tmp_pdf = "/tmp/_corpo.html", "/tmp/_corpo.pdf"
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(to_html(blocks[:cut]))
    subprocess.run(["node", os.path.join(HERE, "pdf.js"), tmp_html, tmp_pdf], check=True)
    count = lambda p: len(re.findall(rb"/Type\s*/Page[^s]", open(p, "rb").read()))
    total, corpo = count(BASE + ".pdf"), count(tmp_pdf)
    print("páginas: total=%d corpo=%d anexos=%d" % (total, corpo, total - corpo))


if __name__ == "__main__":
    main()
