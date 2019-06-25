@dir = "/app/"

worker_processes 2
working_directory @dir

timeout 30

listen "unix://#{ENV['SOCKET']}"
#listen "/run/app.sock", :backlog => 64

# Set process id path
pid "/run/unicorn.pid"
