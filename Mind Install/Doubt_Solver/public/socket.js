$(document).ready(function() {
    $(function () {
        const socket = io();
        let physics_id = 1;
        $('form').submit(function(e) {
            e.preventDefault(); // prevents page reloading
            console.log($('#query').val());
            if('thread_')
            socket.emit('new thread', $('#query').val());
            $('#query').val('');
            return false;
        });
        socket.on('new thread', function(msg, username){            
            let dt = new Date();
            let time = dt.getHours() + ":" + dt.getMinutes() + ":" + dt.getSeconds();
            let newMsg = '<div class="main-thread card card-body bg-light blockquote">' +
                            '<p class="mb-0">'+msg+'</p>' +
                        '<div class="blockquote-footer">' + username['username'] + ', '+time+'</div>' +
                        '<div class="text-right">'+
                        '&nbsp;&nbsp;&nbsp;&nbsp; 30 &uarr; upvotes</div>'+
                        '<form class="form" method="POST" action="/home"><div class="form-row"><div class="col-12 col-lg-10 col-sm-10"><textarea type="text" class="form-control mb-2 mr-sm-2" id="query" name="query" placeholder="Enter your question"  row="200"></textarea></div><div class="col col-lg-2 col-sm"><button type="submit" class="btn btn-primary mb-2">Send</button></div></div></form>'
                        +'</div>'
                        
            $('#physicsMainThread').append(newMsg);
            physics_id++;
        });
        socket.on('reply thread', function(msg){
            let newMsg = '<div class="sub-thread card card-body bg-light blockquote">' +                      
                        '<p class="mb-0">'+msg+'</p>' +
                        '<div class="blockquote-footer">student name, time</div></div>'
            $('#physics_1').append(newMsg);
        });
    });
})