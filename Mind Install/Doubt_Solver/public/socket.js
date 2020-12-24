$(document).ready(function() {
    $(function () {
        const socket = io();
        $('form').submit(function(e) {
            e.preventDefault(); // prevents page reloading
            console.log($('#query').val());
            socket.emit('new thread', $('#query').val());
            $('#query').val('');
            return false;
        });
        socket.on('new thread', function(msg){
            let newMsg = '<div class="main-thread card card-body bg-light blockquote">' +
                        '<p class="mb-0">thread1 '+msg+'</p>' +
                        '<div class="blockquote-footer">student name, time</div></div>'
            $('#physics').append(newMsg);
        });
        socket.on('reply thread', function(msg){
            let newMsg = '<div class="sub-thread card card-body bg-light blockquote">' +                      
                        '<p class="mb-0">'+msg+'</p>' +
                        '<div class="blockquote-footer">student name, time</div></div>'
            $('#physics_1').append(newMsg);
        });
    });
})