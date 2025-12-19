walker track_mood {
    has mood_label: str;
    has mood_intensity: int;
    has mood_date: str;

    start {
        mood = Mood(
            label=mood_label,
            intensity=mood_intensity,
            date=mood_date
        );
        here ++> mood : HAS_MOOD;
        report "Mood successfully recorded.";
    }
}
