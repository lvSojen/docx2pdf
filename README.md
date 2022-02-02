# docx2pdf
Docx2PDF converter, It can convert every .docx file to .pdf file under current directory to a target folder(target folder is hard-coded but it can be user defined)

In order to use Docx2PDF, you will need to

1. install Python
https://www.python.org/downloads/

2. install docx2pdf python package
in cmd(Windows Command Prompt) type
pip install docx2pdf

3. execute auto_docx2pdf or folder_docx2pdf, your og .docx files will remain untouched
auto_docx2pdf: convert every .docx to .pdf to a hard-coded folder named "output"
folder_docx2pdf: prompt user for the folder's name, other than that same as auto_docx2pdf.pdf
