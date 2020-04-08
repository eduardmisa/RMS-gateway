source 0-configuration.sh

expect 01-git-pull-repository.sh
sh $DEPLOYMENT_PATH/02-rebuild-container.sh
