/* Drawing rectangles with mouse clicks
 * https://stackoverflow.com/questions/17408010/drawing-a-rectangle-using-click-mouse-move-and-click
 * Accessed August 15, 2020 */

function initDraw(canvas, ws) {
    var mouse = {
        x: 0,
        y: 0,
        startX: 0,
        startY: 0
    };

    var socket = ws
    socket.binaryType = "arraybuffer";
    var dp = new DOMParser()
    socket.onopen = function (e) {
        console.log("[open] Connection established");
    };
    socket.onclose = function (e) {
        console.log("[close] Connection closed");
    };
    socket.onmessage = function (event) {
        console.log(event.data)
    }

    function setMousePosition(e) {
        var ev = e || window.event; //Moz || IE
        if (ev.pageX) { //Moz
            mouse.x = ev.pageX + window.pageXOffset;
            mouse.y = ev.pageY + window.pageYOffset;
        } else if (ev.clientX) { //IE
            mouse.x = ev.clientX + document.body.scrollLeft;
            mouse.y = ev.clientY + document.body.scrollTop;
        }
    };

    canvas.onmousemove = function (e) {
        setMousePosition(e);
    }
}