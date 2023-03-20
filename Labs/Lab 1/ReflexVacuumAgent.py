A = 'A'
B = 'B'

Enviroment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}


def RELEX_VACUUM_AGENT(loc_st):
    if loc_st[1] == 'Dirty':
        return 'Suck'
    if loc_st[0] == A:
        return 'Right'
    if loc_st[0] == B:
        return 'Left'


def Sensors():
    location = Enviroment['Current']
    return (location, Enviroment[location])


def Actuators(action):
    location = Enviroment['Current']
    if action == 'Suck':
        Enviroment[location] = 'Clean'
    elif action == 'Right' and location == A:
        Enviroment['Current'] = B
    elif action == 'Left' and location == B:
        Enviroment['Current'] = A


def run(n):
    print('         Current                        New')
    print('location    status  action  location    status')
    for i in range(1, n):
        (location, status) = Sensors()
        print("{:12s}{:8s}".format(location, status), end='')
        action = RELEX_VACUUM_AGENT(Sensors())
        Actuators(action)
        (location, status) = Sensors()
        print("{:8s}{:12s}{:8s}".format(action, location, status))


run(10)