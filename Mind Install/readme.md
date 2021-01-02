# Doubt Solver

"Divide and Conquer"

This website is a doubts solving platform kind of like a discussion forum in which students can ask their doubts occured during online classes of different subjects to the respective faculty. A technique
namely ***Conversation Threading*** is used in this platform so that the student's doubts can be solved in time effective manner.

### Why this app is different?

Normally when students have doubt regarding a topic, they use the general messaging panel to communicate with the faculty. But the problem in this system is that if some other student has another doubt at the same time, then he asks it on the messaging panel which opens up an entire new conversation between an ongoing communication. He can also choose to wait till the previous student's query ends but if there are (as an example) two faculties taking the class, then both of them could resolve everyone's queries if they split.
For that, we used messaging threads which helps students to create new threads (start new doubt conversation)
or join existing threads (reply to old conversations). Each thread means a different topic, so the doubt 
solving process is carried out effectively. Lot of the time, spam messages make it difficult to reach at any doubt for any common messaging panel. This app doesn't remove all the spam but it definitely reduces it as the conversations are divided. If in future another student has some doubt on a topic already 
discussed before he/she can continue to clear her doubts on respective thread instead of scrolling through
mixed long messages.

## Techstack 
-> Bootstrap
-> Node.js
-> Express
-> Socket.io

## Running Locally

1) Clone the repo, `cd` into the project directory
2) Then run "node index" to start the server
3) Navigate to "https://localhost:3000" to see the project running