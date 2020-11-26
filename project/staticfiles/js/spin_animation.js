/*Link to HTML did not work because animation needs to be named animation.js*/

var go_to_game = 0;

function go() {
    if (go_to_game == 1) {
        window.location.replace("/home/light");
        
    }
    else if (go_to_game == 2) {
        window.location.replace("/home/spinner");
    }
    else if (go_to_game == 3) {
        window.location.replace("/accounts/signin2");
    }
    else if (go_to_game == 4) {
        window.location.replace("/home/pop");
    }
    else if (go_to_game == 5) {
        window.location.replace("/home/main");
    }
    else if (go_to_game == 6) {
        window.location.replace("/home/pancake");
        
    }
    else if (go_to_game == 7) {
        window.location.replace("/");
        
      
    }
}

function anim() {
    var x = 1024;
    var y = 9999;
    // animation for the spinner
    var deg = Math.abs(Math.floor(Math.random() * (x-y)) + y) ;
    document.getElementById('box').style.transform = "rotate("+ deg + "deg)";




    var deg2 = deg % 360;
    console.log(deg2)
    if (deg2 > 0 && deg2 <= 15) {
        document.getElementById('go').style.color = 'red';
        go_to_game = 1
        
    } 
    else if(deg2 > 15 && deg2 <= 60 ) {
        document.getElementById('go').style.color = 'green';

    }
    else if (deg2 > 60 && deg2 <= 105 ){
        document.getElementById('go').style.color = 'blue';
        go_to_game = 2
     
    }
    else if (deg2 > 105 && deg2 <= 150 ){
        document.getElementById('go').style.color = 'red';
        go_to_game = 3

    }
    else if (deg2 > 150 && deg2 <= 195 ){
        document.getElementById('go').style.color = 'yellow';
        go_to_game = 4

    }
    else if (deg2 > 195 && deg2 <= 240 ){
        document.getElementById('go').style.color = 'blue';
        go_to_game = 5

    }
    else if (deg2 > 240 && deg2 <= 285 ){
        document.getElementById('go').style.color = 'green';
        go_to_game = 6
    }
    else if (deg2 > 285 && deg2 <= 330){
        document.getElementById('go').style.color = 'yellow';
        go_to_game = 7
    }
    else{
        document.getElementById('go').style.color = 'red';
        go_to_game = 1
    }

    



    // arrow animation
    var element = document.getElementById('mainbox');
    element.classList.remove('animate');
    setTimeout(function(){
        element.classList.add('animate');
    }, 5000); 

}