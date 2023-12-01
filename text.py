import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

if __name__ == "__main__":
    pdf_file_path = '/Users/rashinfarahani/Downloads/My_CV.pdf'
    extracted_text = extract_text_from_pdf(pdf_file_path)

    # Print the extracted text
    print(extracted_text)

    # Save the extracted text to a text file
    output_path = '/Users/rashinfarahani/Downloads/extracted_text.txt'
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(extracted_text)
