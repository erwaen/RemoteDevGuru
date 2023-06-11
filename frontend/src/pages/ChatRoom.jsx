import { useState } from "react";
import NavBar from "../components/NavBar";
import ChatBox from "../components/ChatBox";
import SendMessage from "../components/SendMessage";

const ChatRoom = () => {
  const [messages, setMessages] = useState([]);

  const handleSend = (value) => {
    addMessageList(value, "user");
    connectingToBackend(value);
  };

  const connectingToBackend = async (value) => {
    try {
      const response = await fetch(
        "http://localhost:8001/api/chat/?prompt=" + value,
        {
          method: "GET",
        }
      );

      //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

      //response
      const data = await response.json();
      data.respuestas.forEach((element) => {
        addMessageList(element, "bot");
      });
    } catch (error) {

      console.log(error);
    }
  };

  //add new messages to the list by defining their sender
  function addMessageList(text, user) {
    setMessages((prevMessages) => [
      ...prevMessages,
      { text: text, sender: user },
    ]);
  }

  return (
    <div>
      <NavBar></NavBar>
      <ChatBox messages={messages}></ChatBox>
      <SendMessage onSend={handleSend}></SendMessage>
    </div>
  );
};

export default ChatRoom;
