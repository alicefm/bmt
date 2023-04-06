import xml.dom.minidom

# Parses the xml file
xml_doc = xml.dom.minidom.parse("cf79.xml")

# Get all elements with the AUTHOR tag
authors = xml_doc.getElementsByTagName("AUTHOR")

# Writes the extracted authors to a new XML file with indentation and XML tags
with open("autores.xml", "w") as f:

    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<!DOCTYPE FILE SYSTEM "cfc-2.dtd">\n')
    f.write("<FILE>\n")
    f.write("  <AUTHORS>\n")
    for author in authors:
        author_content = author.firstChild.nodeValue.strip()
        f.write("    <AUTHOR>" + author_content + "</AUTHOR>\n")
    f.write("</AUTHORS>\n")
    f.write("</FILE>")