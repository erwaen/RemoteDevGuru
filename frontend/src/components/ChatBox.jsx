import React, { useState } from "react";
import Message from "./Message";

const ChatBox = ({ messages }) => {
  return (
    <div>
      {messages.map((message, index) => (
        <Message key={index} message={message}></Message>
      ))}
    </div>
  );
};

export default ChatBox;
