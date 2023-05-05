const Message = ({ message }) => {
  return (
    <div>
      <div className="chat chat-start">
        <div className="chat-bubble bg-white border border-black">
          <p className="text-black">{message.text}</p>
        </div>
      </div>
    </div>
  );
};

export default Message;
