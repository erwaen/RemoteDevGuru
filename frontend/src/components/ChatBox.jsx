import React, { useState } from "react";
import Message from "./Message";
import SendMessage from "./SendMessage";

const ChatBox = () => {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = (text) => {
    const newMessage = { id: messages.length + 1, text, sentByUser: true };
    setMessages([...messages, newMessage]);
  };

  return (
    <div className="containerWrap pb-1 pt-1 sm:p-3" style={{ border: "1px solid #525252" }}>
      {messages.map((message, index) => (
        <Message key={index} message={message} />
      ))}
      <SendMessage onSendMessage={handleSendMessage} messages={messages} />
    </div>
  );
};

export default ChatBox;
