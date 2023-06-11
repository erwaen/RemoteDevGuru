import { useState } from "react";
import ChatBox from "../components/ChatBox";
import SendMessage from "../components/SendMessage";

const ChatRoom = () => {
  const [messages, setMessages] = useState([]);
  const [suggestedQuestions, setSuggestedQuestions] = useState([]); // Se agregó un nuevo estado para las preguntas sugeridas

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

      // Obtener preguntas sugeridas
      const suggestedQuestions = data.preguntas_sugeridas; // Asignar las preguntas sugeridas desde la respuesta
      setSuggestedQuestions(suggestedQuestions); // Actualizar el estado con las preguntas sugeridas

      data.respuestas.forEach((element) => {
        addMessageList(element, "bot");
      });
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
      <ChatBox messages={messages}></ChatBox>
      <SendMessage onSend={handleSend}></SendMessage>
    </div>
  );
};

export default ChatRoom;
