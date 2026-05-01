from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile

def create_version_page(version):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    
    c = canvas.Canvas(temp_file.name, pagesize=letter)
    
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(300, 500, f"Version {version}")
    
    c.setFont("Helvetica", 14)
    c.drawCentredString(300, 460, "Release Section")
    
    c.save()
    
    return temp_file.name