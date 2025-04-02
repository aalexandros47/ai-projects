from fpdf import FPDF

def organize_report(query, summaries):
    report = f"# Research Summary: {query}\n\n"
    for item in summaries:
        report += f"## Source: {item['url']}\n\n"
        report += f"{item['summary']}\n\n"
    return report


