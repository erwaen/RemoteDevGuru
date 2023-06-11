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
      setErrorMessage("Por favor, escribe un mensaje..."); // Se agregó el mensaje de error
      return;
    }
    onSend(value);
    setValue("");
    setErrorMessage("");
  };

  const handleSuggestedQuestionClick = (question) => {
    setValue(question);
  };

  const suggestedQuestion = suggestedQuestions[0] || ""; // Obtener la primera pregunta sugerida o una cadena vacía si no hay preguntas sugeridas

  return (
    <div className="fixed bottom-3 left-7 right-7 items-center">
      {/* Botón para preguntas sugeridas */}
      <button
        className="px-4 py-2 bg-gray-200 rounded-lg"
        onClick={() => handleSuggestedQuestionClick(suggestedQuestion)}
      >
        {suggestedQuestion}
      </button>

      <div className="flex justify-between mt-2">
        {/* Cuadro de entrada de texto */}
        <input
          type="text"
          className="w-full h-12 bg-gray-300 rounded-l-lg ps-5"
          value={value}
          placeholder="Escribe algo..."
          onChange={handleChange}
          onKeyDown={handleKeyDown}
        />

        {/* Botón para enviar el mensaje */}
        <button
          className="flex w-20 h-12 rounded-r-lg items-center justify-center bg-zinc-800"
          onClick={handleSendMessage}
        >
          <FaPaperPlane style={{ color: "#ffffff" }} />
        </button>
      </div>

      {/* Mostrar mensaje de error */}
      <p className="text-red-500 text-xs italic mt-2">{errorMessage}</p>
    </div>
  );
};

export default SendMessage;
