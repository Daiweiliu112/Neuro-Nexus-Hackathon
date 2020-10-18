/* Drawing rectangles with this.mouse clicks
 * https://stackoverflow.com/questions/17408010/drawing-a-rectangle-using-click-this.mouse-move-and-click
 * Accessed August 15, 2020 */

class ClientGame {
    constructor(canvas, ws) {
        this.mouse = {
            x: 0,
            y: 0,
        };

        this.socket = ws;
        this.canvas = canvas;
        this.items = [];    
        this.initializeSocket();
        this.initializeListeners();
        var game = this;
    }

    initializeSocket() {
        this.socket.onopen = function(e)  {
            console.log("[open] Connection established");
        };
        this.socket.onclose = function(e) {
            console.log("[close] Connection closed");
        };
        this.socket.onmessage = function(e) {
            var data = JSON.parse(e.data)['message']
            if (data.origin === clinician) {
                data = data.content
                if (data === 'delete') {
                    game.deleteRects()
                } else if (data === 'next') {
                    //alert("Next image will be loaded");
                    next_image();
                } else if (typeof data === 'object' && data.length > 0) {
                    game.makeRects(data)
                }
            }
        }
    }

    initializeListeners() {
        this.canvas.addEventListener('mousedown', e => {
            send(this.socket, {origin: client, x: this.mouse['x'], y: this.mouse['y']})
        });

        /* Set this.mouse location */
        canvas.onmousemove = function(e) {
            var ev = e || window.event; //Moz || IE
            if (ev.pageX) { //Moz
                game.mouse.x = ev.pageX + window.pageXOffset;
                game.mouse.y = ev.pageY + window.pageYOffset;
            } else if (ev.clientX) { //IE
                game.mouse.x = ev.clientX + document.body.scrollLeft;
                game.mouse.y = ev.clientY + document.body.scrollTop;
            }
        }
    }

    makeRects(data) {
        var element = null;
        this.items = [];
        for (let i = 0; i < data.length; i++) {
            element = document.createElement('div');
            element.className = 'target'
            element.style.position = 'absolute'
    
            /* Adjust pixel values for different screen sizes */
            element.style.top = data[i]['top'] * screen.height + 'px'
            element.style.left = data[i]['left'] * screen.width + 'px'
            element.style.width = data[i]['width'] * screen.width + 'px'
            element.style.height = data[i]['height'] * screen.height + 'px'
            element.id = data[i]['id']
            this.items.push(data[i]['id'].replace('$$$', ' '))

            canvas.appendChild(element)
            
        }

        document.getElementById('item-list').innerText = "this.items: " + this.items.join(', ');
        this.items = [];
    }

    deleteRects() {
        document.querySelectorAll('.target').forEach(rect => {
            rect.remove()
        });
        this.items = []
    }
}
