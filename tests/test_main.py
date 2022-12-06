from src.main import main


def test_main(capfd):
    main()  # print to stdout
    out, err = capfd.readouterr()
    assert out == "True\n"
