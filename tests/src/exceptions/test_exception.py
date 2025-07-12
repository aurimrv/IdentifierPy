import pytest

@pytest.mark.skip(reason="Teste não pertence ao projeto")
@pytest.mark.exceptions
def test_exception01():
    with pytest.raises(IndexError):
        str = "MLP-ESBD3"[20]  # IndexError