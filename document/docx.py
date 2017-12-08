from docx import Document
from docx.shared import Inches
from document.template import create_template
from document.doc_path import set_path


def create_document(filename, urls):
    word_doc = Document()

    # if not isinstance(urls, list):
    #     raise TypeError("urls must be a list")

    # Create doc_section for every URL passed in
    for url in urls:
        doc_section = create_template(url)
        create_section(word_doc, doc_section)

    path = set_path(filename)
    word_doc.save(path)


def create_section(word_doc, doc_section):
    ds = doc_section
    word_doc.add_heading(ds.heading, 0)

    word_doc.add_paragraph().add_run('Title:').bold = True
    word_doc.add_paragraph(ds.title)

    word_doc.add_paragraph().add_run('Description:').bold = True
    word_doc.add_paragraph(ds.description)

    word_doc.add_paragraph().add_run('Top Ten Keywords:').bold = True
    add_top_ten_words(word_doc, ds.top_ten_words)
    # Add blank paragraph under table
    word_doc.add_paragraph()

    word_doc.add_paragraph().add_run('Content:').bold = True
    add_page_content(word_doc, ds.content)

    word_doc.add_page_break()


def add_top_ten_words(document, top_ten_words):
    table = document.add_table(rows=1, cols=3, style='Table Grid')
    set_column_widths(table)
    hdr_cells = table.rows[0].cells
    hdr_cells[1].text = 'Keyword'
    hdr_cells[2].text = 'Frequency'

    for idx, item in enumerate(top_ten_words, start=1):
        word, count = item
        row_cells = table.add_row().cells
        row_cells[0].text = str(idx)
        row_cells[1].text = word
        row_cells[2].text = str(count)


def add_page_content(document, page_content):
    for item in page_content:
        # Unpack tuple
        tag, content = item
        # If header tag add text and header type
        if tag[0] == 'h':
            header = f'{content} - ({tag})'
            document.add_heading(header, level=1)
        # If any list item add bullet point
        elif tag == 'li':
            document.add_paragraph(content, style='List Bullet')
        # Else paragraph, no formatting needed
        else:
            document.add_paragraph(content)


# Need to edit column width and every cell inside for width to stick. See below:
# https://stackoverflow.com/questions/43051462/python-docx-how-to-set-cell-width-in-tables
def set_column_widths(table):
    widths = (Inches(0.8), Inches(1.6), Inches(1))

    for column, width in zip(table.columns, widths):
        column.width = width

    for row in table.rows:
        for cell, width in zip(row.cells, widths):
            cell.width = width
