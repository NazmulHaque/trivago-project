from nose.tools import nottest

@nottest
def append_test_log(test_case, message, mode='a+'):
    file_name = 'test_logs/{}.txt'.format(test_case)

    f = open(file_name, mode)

    text = message + '\n'
    f.write(text)

    f.close()
