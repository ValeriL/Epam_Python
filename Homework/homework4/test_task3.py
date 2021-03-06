from homework4.task3 import my_precious_logger


def test_stderr(capsys):
    text = "error: file nor found"
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.err == text
    assert not captured.out


def test_stdout(capsys):
    text = "OK"
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.out == text
    assert not captured.err


def test_empty_string(capsys):
    my_precious_logger("")
    captured = capsys.readouterr()
    assert not captured.out
    assert not captured.err
