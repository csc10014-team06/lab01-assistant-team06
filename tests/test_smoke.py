from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."


def test_health_center_lookup():
    assert "C.101" in reply("Where is the Health Center?")


def test_admissions_office_lookup():
    assert "A.105" in reply("When is the Admissions Office open?")


def test_partial_office_lookup_training():
    assert "I.101" in reply("training")


def test_partial_office_lookup_in_question():
    assert "I.101" in reply("Where is training?")


def test_finance_office_lookup():
    assert "I.103" in reply("Where is the Finance Office?")


def test_career_center_lookup():
    assert "C.102" in reply("When is the Career Center open?")
