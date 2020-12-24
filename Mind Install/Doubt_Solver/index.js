const express = require('express');
const path = require('path');

const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

const port = 3000;
let username = 'New User';

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'));

app.get('/', (req, res) => {
    res.render('index');
});

app.post('/', (req, res) => {
    username = req.body.firstname;
    res.redirect('/home');
})

app.get('/home', (req, res) => {
    res.render('query', { username });
});

app.post('/home', (req, res) => {
    console.log("Question ", req.body)
    res.redirect('/home');
})

io.on('connection', (socket) => {
    console.log({username});
    console.log(`${username} connected`);

    
    socket.on('new thread', (msg, {username}) => {
        io.emit('new thread', msg, {username});
    });

    socket.on('new physics thread', (msg, {username}) => {
        io.emit('new physics thread', msg, {username});
    });
    socket.on('new maths thread', (msg) => {
        io.emit('new physics thread', msg);
    });
    socket.on('new chemistry thread', (msg) => {
        io.emit('new physics thread', msg);
    });
    socket.on('new computer thread', (msg) => {
        io.emit('new physics thread', msg);
    });
    
    socket.on('reply thread', (msg) => {
        io.emit('reply thread', msg);
    });
    socket.on('disconnect', () => {
        console.log(`${username} disconnected`);
    });
});

http.listen(3000, () => {
    console.log(`Server listening on port ${port}`);
});