import xml.sax

# Defines a content handler for the SAX parser
class TitleHandler(xml.sax.ContentHandler):
    # Initializes handler instance variables
    def __init__(self):
        self.in_title = False # Flag that indicates whether we are inside a title element
        self.current_title = "" # String that stores the contents of each title
        self.titles = [] # List that stores extracted titles

    # Called by parser when new element is found
    def startElement(self, name, attrs):
        # If element name is TITLE                                                                                                               
        if name == "TITLE": 
            self.in_title = True # Sets flag to true

    # Called by parser when inside an element
    def characters(self, content):        
        # If element name is TITLE
        if self.in_title:
            self.current_title += content # Appends title content to string
    
    #Called by parser at the end of each element
    def endElement(self, name):
        # If element name is TITLE
        if name == "TITLE":
            # Replaces consecutive spaces within a title with a single space
            self.current_title = " ".join(self.current_title.split())
            # Removes leading and trailing whitespaces from a title
            title_text = self.current_title.strip()
            # Appends title to list of titles
            self.titles.append(title_text)
            # Resets content string to empty string
            self.current_title = ""
            # Resets flag to indicate we are no longer inside a title
            self.in_title = False

# Creates an instance of the handler and parses the XML file
handler = TitleHandler()
xml.sax.parse("cf79.xml", handler)

# Writes the extracted titles to a new XML file with indentation and SML tags
with open("titulos.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<!DOCTYPE FILE SYSTEM "cfc-2.dtd">\n')
    f.write("<FILE>\n")
    f.write("  <TITLES>\n")
    for title in handler.titles:
        f.write ("    <TITLE>" + title + "</TITLE>\n")
    f.write("</TITLES>\n")
    f.write("</FILE>")