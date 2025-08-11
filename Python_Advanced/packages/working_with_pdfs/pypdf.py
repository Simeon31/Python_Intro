import PyPDF2

with open("first.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)

# Merging pdfs
merger = PyPDF2.PdfMerger()
file_names = ["first.pdf", "second.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("merged.pdf")