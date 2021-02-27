import PyPDF2
a = PyPDF2.PdfFileReader('DBMS_PROJECT_BANKING SYSTEM_1961055.pdf')
print(a.documentInfo)
print(a.getNumPages())

str = ''
for i in range(1,20):
    str += a.getPage(i).extractText()

with open('pdf.txt','w',encoding='utf-8') as f:
    f.write(str)