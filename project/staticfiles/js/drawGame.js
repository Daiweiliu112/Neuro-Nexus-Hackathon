
/* Drawing rectangles with this.mouse clicks
* https://stackoverflow.com/questions/17408010/drawing-a-rectangle-using-click-this.mouse-move-and-click
* Accessed August 15, 2020 */

class ClinicianGame {
    constructor(canvas, ws, numImages) {
        this.mouse = {
            x: 0,
            y: 0,
            startX: 0,
            startY: 0
        };
        this.data = Array.apply(null, Array(numImages)).map(function () {
            return {
                totalClicks: 0,
                timeElapsed: 0,
                incorrectClicks: [],
                correctClicks: [],
                correct: false,
            }
        })
        this.drawSwitch = false;
        this.socket = ws;
        this.canvas = canvas;
        this.element = null;
        this.trial = 0;
        this.initializeSocket();
        this.initializeListeners();
        this.trialStartTime = this.getTime()

        var game = this;
    }

    /* Initializes the different socket functions */
    initializeSocket() {
        this.socket.onopen = function(e) {
            console.log("[open] Connection established");
        };
    
        this.socket.onclose = function(e) {
            console.log("[close] Connection closed");
        };
    
        this.socket.onmessage = function(e) {
            var data = JSON.parse(e.data)['message']
            if (data.origin === client) {
                game.makeCirc(data.x, data.y)
            }
        }
    }

    /* Initializes the different DOM listeners */
    initializeListeners() {
        document.querySelector('img').draggable = false;

        /* Updates endpoint of this.element, if necessary */
        this.canvasmousemove = function(e) {
            game.setmousePosition(e);
            if (game.element !== null) {
                game.element.style.width = Math.abs(game.mouse.x - game.mouse.startX) + 'px';
                game.element.style.height = Math.abs(game.mouse.y - game.mouse.startY) + 'px';
                game.element.style.left = (game.mouse.x - game.mouse.startX < 0) ? game.mouse.x + 'px' : game.mouse.startX + 'px';
                game.element.style.top = (game.mouse.y - game.mouse.startY < 0) ? game.mouse.y + 'px' : game.mouse.startY + 'px';
            }
        }

        /* Perform different operations for each of the footer's buttons when clicked */
        document.getElementById('draw-switch').addEventListener('click', function(e) {
            if (!game.element)
                game.drawSwitch = !game.drawSwitch;
        })

        /* Iterates over all new rectangles, collects them, and sends them to the user */
        document.getElementById('send-button').addEventListener('click', () => {
            var rects = document.querySelectorAll('.rectangle')
            var id = null;
            var el = null;
            var objs = [];
            var ids = [];

            if (rects.length === 0) {
                alert('Please create at least one element');
                return
            }

            for (let i = 0; i < rects.length; i++) {
                el = rects[i]
                id = el.children[0].children[0] // Get input of the current rectangle

                /* Ensures all rectangles have a name */
                if (id.value === '') {
                    alert('Please enter a value for all rectangles.');
                    return
                } else if (ids.indexOf(id.value) >= 0) {
                    /* Ensures all rectangles are uniquely labelled */
                    alert("Your rectangles must have unique lables");
                    return
                }

                el.id = id.value.replace(' ', '$$$');
                /* Convert to percentage, convert back after sending */
                objs.push({
                    width: Number(el.style.width.slice(0, -2)) / screen.width,
                    height: Number(el.style.height.slice(0, -2)) / screen.height,
                    top: Number(el.style.top.slice(0, -2)) / screen.height,
                    left: Number(el.style.left.slice(0, -2)) / screen.width,
                    id: el.id
                })
                ids.push(id.value)
            }
            send(this.socket, {content: objs, origin: clinician})
        });

        /* Sends next image to the user */
        document.getElementById('next-button-success').addEventListener('click', () => {
            send(this.socket, {content: 'next', origin: clinician});
        })
        document.getElementById('next-button-failure').addEventListener('click', () => {
            send(this.socket, {content: 'next', origin: clinician});
        })

        /* Deletes all rectangles from the user's screen */
        document.getElementById('delete-button').addEventListener('click', () => {
            document.querySelectorAll('.rectangle').forEach(rect => {
                rect.remove()
            });
            send(this.socket, {content:'delete', origin: clinician})
        })

        /* Start drawing this.element */
        this.canvas.addEventListener('mousedown', e => {
            if (this.drawSwitch) {
                this.mouse.startX = this.mouse.x;
                this.mouse.startY = this.mouse.y;
                this.element = document.createElement('div');
                this.element.className = 'rectangle'
                this.element.style.left = this.mouse.x + 'px';
                this.element.style.top = this.mouse.y + 'px';
                this.canvas.appendChild(this.element)

                this.canvas.style.cursor = "crosshair";
            }
        })

        /* If the this.element is done being drawn and is in a valid
        * location, place it onto the screen */
        this.canvas.addEventListener('mouseup', e => {
            if (this.drawSwitch) {
                if (this.element && !this.newRectIntersect(this.element)) {
                    var title = document.createElement('div')
                    var inp = document.createElement('input')

                    title.classList.add('rectangle-header')
                    title.classList.add('center-horizontal')
                    title.classList.add('center-vertical')
                    this.element.appendChild(title)

                    inp.classList.add('rectangle-title')
                    inp.placeholder = 'No value entered'
                    inp.type = 'text'
                    
                    title.appendChild(inp)
                } else {
                    if (this.element !== null) {
                        console.log('Please construct the rectangles such that they do not intersect')
                    }
                    this.element.remove()
                }
                this.element = null
                this.canvas.style.cursor = "default";
            }
            this.drawSwitch = false;
        })
    }

