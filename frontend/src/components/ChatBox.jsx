import React from "react";
import Message from "./Message";

const ChatBox = ({ messages }) => {
  return (
    <div className="fixed top-[60px] bottom-[95px] right-0 left-0 overflow-y-auto">
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
