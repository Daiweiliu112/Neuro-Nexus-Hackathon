/* Drawing rectangles with mouse clicks
 * https://stackoverflow.com/questions/17408010/drawing-a-rectangle-using-click-mouse-move-and-click
 * Accessed August 15, 2020 */

function initDraw(canvas) {
    var mouse = {
        x: 0,
        y: 0,
        startX: 0,
        startY: 0
    };
    var drawSwitch = false;

    document.getElementById('draw-switch').addEventListener('click', (e) => {
        if (!element)
            drawSwitch = !drawSwitch;
    })

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

    
    var element = null;
    canvas.onmousemove = function (e) {
        setMousePosition(e);
        if (element !== null) {
            element.style.width = Math.abs(mouse.x - mouse.startX) + 'px';
            element.style.height = Math.abs(mouse.y - mouse.startY) + 'px';
            element.style.left = (mouse.x - mouse.startX < 0) ? mouse.x + 'px': mouse.startX + 'px';
            element.style.top = (mouse.y - mouse.startY < 0) ? mouse.y + 'px': mouse.startY + 'px';
        }
    }

    function newRectIntersect(element) {
        var inside = false
        var rect;
        var rects = document.querySelectorAll('.rectangle')

        var el = {
            width: Number(element.style.width.slice(0,-2)),
            height: Number(element.style.height.slice(0,-2)),
            left: Number(element.style.left.slice(0,-2)),
            top: Number(element.style.top.slice(0,-2)),
        }
        
        for (let i = 0; i < rects.length; i++) {
            if (rects[i] == element)
                continue

            rect = {
                width: Number(rects[i].style.width.slice(0,-2)),
                height: Number(rects[i].style.height.slice(0,-2)),
                left: Number(rects[i].style.left.slice(0,-2)),
                top: Number(rects[i].style.top.slice(0,-2)),
            }


            let arr = [rect.left <= (el.left + el.width),
                        el.left <= (rect.left + rect.width),
                        rect.top <= (el.top + el.height),
                        el.top <= (rect.top + rect.height)]
            
             if (arr.every(i => i)) {
                inside = true
                break
            }
        }
        return inside
    }
    
    canvas.addEventListener('mousedown', e => {
        if (drawSwitch) {
            mouse.startX = mouse.x;
            mouse.startY = mouse.y;
            element = document.createElement('div');
            element.className = 'rectangle'
            element.style.left = mouse.x + 'px';
            element.style.top = mouse.y + 'px';
            canvas.appendChild(element)
            
            
            canvas.style.cursor = "crosshair";
        }
    })
    
    canvas.addEventListener('mouseup', e => {
        if (drawSwitch) {
            if (element && !newRectIntersect(element)) {
                var title = document.createElement('div')
                var inp = document.createElement('input')
                
                title.classList.add('rectangle-header')
                title.classList.add('center-horizontal')
                title.classList.add('center-vertical')
                element.appendChild(title)
        
                inp.classList.add('rectangle-title')
                inp.placeholder = 'No value entered'
                inp.type = 'text'
                                
                title.appendChild(inp)
            } else if (element !== null) {
                console.log('Please construct the rectangles such that they do not intersect')
                element.remove()
            }
            element = null
            canvas.style.cursor = "default";
        }
        drawSwitch = false;
    })
}