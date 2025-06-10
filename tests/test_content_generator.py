from importlib import reload
import sys


def test_generate_text_without_openai(monkeypatch):
    monkeypatch.setitem(sys.modules, 'openai', None)
    import campaign_ai.content_generator as cg
    reload(cg)
    text = cg.generate_text('Hello')
    assert text.startswith('[Mocked response')
