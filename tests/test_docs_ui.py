from pathlib import Path

def test_ui_sources_mockup_exists_and_valid():
    doc_path = Path("docs/ui-sources.md")
    assert doc_path.exists(), "docs/ui-sources.md must exist"
    
    content = doc_path.read_text(encoding="utf-8")
    assert "Example 1" in content, "Mockup must contain Example 1"
    assert "Example 2" in content, "Mockup must contain Example 2"
    assert "Sources:" in content, "Mockup must specify citation format with 'Sources:'"