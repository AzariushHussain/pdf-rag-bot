import fitz

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as pdf_doc:
        for page_num in range(pdf_doc.page_count):
            page = pdf_doc.load_page(page_num)
            text += page.get_text("text")
    return text


def truncate_text(text):
    last_period = text.rfind('.')
    if last_period != -1:
        return text[:last_period + 1]
    return text  