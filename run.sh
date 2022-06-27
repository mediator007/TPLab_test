case $1 in
  start)
    ./run.sh stop
    docker-compose up --build
  ;;
  stop)
    docker-compose down -v --remove-orphans
  ;;
  *)
    echo "Use 'start' command"
esac