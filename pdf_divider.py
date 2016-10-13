from PyPDF2 import PdfFileMerger,PdfFileReader,PdfFileWriter
import codecs
import math  

original_file = PdfFileReader(open("SDPM.pdf",'rb'))

 # a writer
pdfWriter=PdfFileWriter()

start_page = 1
end_page = 600
counter = 0


pages = end_page-start_page;
diff = pages/24

diff = math.ceil(diff)

print (diff)



for x in range(counter,counter+diff):
	count = str(x)
	start_page_new = start_page-1
	if(start_page+23<end_page):
		end_page_new = start_page+23
	else:
		end_page_new = end_page
	 	
	for i in range(start_page_new,end_page_new):
		original_page = original_file.getPage(i)
		pdfWriter.addPage(original_page)
	start_page = end_page_new+1	
	output_file_name = "sdpm_book_print_"+count+".pdf"
	outfp=open(output_file_name,'wb')
	pdfWriter.write(outfp)
	pdfWriter = None;
	pdfWriter=PdfFileWriter()