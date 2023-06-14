import { useState } from "react";
import Navbar from "../components/NavBar";
import ChatBox from "../components/ChatBox";
import SendMessage from "../components/SendMessage";

const ChatRoom = () => {
  const [messages, setMessages] = useState([]);
  const [suggestedQuestions, setSuggestedQuestions] = useState([]);

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

      const data = await response.json();

      data.respuestas.forEach((element) => {
        addMessageList(element, "bot");
      });

      const suggestedQuestions = data.preguntas_sugeridas;
      setSuggestedQuestions(suggestedQuestions);
    } catch (error) {
      console.log(error);
    }
  };

  function addMessageList(text, user) {
    setMessages((prevMessages) => [
      ...prevMessages,
      { text: text, sender: user },
    ]);
  }

  return (
    <div>
      <Navbar></Navbar>
      <ChatBox messages={messages}></ChatBox>
      <SendMessage onSend={handleSend} suggestedQuestions={suggestedQuestions}></SendMessage>
    </div>
  );
};

export default ChatRoom;
