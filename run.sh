set -a
. deploys/dev.env
set +a

case $1 in
  start)
    ./run.sh stop
    docker-compose build bot
    docker-compose up -d
  ;;
  stop)
    docker-compose down -v --remove-orphans
  ;;
  *)
    echo "Use 'start' command"
esac