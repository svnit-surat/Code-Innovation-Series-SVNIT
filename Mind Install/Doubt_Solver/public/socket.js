$(function () {
    var socket = io();
    $('form').submit(function(e) {
        e.preventDefault();
        socket.emit('chat message', $('#question').val());
        $('#question').val('');
        return false;
    });
});