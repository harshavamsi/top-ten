   function upvoteme(pid){
        console.log(pid)
        console.log(this)
        var postid = pid;

$.get('/upvote/', {post_id: postid}, function(data){
        id = $("#" + pid )
        id.html(data);
        if($("."+pid).text()!="Upvoted"){
             $("."+pid).text("Upvoted");
        $("."+pid).css("background","#3498db");
        
        }
        else{
            $("."+pid).text("Upvote");
        $("."+pid).css("background","red");
        
        }         
});
}

$(document).ready(function() {
    var x_timer; 
    console.log("Checking")   
    $("#usernam").keyup(function (e){
        clearTimeout(x_timer);
        var user_name = $(this).val();
        x_timer = setTimeout(function(){
            console.log("Checking")
            $.get('/checkusername/', {username: user_name}, function(data){
                if(data==true){
                    $("#user-result").data("not available");
                }
                else{
                   $("#user-result").data("available"); 
                }
            });
        }, 1000);
    }); 
}




 
