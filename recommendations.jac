walker wellbeing_recommendation {
    start {
        for mood in here --> Mood {
            if (mood.intensity > 7 or mood.label == "sad") {
                rec = Recommendation(
                    message="Take a short walk, breathe deeply, or write your thoughts."
                );
                here ++> rec : RECEIVES;
                report rec.message;
            }
        }
    }
}
