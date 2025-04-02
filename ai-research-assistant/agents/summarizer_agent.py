from transformers import pipeline

# Load model once at the top
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    try:
        # Limit input to 1024 tokens max
        text = text[:1024]
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print("❌ Summarization error:", e)
        return ""
