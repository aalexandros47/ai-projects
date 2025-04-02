from transformers import pipeline

# Load once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    try:
        text = text[:1024]  # truncate to model input length
        summary = summarizer(
            text, 
            max_length=min(len(text.split()), 150), 
            min_length=30, 
            do_sample=False
        )
        return summary[0]['summary_text']
    except Exception as e:
        print("❌ Summarization error:", e)
        return ""
