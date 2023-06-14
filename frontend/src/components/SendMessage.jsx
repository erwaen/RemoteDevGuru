import React, { useState } from "react";
import { FaPaperPlane } from "react-icons/fa";

const SendMessage = ({ onSend, suggestedQuestions }) => {
  const [value, setValue] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleChange = (e) => {
    setValue(e.target.value);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSendMessage();
    }
  };

  const handleSendMessage = () => {
    if (value === "") {
      setErrorMessage("Por favor, escribe un mensaje...");
      return;
    }
    onSend(value);
    setValue("");
    setErrorMessage("");
  };

  const handleSuggestedQuestionClick = (question) => {
    setValue(question);
  };

  const suggestedQuestion = suggestedQuestions[0] || "";

  return (
    <div className="fixed bottom-3 left-7 right-7 items-center">
      {suggestedQuestions.length > 0 && (
        <button
          className="px-4 py-2 bg-gray-200 rounded-lg mb-2"
          onClick={() => handleSuggestedQuestionClick(suggestedQuestion)}
        >
          {suggestedQuestion}
        </button>
      )}

      <div className="flex justify-between">
        <input
          type="text"
          className="w-full h-12 bg-gray-300 rounded-l-lg ps-5"
          value={value}
          placeholder="Escribe algo..."
          onChange={handleChange}
          onKeyDown={handleKeyDown}
        />

        <button
          className="flex w-20 h-12 rounded-r-lg items-center justify-center bg-zinc-800"
          onClick={handleSendMessage}
        >
          <FaPaperPlane style={{ color: "#ffffff" }} />
        </button>
      </div>

      <p className="text-red-500 text-xs italic mt-2">{errorMessage}</p>
    </div>
  );
};

export default SendMessage;
