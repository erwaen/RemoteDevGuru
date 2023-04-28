const Message = ({ message }) => {
  return (
    <div>
      <div className="chat chat-start">
        <div className="chat-bubble">{message.text}</div>
      </div>
    </div>
  );
};

export default Message;
