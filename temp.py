import win32com.client
 
doc = win32com.client.Dispatch("Aspose.Words.Document")
 
builder = win32com.client.Dispatch("Aspose.Words.DocumentBuilder")
 
builder.Document = doc
 
builder.Write("Hello world!")
 
doc.Save("C:\\Temp\\out.doc")
