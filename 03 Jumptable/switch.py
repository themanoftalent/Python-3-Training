def main():
    print('this is the switch file')

    choices = dict(
        one='first',
        two='second',
        three='third',
        four='fourth',
        five='fifth',
        six = 'sixth'
    )

    van = 'one'
    print(choices[van])
    any_key = choices.get('ten', 'other')
    print(any_key)


if __name__ == "__main__": main()
