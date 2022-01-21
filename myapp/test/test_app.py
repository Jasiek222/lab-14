import pytest
import app

def test_hello():
    got = app.hello("Aleksandra")
    want = "Hello Aleksandra"
    assert got == want


testdata = [("I think today will be a great day", True),("I do not think this will turn out well", False)]
@pytest.mark.parametrize('sample, out', testdata)
def test_extract_sentiment(sample, out):
    sentiment = app.extract_sentiment(sample)
    assert bool(sentiment) == out

testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]
@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):
    assert app.text_contain_word(word, sample) == expected_output

testdata = [
    ([2, 6, 4, 1, 3, 5], [1, 2, 3, 4, 5, 6]),
    ([4, 16, 9, 5, 1, 7], [1, 4, 5, 7, 9, 16]),
    ([6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
     ([], [])
     ]
@pytest.mark.parametrize('sample, result', testdata)
def test_bubble_sort(sample, result):
    try:
        assert app.bubble_sort(sample) == result
    except:
        assert ValueError('Lista jest pusta')