    /* Set this.mouse location */
    setMousePosition(e) {
        var ev = e || window.event; //Moz || IE
        if (ev.pageX) { //Moz
            this.mouse.x = ev.pageX + window.pageXOffset;
            this.mouse.y = ev.pageY + window.pageYOffset;
        } else if (ev.clientX) { //IE
            this.mouse.x = ev.clientX + document.body.scrollLeft;
            this.mouse.y = ev.clientY + document.body.scrollTop;
        }
    };

    /* Detect if new rectangle intersects with any existing rectangles */
    newRectIntersect(el) {
        var inside = false
        var rect;
        var rects = document.querySelectorAll('.rectangle')

        var el = {
            width: Number(el.style.width.slice(0, -2)),
            height: Number(el.style.height.slice(0, -2)),
            left: Number(el.style.left.slice(0, -2)),
            top: Number(el.style.top.slice(0, -2)),
        }

        for (let i = 0; i < rects.length; i++) {
            if (rects[i] == el)
                continue

            rect = {
                width: Number(rects[i].style.width.slice(0, -2)),
                height: Number(rects[i].style.height.slice(0, -2)),
                left: Number(rects[i].style.left.slice(0, -2)),
                top: Number(rects[i].style.top.slice(0, -2)),
            }

            let arr = [
                rect.left <= (el.left + el.width),
                rect.top <= (el.top + el.height),
                el.left <= (rect.left + rect.width),
                el.top <= (rect.top + rect.height)
            ]

            if (arr.every(i => i)) {
                inside = true
                break
            }
        }
        return inside
    }

    /* Creates a red circle at the location a user clicked */
    makeCirc(x, y) {
        /* Create element, add styles (class doesn't work
         * for some reason) */
        var circ = document.createElement('div');
        circ.className = "client-click-pos";
        circ.style.borderRadius = "50%";
        circ.style.width = "10px";
        circ.style.height = "10px";
        circ.style.backgroundColor = "red";
        circ.style.position = "absolute";
        circ.style.top = String(y)+'px'; // TODO: Adjust for different screen sizes
        circ.style.left = String(x)+'px';

        /* Append the child to the canvas */
        this.canvas.appendChild(circ);

        /* Log click as failure for now */
        this.data[this.trial].incorrectClicks.push([x, y])
        this.data[this.trial].totalClicks += 1
    }

    /* Finish logging this trial's data, start next trial */
    nextImage(succ) {
        this.data[this.trial].timeElapsed = this.getTime() - this.trialStartTime

        if (succ) {
            let numClicks = this.data[this.trial].incorrectClicks.length
            this.data[this.trial].correctClicks.push(this.data[this.trial].incorrectClicks[numClicks - 1])
            this.data[this.trial].incorrectClicks.pop()
        }

        this.data[this.trial].correct = succ
        this.trial += 1
        this.trialStartTime = this.getTime()
    }

    /* Gets current time of game */
    getTime() {
        return new Date().getTime();
    }

    /* Get the current state of the game data */
    getData() {
        return this.data
    }
}