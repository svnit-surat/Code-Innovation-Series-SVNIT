$(document).ready(function() {
    $(function () {
        const socket = io();
        let physics_id = 1, 
            chemistry_id = 1
            maths_id = 1
            comps_id = 1;
        let phyThread = 'physics_'+physics_id,
            mathsThread = 'physics_'+physics_id,
            chemThread = 'physics_'+physics_id,
            compsThread = 'physics_'+physics_id;

        // handle submit for every new thread
        $('#newFormPhysics').submit(function(e) {
            e.preventDefault(); // prevents page reloading
            let subjectID = $(this).parent().children()['1'].id;
            let message = $(this).parent().find('input[name="askQuery"]').val();
            let payload = {
                subjectID,
                threadID: phyThread,
                message
            };          
            console.log(payload);
            socket.emit('new thread', payload);

            $(this).parent().find('input[name="askQuery"]').val('');
            physics_id++;
            phyThread = 'physics_'+physics_id;
            return false;
        });

        $('#newFormMaths').submit(function(e) {
            e.preventDefault(); // prevents page reloading
            let subjectID = $(this).parent().children()['1'].id;
            let message = $(this).parent().find('input[name="askQuery"]').val();
            let payload = {
                subjectID,
                threadID: mathsThread,
                message
            };          
            console.log(payload);
            socket.emit('new thread', payload);

            $(this).parent().find('input[name="askQuery"]').val('');
            maths_id++;
            mathsThread = 'maths_'+maths_id;
            return false;
        });

        $('#newFormChemistry').submit(function(e) {
            e.preventDefault(); // prevents page reloading
            let subjectID = $(this).parent().children()['1'].id;
            let message = $(this).parent().find('input[name="askQuery"]').val();
            let payload = {
                subjectID,
                threadID: chemThread,
                message
            };          
            console.log(payload);
            socket.emit('new thread', payload);

            $(this).parent().find('input[name="askQuery"]').val('');
            chemistry_id++;
            chemThread = 'chemistry_'+chemistry_id;
            return false;
        });

        $('#newFormComps').submit(function(e) {
            e.preventDefault(); // prevents page reloading
            let subjectID = $(this).parent().children()['1'].id;
            let message = $(this).parent().find('input[name="askQuery"]').val();
            let payload = {
                subjectID,
                threadID: compsThread,
                message
            };          
            console.log(payload);
            socket.emit('new thread', payload);

            $(this).parent().find('input[name="askQuery"]').val('');
            comps_id++;
            compsThread = 'comps_'+comps_id;
            return false;
        });


        // handle submit for every reply thread
        $('#replyFormphysicsMainThread').submit(function(e) {
            e.preventDefault(); // prevents page reloading
            let threadID = $(this).parent().id;
            let message = $(this).find('input[name="replyQuery"]').val();
            let payload = {
                threadID,
                message
            };          
            console.log(payload);
            //socket.emit('reply thread', payload);

            $(this).find('input[name="replyQuery"]').val('');
            return false;
        });


        // handle sockets communication
        socket.on('new thread', function(payload){  
            let dt = new Date();
            let time = dt.getHours() + ":" + dt.getMinutes() + ":" + dt.getSeconds();
            let newMsg = '<div id="'+ payload.threadID +'" class="main-thread card card-body bg-light blockquote">' +
                            '<p class="mb-0">'+ payload.message +'</p>' +
                        '<div class="blockquote-footer">' + payload.username + ', '+time+'</div>' +
                        '<div class="text-right">'+
                        '&nbsp;&nbsp;&nbsp;&nbsp; 30 &uarr; upvotes</div>'+
                        '<form id="replyForm'+ payload.subjectID+'" class="form" method="POST" action="/home"><div class="form-row"><div class="col-12 col-lg-10 col-sm-10">'+
                        '<input type="text" class="form-control mb-2 mr-sm-2" id="query" name="replyQuery" placeholder="Enter your question"></input>'+ 
                        '</div><div class="col col-lg-2 col-sm"><button type="submit" class="btn btn-primary mb-2">Send</button>'+
                        '</div></div></form></div>';
                        
            $('#'+payload.subjectID).append(newMsg);
        });

        socket.on('reply thread', function(payload){
            let newMsg = '<div class="sub-thread card card-body bg-light blockquote">' +                      
                        '<p class="mb-0">'+payload.message+'</p>' +
                        '<div class="blockquote-footer">student name, time</div></div>'
            $('#'+payload.threadID).append(newMsg);
        });
    });
})