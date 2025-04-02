import streamlit as st
import os
from agents.web_search_agent import search_web
from agents.scraper_agent import scrape_url
from agents.summarizer_agent import summarize_text
from agents.organizer_agent import organize_report

st.set_page_config(page_title="AI Research Assistant", layout="centered")
st.title("🧠 Autonomous AI Research Assistant")

query = st.text_input("Enter a research topic:")

if st.button("Generate Report") and query:
    st.write("🔍 Searching...")
    urls = search_web(query)

    if not urls:
        st.error("❌ No URLs found. Try a more specific query.")
    else:
        st.write("🔗 URLs found:")
        for u in urls:
            st.markdown(f"- [{u}]({u})")

        summaries = []

        for url in urls:
            text = scrape_url(url)
            st.write(f"🧽 Scraped {len(text)} characters from {url}")

            if not text:
                st.warning(f"⚠️ No content scraped from {url}. Skipping.")
                continue

            summary = summarize_text(text)
            if summary:
                summaries.append({"url": url, "summary": summary})
            else:
                st.warning(f"⚠️ No summary returned for {url}")

        if summaries:
            report = organize_report(query, summaries)
            st.success("✅ Report generated!")

            # Download markdown report
            st.download_button("📄 Download Markdown Report", report, file_name="report.md")

            # Show inline preview
            st.markdown("### 📝 Report Preview")
            st.markdown(report)
        else:
            st.error("❌ No summaries could be generated.")
