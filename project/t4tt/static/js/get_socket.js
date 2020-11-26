function get_socket(host, roomName) {
  return new WebSocket(
    'ws://'
    + host
    + '/ws/socket/'
    + roomName
    + '/'
  );
}