# import calculator as bc
#
#
# m_arg1, m_arg2, m_action = bc.input_data()
# try:
#     m_arg1, m_arg2, m_action = bc.check_data(m_arg1, m_arg2, m_action)
# except bc.CalcExeption as e:
#     print(e)
#     exit(1)
# bc.output_data(m_arg1, m_arg2, m_action)
from calculator import input_data

a, b, c = input_data()
