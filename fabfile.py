from fabric.api import *
#from deploy import *
#from deploy import app

def backup():
    local('git pull')
    local('git add .')
    print "Enter your commit statement"
    comment = raw_input()

    local("git commit -m '%s'" % comment)

    local("git push")


def switch_debug(what_to_change,change_to):
    local('cp TheMuse/settings.py TheMuse/settings.py.bk')
    sed = "sed 's/^DEBUG = %s$/DEBUG = %s/' TheMuse/settings.py.bk > TheMuse/settings.py"
    local(sed % (what_to_change,change_to))
    local('rm TheMuse/settings.py.bk')


def server():
    host_string = '54.221.202.250'
    user = 'ubuntu'
    key_filename = '.gist_suqare/gist_square_host.pem'

def deploy():
    local('pip freeze > requirements.txt')
    local('git pull')
    local('git add .')

    print "Enter commit comment"
    comment = raw_input()
    local('git commit -m "%s"' % comment)

    local('git push')
    switch_debug('True','False')

    local('./manage.py collectstatic')

    switch_debug('False', 'True')

