from fpdf import FPDF

# ✅ Function to organize the summaries into a report
def organize_report(query, summaries):
    report = f"# Research Summary: {query}\n\n"
    for item in summaries:
        report += f"## Source: {item['url']}\n\n"
        report += f"{item['summary']}\n\n"
    return report

# ✅ Function to save the report as PDF
def save_summary_as_pdf(summary_text, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "AI Research Assistant Summary", ln=True)
    pdf.ln(5)

    # Add content
    pdf.set_font("Arial", size=12)
    for line in summary_text.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)