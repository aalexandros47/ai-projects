def organize_report(topic, summaries):
    report = f"# Research Summary: {topic}\n\n"
    for i, item in enumerate(summaries, 1):
        report += f"## Source {i}: {item['url']}\n{item['summary']}\n\n"
    return report
