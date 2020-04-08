set DEPLOYMENT_PATH [lindex $argv 0]
set GIT_LINK [lindex $argv 1]
set GIT_BRANCH [lindex $argv 2]
set GIT_PASSWORD [lindex $argv 3]

cd $DEPLOYMENT_PATH

spawn git pull "$GIT_LINK" $GIT_BRANCH
expect "Password for"
send "$GIT_PASSWORD\n"
interact