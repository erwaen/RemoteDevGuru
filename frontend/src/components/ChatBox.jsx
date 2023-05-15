import React, { useState } from "react";
import Message from "./Message";
import SendMessage from "./SendMessage";

const ChatBox = ({ messages }) => {
  //console.log(messages)
  return (
    <div>
      {messages.map((message, index) => (
        <Message key={index} message={message}></Message>
      ))}
    </div>
  );

  // //const [messages, setMessages] = useState([]);

  // const handleSendMessage = (text) => {
  //   const newMessage = { id: messages.length + 1, text, sentByUser: true };
  //   setMessages([...messages, newMessage]);
  // };

  // /*return (
  //   <div className="containerWrap pb-1 pt-1 sm:p-3" style={{ border: "1px solid #525252" }}>
  //     {messages.map((message, index) => (
  //       <Message key={index} message={message} />
  //     ))}
  //     <SendMessage onSendMessage={handleSendMessage} messages={messages} />
  //   </div>
  // );*/

  // return (
  //   <>
  //     <div className="chat chat-start">
  //       <div className="chat-bubble">
  //         It's over Anakin, <br />I have the high ground.
  //       </div>
  //     </div>
  //     <div className="chat chat-end">
  //       <div className="chat-bubble">{}</div>
  //     </div>
  //     <SendMessage />
  //   </>
  // );
};

export default ChatBox;
