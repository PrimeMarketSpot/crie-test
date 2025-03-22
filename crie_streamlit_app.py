
import streamlit as st

st.set_page_config(page_title="CRIE Test", layout="centered")

st.title("CRIE: Cognitive & Relational Intelligence Evaluation")
st.subheader("A Hybrid IQ and Emotional Insight Assessment")

st.markdown("Answer the questions below to receive your cognitive-relational archetype.")

# Questions and options
questions = {
    "1. Crown : King :: Spotlight : ?": ["Audience", "Performance", "Self", "Fame"],
    "2. Admiration : Confidence :: Obedience : ?": ["Control", "Influence", "Respect", "Loyalty"],
    "3. What comes next? 3, 6, 12, 24, ___": ["36", "42", "48", "54"],
    "4. Which one doesn’t belong?": ["Justice", "Pride", "Loyalty", "Compassion"],
    "5. A friend is upset at work. You respond:": ["I'm here—tell me everything.", "I had a similar experience...",
                                                  "People need to toughen up.", "What do you want to do?"],
    "6. Someone else is praised for your work. You feel:": ["Slightly annoyed", "Make your role known",
                                                            "Outraged", "Indifferent"],
    "7. You’re told 'You never listen.' You think:": ["That's not true", "Maybe they're right",
                                                      "They're manipulating me", "Was I unclear?"],
    "8. Which statement fits best?": ["I'm misunderstood", "People should value me more",
                                      "I adjust my message", "I avoid conflict"],
    "9. Which word best reflects your drive?": ["Legacy", "Harmony", "Recognition", "Impact"],
    "10. Choose the quote that fits you:": ["To be great is to be misunderstood.",
                                           "The best leaders eat last.",
                                           "Life’s a stage.", "Wanting to win is everything."]
}

# Trait scoring map
narcissistic_choices = {
    1: [2, 3],
    2: [0],
    4: [1, 2],
    5: [1, 2],
    6: [2],
    7: [0, 1],
    8: [0, 1],
    9: [2],
    10: [0, 2, 3]
}

# Collect answers
responses = []
for i, (q, opts) in enumerate(questions.items(), 1):
    choice = st.radio(q, opts, key=i)
    responses.append(opts.index(choice))

# Submit and evaluate
if st.button("Submit and Get Result"):
    # Score
    score = 0
    for idx, answer in enumerate(responses):
        if idx in narcissistic_choices and answer in narcissistic_choices[idx]:
            score += 1

    # Archetype logic
    if score <= 3:
        archetype = "The Diplomat"
        desc = "You are empathetic, collaborative, and attuned to others' emotions. You value harmony over ego."
    elif score <= 6:
        archetype = "The Strategist"
        desc = "You blend ambition with insight. You’re goal-driven and socially perceptive but can be image-conscious."
    elif score <= 10:
        archetype = "The Visionary"
        desc = "You’re charismatic and confident, driven by excellence. Emotional connection may require intentional effort."
    else:
        archetype = "The Mirror"
        desc = "You are magnetic and self-assured, but often require validation. Your impact is powerful, yet relationships may challenge your inner world."

    st.success(f"Your Archetype: {archetype}")
    st.markdown(desc)
    st.info("This result is for personal insight and relationship enhancement—not a clinical diagnosis.")
