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
    var dp = new DOMParser()
    socket.onopen = function (e) {
        console.log("[open] Connection established");
    };
    socket.onclose = function (e) {
        console.log("[close] Connection closed");
    };

    function deleteRects() {
        document.querySelectorAll('.rectangle').forEach(rect => {
            rect.remove()
        });
    }

    function makeRects(data) {
        var element = null;
        for (let i = 0; i < data.length; i++) {
            element = document.createElement('div');
            element.className = 'rectangle'
    
            element.style.top = data[i]['top']
            element.style.left = data[i]['left']
            element.style.width = data[i]['width']
            element.style.height = data[i]['height']
            element.id = data[i]['id']
    
            canvas.appendChild(element)
        }
    }

    socket.onmessage = function (event) {
        var data = JSON.parse(event.data)['message']
        if (data === 'delete') {
            deleteRects()
        } else {
            makeRects(data)
        }

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