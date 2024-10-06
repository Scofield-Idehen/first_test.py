#!/usr/bin/env python3

import random
import os
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

# Define multiple story templates
story_templates = [
    """
    Once upon a time, in a {adjective} {noun}, there lived a {adjective} {noun}.
    Every day, they would {verb} to the {noun} and {verb} with their {adjective} {noun}.
    One day, something {adjective} happened! They found a {adjective} {noun} that could {verb}!
    From that day on, their life became even more {adjective} and full of {noun}.
    """,
    """
    In a {adjective} galaxy far, far away, a {adjective} {noun} embarked on a {adjective} quest.
    Armed with a {adjective} {noun}, they set out to {verb} the evil {noun} and save the {noun}.
    Along the way, they encountered a {adjective} {noun} who taught them to {verb} with great skill.
    In the end, they emerged {adjective} and ready to face any {noun} that came their way.
    """,
    """
    On a {adjective} summer day, a {noun} decided to {verb} a {adjective} picnic.
    They packed a basket full of {adjective} {noun} and headed to the {noun}.
    While {verb}-ing, they stumbled upon a {adjective} {noun} that could {verb}!
    The day turned out to be more {adjective} than they could have ever imagined.
    """
]


def print_colored(text, color=Fore.WHITE, style=Style.NORMAL):
    """Print text in color."""
    print(f"{style}{color}{text}{Style.RESET_ALL}")


def choose_random_template():
    """Choose a random story template."""
    return random.choice(story_templates)


def extract_word_types(template):
    """Extract required word types from the template."""
    return [word.split('}')[0] for word in template.split('{')[1:]]


def get_word(word_type):
    """Prompt the user for a word of a specific type."""
    while True:
        word = input(f"Enter a(n) {word_type}: ").strip()
        if word:
            return word
        print_colored("Oops! You didn't enter anything. Please try again.", Fore.RED)


def collect_words(word_types):
    """Collect all required words from the user."""
    return [get_word(word_type) for word_type in word_types]


def fill_story(template, words):
    """Fill in the story template with the provided words."""
    for word_type, word in zip(extract_word_types(template), words):
        template = template.replace("{" + word_type + "}", word, 1)
    return template


def save_story(story):
    """Save the completed story to a file."""
    if not os.path.exists("mad_libs_stories"):
        os.makedirs("mad_libs_stories")

    filename = f"mad_libs_stories/story_{len(os.listdir('mad_libs_stories')) + 1}.txt"
    with open(filename, "w") as file:
        file.write(story)

    print_colored(f"Your story has been saved as {filename}", Fore.GREEN)


def play_again():
    """Ask the user if they want to play again."""
    return input("Would you like to play again? (yes/no): ").lower().startswith('y')


def play_mad_libs():
    """Play one round of Mad Libs."""
    print_colored("Welcome to Mad Libs!", Fore.CYAN, Style.BRIGHT)
    print_colored("I'll ask you for some words to fill in the blanks of our story.", Fore.YELLOW)

    template = choose_random_template()
    word_types = extract_word_types(template)
    words = collect_words(word_types)
    completed_story = fill_story(template, words)

    print_colored("\nHere's your Mad Libs story:\n", Fore.GREEN, Style.BRIGHT)
    print_colored(completed_story, Fore.WHITE, Style.BRIGHT)

    if input("Would you like to save this story? (yes/no): ").lower().startswith('y'):
        save_story(completed_story)


def mad_libs_game():
    """Main game loop."""
    while True:
        play_mad_libs()
        if not play_again():
            print_colored("Thanks for playing Mad Libs!", Fore.CYAN, Style.BRIGHT)
            break


if __name__ == "__main__":
    mad_libs_game()
