#!/bin/bash
#
# Daemon Name: zopesendmail_ctl
#
# chkconfig: - 58 74
# description: zope-sendmail service script

# Source function library.

. /etc/init.d/functions

SOFTWARE_HOME="${buildout:directory}"
USER=${configuration:effective-user}

NAME="zope-sendmail"
SENDMAIL=$SOFTWARE_HOME/bin/$NAME
QUEUE=${configuration:mail-queue}

prog="$SENDMAIL --daemon $QUEUE --hostname ${configuration:smtp-server}"
lockfile=/var/lock/subsys/$NAME

start() {
    #Make some checks for requirements before continuing
    [ -x $SENDMAIL ] || exit 5

    # Start our daemon daemon
    echo -n $"Starting $NAME: "
    daemon --user=$USER --pidfile /var/run/$NAME.pid $prog >/dev/null 2>&1 &
    RETVAL=$?
    echo

    #
    #If all is well touch the lock file
    [ $RETVAL -eq 0 ] && touch $lockfile
    return $RETVAL
}

stop() {
    echo -n $"Shutting down $NAME: "
    killproc $NAME
    RETVAL=$?
    echo

    #If all is well remove the lockfile
    [ $RETVAL -eq 0 ] && rm -f $lockfile
    return $RETVAL
}

# See how we were called.
case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  status)
        status $NAME
        ;;
  restart)
        stop
        start
        ;;
   *)
        echo $"Usage: $0 {start|stop|status|restart}"
        exit 2
esac

#  daemon user=zope-www $SENDMAIL --daemon $QUEUE >/dev/null 2>&1 &

