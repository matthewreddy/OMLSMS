import os, tempfile, subprocess, codecs
from omldb import PDF_PRINTER_PATH, PDF_VIEWER_PATH, HTML_CONVERTER_PATH, LABEL_PRINTER, DEFAULT_PRINTER
#import time
#import win32print

# defined by main() after loading config file:
pdfview_filename = PDF_VIEWER_PATH
gsprint_filename = PDF_PRINTER_PATH
htmltopdf_filename = HTML_CONVERTER_PATH
labelPrinterName = LABEL_PRINTER
defaultPrinterName = DEFAULT_PRINTER
testPrinting = False # test printing, use a viewer rather than send directly to printer

'''    
def printPDF(PDF_string):
    try:
        file = tempfile.NamedTemporaryFile (suffix=".html", delete=False)
        file.write (PDF_string)
        file.close()
    except:
        raise EnvironmentError(101, "Error opening temporary file.")
    
    try:
        p = subprocess.Popen([gsviewpath, file.name], 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
    except:
        raise EnvironmentError(102, "Error printing file.")
    
    try:
        os.remove(file.name)
    except:
        raise Warning("Could not delete temporary file: %s." % file.name)

    return None
'''

def printHTML(HTML_string, useLabelPrinter=False):
    startupinfo = subprocess.STARTUPINFO()
    if not testPrinting:
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW # prevent dos box popup
        print_app = gsprint_filename, 
    else:
        print_app = pdfview_filename

    try:
        file = tempfile.NamedTemporaryFile (suffix=".html", delete=False)
        file.write (HTML_string)
        file.close()
    except:
        raise EnvironmentError(101, "Error opening temporary file.")

    try:
        pdffilename = os.path.join(os.path.dirname(file.name),
                        os.path.basename(file.name).split('.')[0] + ".pdf")
        p = subprocess.Popen([htmltopdf_filename, file.name, pdffilename],
                             startupinfo=startupinfo, 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        if testPrinting:
            print_command = [pdfview_filename, pdffilename]
        elif useLabelPrinter:
            print_command = [gsprint_filename, pdffilename, '-printer', '%s' % labelPrinterName]
        elif defaultPrinterName != "default":
            print_command = [gsprint_filename, pdffilename, '-printer', '%s' % defaultPrinterName]
        else:
            print_command = [gsprint_filename, pdffilename]
        
        #if useLabelPrinter and not testPrinting:
        #    print_jobs = True
        #    while print_jobs:
        #        phandle = win32print.OpenPrinter(labelPrinterName)
        #        print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
        #        win32print.ClosePrinter(phandle)
        #        if print_jobs:
        #            time.sleep(0.2)
        
        p = subprocess.Popen(print_command, 
                             startupinfo=startupinfo, 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
    except:
        raise EnvironmentError(102, "Error printing file.")
    finally:
        try:
            os.remove(pdffilename)
            os.remove(file.name)
        except:
            pass

    return None


def viewText(text):
    startupinfo = subprocess.STARTUPINFO()
    #startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:
            # Open a temporary file with a .txt suffix and prevent automatic deletion
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
            temp_file_path = temp_file.name  # Get the file path of the temporary file

        # Write the text to the temporary file
        with codecs.open(temp_file_path, 'w', encoding='utf-8') as file_writer:
            file_writer.write(text)
    except Exception as e:
        print(e)
        raise EnvironmentError(101, "Error opening temporary file.")

    try:
        p = subprocess.Popen(["notepad.exe", temp_file.name], 
                             startupinfo=startupinfo, 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
    except:
        raise EnvironmentError(103, "Error viewing file.")
    finally:
        try:
            os.remove(temp_file.name)
        except:
            pass


def printText(text):
    startupinfo = subprocess.STARTUPINFO()
    #startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:
            # Open a temporary file with a .txt suffix and prevent automatic deletion
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
            temp_file_path = temp_file.name  # Get the file path of the temporary file

        # Write the text to the temporary file
        with codecs.open(temp_file_path, 'w', encoding='utf-8') as file_writer:
            file_writer.write(text)
    except:
        raise EnvironmentError(101, "Error opening temporary file.")

    try:
        p = subprocess.Popen(["notepad.exe", "/P", temp_file.name], shell=True)
        p.communicate()
        # p = subprocess.Popen(["notepad.exe /P", temp_file.name], 
        #                      startupinfo=startupinfo, 
        #                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # stdout, stderr = p.communicate()
    except:
        raise EnvironmentError(102, "Error printing file.")
    finally:
        try:
            os.remove(temp_file.name)
        except:
            pass           
