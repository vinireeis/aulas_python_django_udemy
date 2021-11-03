from metodos import minimo, maximo, media, quantidade


def test_minimo():
    assert minimo([-5, 3, 5]) == -5


def test_maximo():
    assert maximo([0, 9, 15]) == 15


def test_media():
    assert media([-1, -3, -5]) == -3


def test_quantidade():
    assert quantidade([0, 3, 9, 8]) == 4


if __name__ == '__main__':
    test_maximo()
    test_minimo()
    test_media()
    test_quantidade()
