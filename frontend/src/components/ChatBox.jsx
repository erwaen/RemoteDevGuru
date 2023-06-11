import React from "react";
import Message from "./Message";

const ChatBox = ({ messages }) => {
  return (
    <div>
      {messages.map((message, index) => (
        <Message key={index} message={message} /> // Se eliminó el cierre explícito de la etiqueta Message
      ))}
      <br />
      <br />
      <br />
      <br />
    </div>
  );
};

export default ChatBox;
