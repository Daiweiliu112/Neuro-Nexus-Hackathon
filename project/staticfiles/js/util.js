function get_socket(host, roomName) {
  return new WebSocket(
    'ws://'
    + host
    + '/ws/socket/'
    + roomName
    + '/'
  );
}

function send(socket, msg) {
  socket.send(JSON.stringify({message: msg}))
}

client = "client"
clinician = "clinician"