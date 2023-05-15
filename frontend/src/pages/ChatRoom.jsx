import { useState } from "react";
import ChatBox from "../components/ChatBox";
import SendMessage from "../components/SendMessage";

const ChatRoom = () => {
  const [messages, setMessages]=useState([])
  //console.log(messages)

  const handleSend=(value)=>{
    const newMessage=value
    setMessages([...messages, newMessage])
    console.log(messages)
  }

  return (
    <div>
      <ChatBox messages={messages}></ChatBox>
      <SendMessage onSend={handleSend}></SendMessage>
      {/* <ChatBox /> */}
      {/*<SendMessage/>*/}
    </div>
  );
};

export default ChatRoom;