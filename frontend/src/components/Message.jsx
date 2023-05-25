import React from "react";

const Message = ({ message }) => {
  //return a chat bubble per message
  //in the ternary operation it establishes which side the message bubble is show on
  //left side=user
  //right side=Bot
  return (
    <div>
      <div
        className={
          message.sender == "user" ? "chat chat-end" : "chat chat-start"
        }
      >
        <div className="chat-bubble bg-zinc-700 flex">
          <p className="flex">{message.text}</p>
        </div>
      </div>
    </div>
  );
};

export default Message;
