import random as rnd

import util


NAME = 'Team Splitter'
BR = ';'
KEYWORD = 'sausage'


def header(name: str, header_len: int, hint: str = None):
    util.clear_terminal()
    if hint is not None:
        header_len = max(header_len, len(hint))

    print(f'{" " + name + " ":=^{header_len}}\n')
    if hint is not None:
        print(hint)


def main():
    error_code = ''

    while True:
        input_str = 'Enter the teams count: '
        header(NAME, len(input_str), error_code)
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

    while True:
        desc_str = 'Enter the participants separating them with "{0}", e. g. A{0}BC{0}D E{0}F'.format(BR)
        header(NAME, len(desc_str), error_code)
        print(desc_str + '\n')
        players = input('Enter the participants: ')
        if not players or players.isspace():
            error_code = 'ERROR! The input cannot be blank.'
            continue
        if BR not in players:
            error_code = 'ERROR! Entered only one participant (maybe you forgot about separators?).'
            continue
        players = players.split(BR)
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
        while True:
            desc_str = f'These participants ({players_len} people) cannot be divided' \
                       f' equally into {teams_count} teams.'
            header(NAME, len(desc_str), error_code)
            print(desc_str + '\n')
            decision = input('Continue? (y/n): ')
            if decision not in ('y', 'n'):
                error_code = 'ERROR! Incorrect input.'
                continue
            if decision == 'y':
                error_code = ''
                break
            else:
                return main()

        while True:
            desc_strs = ['With the usual uneven sorting of players among teams, the first teams on the list',
                         'will cover a larger number of participants than the last ones.',
                         '',
                         'As a solution to this, a chaotic sorting of players can be used, in which',
                         'random teams will cover a larger number of players, '
                         'regardless of the order of the teams in the list.',
                         '']
            max_len = max(len(x) for x in desc_strs)
            header(NAME, max_len, error_code)
            print(*desc_strs, sep='\n')
            decision = input('Use chaotic sorting? (y/n): ')
            if decision not in ('y', 'n'):
                error_code = 'ERROR! Incorrect input.'
                continue
            chaotic_sorting = (decision == 'y')
            error_code = ''
            break
    rnd.shuffle(players)
    teams = util.split_array(players, teams_count, chaotic_sorting)

    while True:
        desc_str = 'Here are all the teams that have been formed:'
        input_str = f'Enter "{KEYWORD}" to return to the program\'s beginning: '
        max_len = max(max(len(f'>> Team {index + 1}: {", ".join(team)} ({len(team)} people)')
                          for index, team in enumerate(teams)), len(desc_str), len(input_str))
        header(NAME, max_len, error_code)
        print(desc_str + '\n')
        for index, team in enumerate(teams):
            print(f'>> Team {index + 1}: {", ".join(team)} ({len(team)} people)')
        print()
        decision = input(input_str)
        if decision != KEYWORD:
            error_code = "You entered the wrong word. (This entry is necessary to protect" \
                         " against accidental jumping to the program's beginning.)"
            continue
        return main()


if __name__ == '__main__':
    main()
