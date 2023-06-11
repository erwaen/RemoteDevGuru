import React from "react";

const Message = ({ message }) => {
  const bubbleStyle = {
    backgroundColor: message.sender === "user" ? "#006400" : "#333333", // Cambio: Establece el color de fondo según el remitente del mensaje
    color: "#FFFFFF", // Cambio: Establece el color de texto en blanco para ambos remitentes
  };

  return (
    <div>
      <div
        className={
          message.sender === "user" ? "chat chat-end" : "chat chat-start"
        }
      >
        <div className="chat-bubble bg-zinc-700 flex" style={bubbleStyle}>
          <p className="flex">{message.text}</p>
        </div>
      </div>
    </div>
  );
};

export default Message;
