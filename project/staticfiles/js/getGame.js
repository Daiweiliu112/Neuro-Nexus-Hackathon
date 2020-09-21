/* Drawing rectangles with mouse clicks
 * https://stackoverflow.com/questions/17408010/drawing-a-rectangle-using-click-mouse-move-and-click
 * Accessed August 15, 2020 */

function initDraw(canvas, ws) {
    var socket = ws
    socket.onopen = function (e) {
        console.log("[open] Connection established");
    };
    socket.onclose = function (e) {
        console.log("[close] Connection closed");
    };

    var clicked = []

    function deleteRects() {
        document.querySelectorAll('.rectangle').forEach(rect => {
            rect.remove()
        });
        clicked = []
    }

    function sendClick() {
        var id = this.id
        if (clicked.indexOf(id) < 0) {
            send(socket, {content: id, origin: client})
            clicked.push(id)
        }
    }

    function makeRects(data) {
        var element = null;
        for (let i = 0; i < data.length; i++) {
            element = document.createElement('div');
            element.className = 'rectangle'
    
            /* Adjust pixel values for different screen sizes */
            element.style.top = data[i]['top'] * screen.height + 'px'
            element.style.left = data[i]['left'] * screen.width + 'px'
            element.style.width = data[i]['width'] * screen.width + 'px'
            element.style.height = data[i]['height'] * screen.height + 'px'
            element.id = data[i]['id']
    
            canvas.appendChild(element)

        }
        
        document.querySelectorAll('.rectangle').forEach(rect => {
            rect.onclick = sendClick
        })
    }

    socket.onmessage = function (event) {
        var data = JSON.parse(event.data)['message']
        console.log(data);
        if (data.origin === clinician) {
            data = data.content
            if (data === 'delete') {
                deleteRects()
            } else if (typeof data === 'object' && data.length > 0) {
                makeRects(data)
            }
        }
    }
}