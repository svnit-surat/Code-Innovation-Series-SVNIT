
const router = require('express').Router();
const userData = require('../userdata/userData.js');

// Register route
router.post('/register', (req, res) => {
  try {

    const { username, email, password } = req.body;

    if(!userData.hasOwnProperty(username)) {
      res.json(userData[username]);
    }
    else {
      res.status(401).json("User already exists");
    }



  } catch (err) {
    console.error(err.message);
    res.status(500).json("Server error");
  }
});

// Login route
router.post('/login', (req, res) => {
  try {

    const { email, password } = req.body;

    if(email in userData) {
      if(userData[email]["password"] === password) {
        res.json(userData[email]);
      }
      else {
        res.status(401).json("Wrong password!");
      }
    }
    else {
      res.status(401).json("User doesn't exist!");
    }

  } catch (err) {
    console.error(err.message);
    res.status(500).json("Server error");
  }
});

module.exports = router;
