# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.contrib.files import exists, append, upload_template

from fab_settings import *

env.ami = 'ami-8f03ede6'
env.directory = '/home/%s/projects/titanic' % SSH_USER
env.manage_dir = env.directory + '/src'
env.deploy_user = env.user = SSH_USER
env.activate = 'source %s/ENV/bin/activate' % env.directory
env.www_ssh_key = 'ssh-dss AAAAB3NzaC1kc3MAAACAbN+8KDO1jkRluNqiqO2KjkaSn4Qs66zBcV+JaUFrnoVt5tBaEMGW56ihtd1zmPqSufpDKTMXKneZWLAx8evFobvU5S32OKtFpR6oylZwIWg0SQNtjBE7lFHC5VnN4BtjpLp6DBzUOt6mTXYyCjaYhorMWmyw5641KXOsW0V7et0AAAAVALlYgGve+sIVrw7MTQFD4Hvb1utVAAAAgAGktSDpYw1sEC9tA593z3Ymk9r4J939DsKiL3d+RK/RXfY9KgoFtMHmCzL8goYpyWdaE2XQzCrIfp3EFW41NUWUfxsaDzXSEg4Q/CYAfJm7nNDpwv1eAq3c0Mw7RMGEw3pxsAnQrq0snHI7cVhdZ12Z6wO147+ybAbOXW7XF04sAAAAgGzFeuezmdfyS0N4VE42/kgC4SusMTxYOj5nrb8VRvzQ08Msa5FChXIWv0Fj5hMpOVX/gc4uEkbt7knpjqouo+K+8jadQ4I+sRidqG13U6b2UGJy844THSqL3HIhuPmhvWPOFjJbsNFxcoakSqLxn3ewkDzco7CH/aYo9u9VrLwk dsa-key-20080514'

if not env.hosts:
    env.hosts = ['ec2-107-21-102-210.compute-1.amazonaws.com']


def virtualenv(command):
    with cd(env.directory):
        run(env.activate + ' && ' + command)


def init():
    env.deploy_user = env.user = 'ubuntu'

    sudo('apt-get update')
    sudo('apt-get install -y mc lighttpd mysql-client git-core python-setuptools python-dev runit rrdtool memcached libjpeg62-dev')
    sudo('apt-get build-dep -y python-mysqldb')

    if not exists('/home/%s' % SSH_USER):
        sudo('yes | adduser --disabled-password %s' % SSH_USER)
        sudo('mkdir /home/%s/.ssh' % SSH_USER)
        sudo('echo "%s" >> /home/%s/.ssh/authorized_keys' % (env.www_ssh_key, SSH_USER))

    append('/etc/sudoers', '%s  ALL=(ALL) NOPASSWD:/usr/bin/sv' % SSH_USER, use_sudo=True)

    if not exists('/var/log/projects/titanic'):
        sudo('mkdir -p /var/log/projects/titanic')
        sudo('chmod 777 /var/log/projects/titanic')

    if not exists('/etc/lighttpd/conf-available/10-modules.conf'):
        put('tools/lighttpd/10-modules.conf', '/etc/lighttpd/conf-available/10-modules.conf', use_sudo=True)
        sudo('ln -s /etc/lighttpd/conf-available/10-modules.conf /etc/lighttpd/conf-enabled/10-modules.conf', shell=False)

    if not exists('/etc/lighttpd/conf-available/90-titanic.conf'):
        sudo('touch /etc/lighttpd/conf-available/90-titanic.conf')
        sudo('chown %s /etc/lighttpd/conf-available/90-titanic.conf' % SSH_USER)
    if not exists('/etc/lighttpd/conf-enabled/90-titanic.conf'):
        sudo('ln -s /etc/lighttpd/conf-available/90-titanic.conf /etc/lighttpd/conf-enabled/90-titanic.conf', shell=False)

    if not exists('/etc/sv/titanic'):
        sudo('mkdir -p /etc/sv/titanic/supervise')
        sudo('touch /etc/sv/titanic/run')
        sudo('chown %s /etc/sv/titanic/run' % SSH_USER)
        sudo('chmod 755 /etc/sv/titanic/run')
        sudo('ln -s /etc/sv/titanic /etc/service/titanic', shell=False)

    sudo('mkdir -p /home/%s/projects/titanic' % SSH_USER)
    sudo('chown -R %(user)s:%(user)s /home/%(user)s' % {'user': SSH_USER})


def production():
    upload()
    environment()
    local_settings()
    lighttpd()
    runit()
    migrate()
    restart()


def upload():
    local('git archive -o archive.tar.gz HEAD')
    put('archive.tar.gz', env.directory + '/archive.tar.gz')
    with cd(env.directory):
        run('tar -zxf archive.tar.gz')
        run('rm archive.tar.gz')
    local('del archive.tar.gz')


def environment():
    with cd(env.directory):
        with settings(warn_only=True):
            run('python virtualenv.py ENV')
        virtualenv('pip install -r requirements.txt')


def local_settings():
    with cd(env.manage_dir):
        upload_template(
            'src/local_settings.py.sample',
            'local_settings.py',
            globals(),
            backup=False
        )


def lighttpd():
    run('cp %(directory)s/tools/lighttpd/90-titanic.conf /etc/lighttpd/conf-available/90-titanic.conf' % env, shell=False)
#    sudo('/etc/init.d/lighttpd reload', shell=False)


def runit():
    run('cp %(directory)s/tools/runit/run /etc/sv/titanic/run' % env, shell=False)


def manage_py(command):
    virtualenv('cd %s && python manage.py %s' % (env.manage_dir, command))


def migrate():
    manage_py('migrate')


def restart():
    run('sudo sv restart titanic')


def local_env():
    with settings(warn_only=True):
        local('c:\\python\\python virtualenv.py ENV --system-site-packages')
    local('ENV\\Scripts\\pip install -r requirements.txt ')


def update_local_db():
    run("mysqldump -u %(DATABASE_USER)s -p%(DATABASE_PASSWORD)s -h %(DATABASE_HOST)s %(DATABASE_DB)s > dump.sql" % globals())
    get("dump.sql", "dump.sql")
    run("rm dump.sql")
    local("mysql -uroot %(DATABASE_DB)s < dump.sql" % globals())
    local("del dump.sql")