walker journal_reflection {
    has entry_text: str;

    start {
        sentiment = "neutral";

        if ("sad" in entry_text or "tired" in entry_text) {
            sentiment = "negative";
        }
        if ("happy" in entry_text or "grateful" in entry_text) {
            sentiment = "positive";
        }

        entry = JournalEntry(
            text=entry_text,
            sentiment=sentiment,
            date="today"
        );

        here ++> entry : WROTE;
        report sentiment;
    }
}
