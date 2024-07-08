from django.shortcuts import render, redirect
import random

words = ['python', 'django', 'programming', 'hangman', 'development']

def select_random_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman(request):
    if 'word' not in request.session:
        request.session['word'] = select_random_word()
        request.session['guessed_letters'] = []
        request.session['incorrect_guesses'] = []

    word = request.session['word']
    guessed_letters = set(request.session['guessed_letters'])
    incorrect_guesses = set(request.session['incorrect_guesses'])
    max_incorrect_guesses = 6

    if request.method == 'POST':
        guess = request.POST.get('guess').lower()
        if guess in guessed_letters or guess in incorrect_guesses:
            pass
        elif guess in word:
            guessed_letters.add(guess)
        else:
            incorrect_guesses.add(guess)

        request.session['guessed_letters'] = list(guessed_letters)
        request.session['incorrect_guesses'] = list(incorrect_guesses)

    game_over = len(incorrect_guesses) >= max_incorrect_guesses or set(word) == guessed_letters
    game_result = ""
    if game_over:
        if set(word) == guessed_letters:
            game_result = "Congratulations! You guessed the word!"
        else:
            game_result = f"Sorry, you've been hanged. The word was: {word}"

    context = {
        'word_display': display_word(word, guessed_letters),
        'incorrect_guesses': ' '.join(incorrect_guesses),
        'guesses_left': max_incorrect_guesses - len(incorrect_guesses),
        'game_over': game_over,
        'game_result': game_result
    }
    return render(request, 'game/hangman.html', context)
def reset_game(request):
    # Clear the session data to reset the game
    request.session.flush()
    return redirect('hangman')