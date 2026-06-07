from logic_utils import check_guess

# FIX: AI helped refactor tests to unpack (outcome, message) tuple from check_guess
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# FIX: AI verified hint messages are no longer reversed
def test_hint_messages_are_correct():
    # Secret is 50
    outcome_high, message_high = check_guess(60, 50)
    assert message_high == "📉 Go LOWER!"

    outcome_low, message_low = check_guess(40, 50)
    assert message_low == "📈 Go HIGHER!"