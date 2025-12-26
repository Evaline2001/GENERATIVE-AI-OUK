node User {
    has name: str;
    has email: str;
}

node Mood {
    has label: str;
    has intensity: int;
    has date: str;
}

node JournalEntry {
    has text: str;
    has sentiment: str;
    has date: str;
}

node Recommendation {
    has message: str;
}

edge HAS_MOOD;
edge WROTE;
edge RECEIVES;
