from app.main import main


def test_main(capfd):
    main()  # print to stdout
    (out, err) = capfd.readouterr()
    if err != "":
        print(err)
    # assert out == "Log level is INFO\nTrue\n"
    assert out == "True\n"
