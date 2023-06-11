import React, { useState } from "react";
import Message from "./Message";

const ChatBox = ({ messages }) => {
  return (
    <div className="">
      {messages.map((message, index) => (
        <Message key={index} message={message}></Message>
      ))}
      <br />
      <br />
      <br />
      <br />
    </div>
  );
};

export default ChatBox;
