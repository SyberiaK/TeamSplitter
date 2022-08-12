from random import shuffle

from util import clear_terminal, split_array


def frame(length: int, string: str = None):
    clear_terminal()

    name = 'Team Splitter'

    length -= len(name) + 2
    eq_count = length // 2 if length == length // 2 * 2 else length // 2 + 1

    print(f'{"=" * eq_count} {name} {"=" * eq_count}\n')
    print(string) if string else None


def main():
    error_code = ''
    br = ';'
    secret_word = 'butterfly'

    while 1:
        input_str = 'Enter the teams count: '
        max_len = max(len(input_str), len(error_code))
        frame(max_len, error_code)
        teams_count = input(input_str)
        if not teams_count or teams_count.isspace():
            error_code = 'ERROR! The input cannot be blank.'
            continue
        if not teams_count.isnumeric():
            error_code = 'ERROR! The count must be integer.'
            continue
        teams_count = int(teams_count)
        if teams_count < 2:
            error_code = 'ERROR! Must be at least two teams.'
            continue
        error_code = ''
        break

    while 1:
        desc_str = f'Enter the participants separating them with "{br}", e. g. A{br}BC{br}D E{br}F'
        max_len = max(len(desc_str), len(error_code))
        frame(max_len, error_code)
        print(desc_str + '\n')
        players = input('Enter the participants: ')
        if not players or players.isspace():
            error_code = 'ERROR! The input cannot be blank.'
            continue
        if br not in players:
            error_code = 'ERROR! Entered only one participant (maybe you forgot about separators?).'
            continue
        players = players.split(';')
        if any(not p or p.isspace() for p in players):
            error_code = "ERROR! The name of one of the participants was empty " \
                         "(maybe you entered two separators in a row?)."
            continue
        if len(players) < teams_count:
            error_code = 'ERROR! There are more teams than members.'
            continue
        error_code = ''
        break

    players_len = len(players)
    chaotic_sorting = False

    if players_len % teams_count:
        while 1:
            desc_str = f'These participants ({players_len} people) cannot be divided' \
                       f' equally into {teams_count} teams.'
            max_len = max(len(error_code), len(desc_str))
            frame(max_len, error_code)
            print(desc_str + '\n')
            decision = input('Continue? (y/n): ')
            if decision not in ['y', 'n']:
                error_code = 'ERROR! Incorrect input.'
                continue
            match decision:
                case 'y':
                    error_code = ''
                    break
                case 'n':
                    return main()
        while 1:
            desc_strs = ['With the usual uneven sorting of players among teams, the first teams on the list',
                         'will cover a larger number of participants than the last ones.',
                         'As a solution to this, a chaotic sorting of players can be used, in which',
                         'random teams will cover a larger number of players, '
                         'regardless of the order of the teams in the list.']
            max_len = max(len(x) for x in desc_strs)
            frame(max_len, error_code)
            print(desc_strs[0], desc_strs[1], '', sep='\n')
            print(desc_strs[2], desc_strs[3], '', sep='\n')
            decision = input('Use chaotic sorting? (y/n): ')
            if decision not in ['y', 'n']:
                error_code = 'ERROR! Incorrect input.'
                continue
            match decision:
                case 'y':
                    chaotic_sorting = True
                case 'n':
                    chaotic_sorting = False
            error_code = ''
            break
    shuffle(players)
    teams = split_array(players, teams_count, chaotic_sorting)

    while 1:
        desc_str = 'Here are all the teams that have been formed:'
        input_str = f'Enter "{secret_word}" to return to the program\'s beginning: '
        max_len = max(max(len(f'>> Team {index + 1}: {", ".join(team)} ({len(team)} people)')
                          for index, team in enumerate(teams)), len(error_code), len(desc_str), len(input_str))
        frame(max_len, error_code)
        print(desc_str + '\n')
        for index, team in enumerate(teams):
            print(f'>> Team {index + 1}: {", ".join(team)} ({len(team)} people)')
        print()
        decision = input(input_str)
        if decision != secret_word:
            error_code = "You entered the wrong word. (This entry is necessary to protect" \
                         " against accidental jumping to the program's beginning.)"
            continue
        return main()


if __name__ == '__main__':
    main()
