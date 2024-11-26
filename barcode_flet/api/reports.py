from fastapi import APIRouter
from report import PdfReport
import os
from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi.responses import Response

router_reports = APIRouter()
my_pdf_report = PdfReport()

pdf_path = "assets/pdf/generated_report.pdf"  # Ensure this path is valid

@router_reports.get("/generate-pdf")
async def generate_pdf():
    # Create the PDF file
    my_pdf_report.generate_pdf_report(pdf_path)
    
    # Return the PDF file as a response
    if os.path.exists(pdf_path):
        return FileResponse(pdf_path, media_type="application/pdf", filename="report.pdf")
    else:
        return {"error": "Failed to generate PDF"}

@router_reports.get("/view-pdf")
async def view_pdf():
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as pdf:
            pdf_content = pdf.read()
        headers = {"Content-Disposition": "inline; filename=sample.pdf"}
        return Response(pdf_content, media_type="application/pdf", headers=headers)
    else:
        return {"error": "PDF file not found"}