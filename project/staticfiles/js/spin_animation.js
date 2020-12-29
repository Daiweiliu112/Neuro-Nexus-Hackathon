/*Link to HTML did not work because animation needs to be named animation.js*/

var go_to_game = 0;

function go() {
    if (go_to_game == 1) {
        window.location.replace("/home/light");
        
    }
    else if (go_to_game == 2) {
        window.location.replace("/home/pop");
    }
    else if (go_to_game == 3) {
        window.location.replace("/home/custom_game");
    }
    else if (go_to_game == 4) {
        window.location.replace("/home/light");
    }
    else if (go_to_game == 5) {
        window.location.replace("/home/pop");
    }
    else if (go_to_game == 6) {
        window.location.replace("/home/pancake");
        
    }
    else if (go_to_game == 7) {
        window.location.replace("/home/pancake");
        
      
    }else if (go_to_game == 8) {
        window.location.replace("/home/cookies")
    }
    else {
        window.location.replace("/home/light")
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
   
        go_to_game = 1
        
    } 
    else if(deg2 > 15 && deg2 <= 60 ) {
        go_to_game = 2


    }
    else if (deg2 > 60 && deg2 <= 105 ){

        go_to_game = 3
     
    }
    else if (deg2 > 105 && deg2 <= 150 ){
  
        go_to_game = 4

    }
    else if (deg2 > 150 && deg2 <= 195 ){

        go_to_game = 5

    }
    else if (deg2 > 195 && deg2 <= 240 ){

        go_to_game = 6

    }
    else if (deg2 > 240 && deg2 <= 285 ){

        go_to_game = 7
    }
    else if (deg2 > 285 && deg2 <= 330){
 
        go_to_game = 8
    }
    else{
  
        go_to_game = 1
    }

    



    // arrow animation
    var element = document.getElementById('mainbox');
    element.classList.remove('animate');
    setTimeout(function(){
        element.classList.add('animate');
    }, 5000); 

}