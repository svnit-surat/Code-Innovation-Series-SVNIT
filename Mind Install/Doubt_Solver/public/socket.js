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
                        '<div class="text-right"><button id="thread_'+physics_id+'" type="submit" class="btn btn-outline-primary" >'+
                        '<a data-toggle="modal" onclick="question()">Reply</a>'+
                        '</button>&nbsp;&nbsp;&nbsp;&nbsp; 30 &uarr; upvotes</div></div>'
            $('#physics').append(newMsg);
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