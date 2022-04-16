var messages = [], //array that hold the record of each string in chat
  lastUserMessage = "", //keeps track of the most recent input string from the user
  botMessage = "", //var keeps track of what the chatbot is going to say
  botName = "NBA Bot"; //name of the chatbot

async function chatbotResponse() {
  // get response for chatbot
  botMessage = "I'm confused"; //the default message
  let res = await getResponse(lastUserMessage);
  console.log(res);
  botMessage = res['output'];
}

async function getResponse(input) {
  // fetch API
  // https://stackoverflow.com/questions/45018338/javascript-fetch-api-how-to-save-output-to-variable-as-an-object-not-the-prom
  // https://dmitripavlutin.com/javascript-fetch-async-await/#2-fetching-json

  // let url = "https://api.chucknorris.io/jokes/random?category=" + input;
  // let url = "http://localhost:5000/responses/" + encodeURIComponent(input); // works
  let url = "responses/" + encodeURIComponent(input);

  try {

    const response = await fetch(url, {
      method: 'GET',
    });

    const data = await response.json();
    return data;

  } catch (error) {
    console.error(error);
  }
}

async function newEntry() {
  // control the overall input and output
  // runs each time enter is pressed

  //if the message from the user isn't empty then run 
  if (document.getElementById("chatbox").value != "") {
    
    //pulls the value from the chatbox ands sets it to lastUserMessage
    lastUserMessage = document.getElementById("chatbox").value;
    
    //sets the chat box to be clear
    document.getElementById("chatbox").value = "";
    
    //adds the value of the chatbox to the array messages
    messages.push("<b>Human</b>: " + lastUserMessage);
    
    //Speech(lastUserMessage);  //says what the user typed outloud
    //sets the variable botMessage in response to lastUserMessage
    await chatbotResponse();
    
    //add the chatbot's name and message to the array messages
    messages.push("<b>" + botName + ":</b> " + botMessage);
        
    //outputs the last few array elements of messages to html
    for (var i = 1; i < 8; i++) {
      if (messages[messages.length - i])
        document.getElementById("chatlog" + i).innerHTML = messages[messages.length - i];
    }
  }
}

// runs the keypress() function when a key is pressed
document.onkeypress = keyPress;
// if the key pressed is 'enter' runs the function newEntry()
function keyPress(e) {
  var x = e || window.event;
  var key = (x.keyCode || x.which);
  if (key == 13 || key == 3) {
    // runs this function when enter is pressed
    newEntry();
  }
}

function placeHolder() {
  // clears the placeholder text ion the chatbox
  // this function is set to run when the users brings focus to the chatbox, by clicking on it
  document.getElementById("chatbox").placeholder = "";
}