class CalcExeption(Exception):
    pass


def input_data():
    arg1 = input("Enter the first number>> ")
    arg2 = input("Enter the second number>> ")
    action = input("Enter the action>> ")
    return arg1, arg2, action


def check_data(arg1, arg2, action):
    try:
        if "." in arg1:
            arg1 = float(arg1)
        else:
            arg1 = int(arg1)
    except ValueError:
        raise CalcExeption("Error arg1")
    try:
        if "." in arg2:
            arg2 = float(arg2)
        else:
            arg2 = int(arg2)
    except ValueError:
        raise CalcExeption("Error arg2")
    return arg1, arg2, action


def output_data(arg1, arg2, action):
    try:
        if action == "+":
            print(arg1+arg2)

        elif action == "-":
            print(arg1-arg2)

        elif action == "*":
            print(arg1*arg2)

        elif action == "/":
            print(arg1/arg2)
    except ValueError:
        raise CalcExeption("Error action")


if __name__ == '__main__':
    m_arg1, m_arg2, m_action = input_data()
    try:
        m_arg1, m_arg2, m_action = check_data(m_arg1, m_arg2, m_action)
    except CalcExeption as e:
        print(e)
        exit(1)
    output_data(m_arg1, m_arg2, m_action)
