from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=200):
    """Summarize input text safely."""
    if not text or len(text.strip()) == 0:
        return "Error: Input text is empty. Please provide valid text for summarization."

    # Truncate input if it exceeds model limit (1024 tokens)
    if len(text.split()) > 800:  # Approximate token limit
        text = " ".join(text.split()[:800])

    try:
        summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        return f"Summarization failed: {str(e)}"
