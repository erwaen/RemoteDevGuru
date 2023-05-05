import Message from "./Message";

const ChatBox = () => {
  const messages = [
    { id: 1, text: "Hola! Comencemos" },
    {
      id: 2,
      text: "Genial!",
    },
  ];

  return (
    <div className="containerWrap pb-1 pt-1" style={{border: "1px solid #525252"}}>
      {messages.map((message) => (
        <Message key={message.id} message={message} />
      ))}
    </div>
  );
};

export default ChatBox;
