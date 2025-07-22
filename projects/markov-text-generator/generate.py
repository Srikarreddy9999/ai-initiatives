import markovify

text = (
    "Artificial intelligence is the simulation of human intelligence processes "
    "by machines, especially computer systems. These processes include "
    "learning, reasoning, and self-correction. Applications of AI include "
    "expert systems, speech recognition, and machine vision. The field of AI "
    "research was founded on the claim that human intelligence can be so "
    "precisely described that a machine can be made to simulate it. "
    "This raises philosophical arguments about the nature of the mind and "
    "the ethics of creating artificial beings endowed with human-like "
    "intelligence."
)

text_model = markovify.Text(text)

for _ in range(5):
    sentence = text_model.make_sentence()
    print(sentence if sentence else "[No sentence generated]")
