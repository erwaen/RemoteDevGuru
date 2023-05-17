import React from "react";

const Message = ({ message }) => {
  //return a chat bubble per message
  return (
    <div>
      <div className="chat chat-end">
        <div className="chat-bubble bg-zinc-700 flex">
          <p className="flex">{message}</p>
        </div>
      </div>
    </div>
  );
};

export default Message;
