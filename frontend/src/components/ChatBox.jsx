import React from "react";
import Message from "./Message";

const ChatBox = ({ messages }) => {
  return (
    <div>
      {/* Se cambió la sintaxis de cierre de la etiqueta Message */}
      {messages.map((message, index) => (
        <Message key={index} message={message} /> // Se eliminó el cierre explícito de la etiqueta Message
      ))}
    </div>
  );
};

export default ChatBox;
