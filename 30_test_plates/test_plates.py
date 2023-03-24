import plates

def main():
    test_is_valid()



def test_is_valid():
    assert plates.is_valid("sa") == True
    assert plates.is_valid("sa8") == True
    assert plates.is_valid("sa80") == True
    assert plates.is_valid("sa804") == True
    assert plates.is_valid("sal80") == True
    assert plates.is_valid("salo8") == True
    assert plates.is_valid("salome") == True
    assert plates.is_valid("salom6") == True



if __name__ == "__main__":
    main()