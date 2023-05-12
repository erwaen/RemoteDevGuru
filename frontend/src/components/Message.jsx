import React from "react";

const Message = ({ message }) => {
  return (
    <div>
      <div className="chat chat-start">
        <div className="chat-bubble bg-white border border-black">
          <p className="text-black text-sm md:text-base">{message.text}</p>
        </div>
      </div>
    </div>
  );
};

export default Message;

