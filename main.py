from selenium import webdriver
from fpdf import FPDF
import unidecode
import os

# driver.close() = close current tab
# driver.quit() = close browser

# These are the inputs for the novel and chapter selection
selected = False
title = input("1: Overgeared \n2: Trash of the Count's Family\n" + "Choose a Novel: ")

while selected == False:
    if title == "1" or title.lower() == "overgeared":
        link = 'https://www.wuxiaworld.com/novel/overgeared/og-chapter-'
        title = "Overgeared"
        selected = True
        os.system('cls')
    elif title == "2" or title.lower() == "trash of the count's family" or title.lower() == "trash":
        link = 'https://www.wuxiaworld.com/novel/trash-of-the-counts-family/tcf-chapter-'
        title = "TCF"
        selected = True
        os.system('cls')
    else:
        os.system('cls')
        title = input("Invalid attempt\n" + "1: Overgeared \n2: Trash of the Count's Family\n" + "Choose a Novel: ")

# This portion starts selenium
chromedriver = 'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=chromedriver, options=options)

x = input("Which chapters do you want to download\n" + "from: ")
x2 = input("to: ")

for i in range(int(x), int((x2)) + 1):
    i = str(i)
    print("Compiling Chapter %s"%i)
    driver.get(link + i)

    if i != x:
        content = content + "\n\n\n" + driver.find_element_by_id("chapter-outer").text.encode('utf8').decode('latin1')
    elif i == x:
        content = driver.find_element_by_id("chapter-outer").text.encode('utf8').decode('latin1')
    os.system('cls')
driver.quit()

    # This portion uses the fpdf library
print("Compiling chapter together")
class PDF(FPDF):
    def chapter_body(self, name):
        # Read text file
        ay = content.encode('utf8').decode('latin1')
        ay = unidecode.unidecode(ay)
        ay = ay.replace("AC/AA", "'")
        # ay = ay.replace ("Chapter %s"%x, "")
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, ay)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of chapter %s)' % i)

    def print_chapter(self, num, name):
        self.add_page()
        self.chapter_body(name)


pdf = PDF()
pdf.print_chapter(i, content)

pdf.output(r'C:\Users\kinga\Google Drive\Novels\%s' % title + " Chapters %s to %s.pdf" %(x,x2))
print("Done!")
print(r'Saved as: C:\Users\kinga\Google Drive\Novels\%s' % title + " Chapters %s to %s.pdf" %(x,x2))
print ("use this link to convert to epub: https://www.zamzar.com/convert/txt-to-epub/")
# - Things to do:
#     Add bookmarks


# coding=utf-8

# from ebooklib import epub
#
# if __name__ == '__main__':
#     book = epub.EpubBook()
#
#     # add metadata
#     book.set_identifier('sample123456')
#     book.set_title('Sample book')
#     book.set_language('en')
#
#     book.add_author('Aleksandar Erkalovic')
#
#     # intro chapter
#     c1 = epub.EpubHtml(title='Introduction', file_name='intro.xhtml', lang='en')
#     c1.content = u'<html><head></head><body><h1>Introduction</h1><p>Introduction paragraph where i explain what is happening.</p></body></html>'
#
#     # about chapter
#     c2 = epub.EpubHtml(title='About this book', file_name='about.xhtml')
#     c2.content = '<h1>About this book</h1><p>Helou, this is my book! There are many books, but this one is mine.</p>'
#
#     # add chapters to the book
#     book.add_item(c1)
#     book.add_item(c2)
#
#     # create table of contents
#     # - add section
#     # - add auto created links to chapters
#
#     book.toc = (epub.Link('intro.xhtml', 'Introduction', 'intro'),
#                 (epub.Section('Languages'),
#                  (c1, c2))
#                 )
#
#     # add navigation files
#     book.add_item(epub.EpubNcx())
#     book.add_item(epub.EpubNav())
#
#     # define css style
#     style = '''
# @namespace epub "http://www.idpf.org/2007/ops";
# body {
#     font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
# }
# h2 {
#      text-align: left;
#      text-transform: uppercase;
#      font-weight: 200;
# }
# ol {
#         list-style-type: none;
# }
# ol > li:first-child {
#         margin-top: 0.3em;
# }
# nav[epub|type~='toc'] > ol > li > ol  {
#     list-style-type:square;
# }
# nav[epub|type~='toc'] > ol > li > ol > li {
#         margin-top: 0.3em;
# }
# '''
#
#     # add css file
#     nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
#     book.add_item(nav_css)
#
#     # create spine
#     book.spine = ['nav', c1, c2]
#
#     # create epub file
#     epub.write_epub('test.epub', book, {})